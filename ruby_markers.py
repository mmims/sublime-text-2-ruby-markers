import sublime, sublime_plugin, subprocess, os

def is_executable(path):
    return os.path.isfile(path) and os.access(path, os.X_OK)

    
class RubyMarkersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.get_selections()
        self.load_settings()
        self.execute_and_update(edit)
        
    def execute_and_update(self, edit):
        text_reg = sublime.Region(0, self.view.size())
        text = self.view.substr(text_reg)
        
        cmd = self.settings.get("cmd", [])
        cmd.append(self.settings.get("xmpfilter_bin", "xmpfilter"))

        print cmd

        try:
            s = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            out, err = s.communicate(text)
            if s.returncode != None and s.returncode != 0:
                sublime.message_dialog("There was an error: " + err)
                return
            # Replace the entire buffer with output and trim trailing newline
            self.view.replace(edit, text_reg, out[:-1])
            
            # Maintain original selections
            self.reset_selections()

        except OSError, e:
            sublime.message_dialog("There was an error: " + e.strerror)


    def get_selections(self):
        self.selections = []
        for index, region in enumerate(self.view.sel()):
            row,col = self.view.rowcol(region.begin())
            self.selections.append(
                {
                    "region": region,
                    "row":    row,
                    "col":    col
                })


    def load_settings(self):
        self.settings = sublime.load_settings(__name__ + '.sublime-settings')
        
        # Check for rmv or rbenv use
        # Thanks to Ruby Tests plugin <https://github.com/maltize/sublime-text-2-ruby-tests>
        rbenv_cmd = os.path.expanduser('~/.rbenv/bin/rbenv')
        rvm_cmd = os.path.expanduser('~/.rvm/bin/rvm-auto-ruby')
        if self.settings.get("check_for_rbenv") and is_executable(rbenv_cmd):
            self.settings.set("cmd", [rbenv_cmd, 'exec'])
        if self.settings.get("check_for_rvm") and is_executable(rvm_cmd):
            self.settings.set("cmd", [rvm_cmd, '-S'])
        

    def reset_selections(self):
        self.view.sel().clear()

        for selection in self.selections:
            pos = self.view.text_point(selection["row"], selection["col"])
            region = selection["region"]
            if region.empty():
                self.view.sel().add(sublime.Region(pos, pos))
            elif region.a < region.b:
                self.view.sel().add(sublime.Region(pos, pos + region.size()))
            else:
                self.view.sel().add(sublime.Region(pos + region.size(), pos))