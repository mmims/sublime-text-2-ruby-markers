import sublime, sublime_plugin, subprocess, os, re

def is_executable(path):
    return os.path.isfile(path) and os.access(path, os.X_OK)

def  strip_stdout_comments(text):
    return re.sub("(?m)^# >> .*\Z", '', text)

class RubyMarkersCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.get_selections()
        self.load_settings()
        self.execute_and_update(edit)

    def execute_and_update(self, edit):
        text_reg = sublime.Region(0, self.view.size())
        text = self.view.substr(text_reg)
        if self.settings.get('strip_stdout'):
            text = strip_stdout_comments(text)

        startupinfo = None
        currentdir = None
        if sublime.platform() == 'windows':
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            cmd = self.settings.get('xmpfilter_bin_win', ['xmpfilter.bat'])
        else:
            currentfile = self.view.file_name()
            if currentfile == None:
                currentdir = os.path.expanduser('~')
            else:
                currentdir = os.path.dirname(currentfile)
            cmd = self.settings.get('cmd', [])
            cmd.append(self.settings.get('xmpfilter_bin_posix', ['xmpfilter']))

        if self.settings.get('xmpfilter_rails'):
            cmd.append('--rails')
        else:
            if not self.settings.get('xmpfilter_warnings'):
                cmd.append('--no-warnings')

        if self.settings.get('xmpfilter_quiet'):
            cmd.append('--quiet')

        try:
            s = subprocess.Popen(
                cmd,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                cwd=currentdir,
                startupinfo=startupinfo)
            out, err = s.communicate(text.encode('utf8'))
            if s.returncode != None and s.returncode != 0:
                sublime.message_dialog("There was a subprocess error: " + err.decode('utf8'))
                return
            # Replace the entire buffer with output and trim trailing newline
            self.view.replace(edit, text_reg, out.decode('utf8')[:-1])

            # Maintain original selections
            self.reset_selections()

        except OSError as e:
            sublime.message_dialog("There was an OS error: " + e.strerror)


    def get_selections(self):
        self.selections = []
        for index, region in enumerate(self.view.sel()):
            row,col = self.view.rowcol(region.begin())
            self.selections.append(
                {
                    'region': region,
                    'row':    row,
                    'col':    col
                })


    def is_visible(self):
        syntax = self.view.settings().get('syntax').lower()
        return (syntax == 'packages/ruby/ruby.tmlanguage') or \
               (syntax == 'packages/text/plain text.tmlanguage') or \
               self.view.is_scratch()


    def load_settings(self):
        self.settings = sublime.load_settings('ruby_markers.sublime-settings')

        if self.settings.has('check_for_rbenv'):
            sublime.status_message("The `check_for_rbenv` setting has been deprecated. Please remove it and set `ruby_manager` to `rbenv` instead.")
        if self.settings.has('check_for_rvm'):
            sublime.status_message("The `check_for_rvm` setting has been deprecated. Please remove it and set `ruby_manager` to `rvm` instead.")
        if self.settings.has('rbenv_path'):
            sublime.status_message("The `rbenv_path` setting has been deprecated. Please add the path to `rbenv_paths` instead.")

        path_search = self.settings.get('ruby_manager', 'auto').lower()

        if sublime.platform() != 'windows' and path_search != 'none':
            if path_search == 'auto' or path_search != 'rvm':
                rbenv_paths = self.settings.get('rbenv_paths')

                # check for deprecated setting
                user_path = self.settings.get('rbenv_path')
                if user_path != None:
                    rbenv_paths.append(user_path)

                for path in rbenv_paths:
                    path = os.path.expanduser(path)
                    if is_executable(path):
                        self.settings.set('cmd', [path, 'exec'])
                        return

            if path_search == 'auto' or path_search != 'rbenv':
                rvm_paths = self.settings.get('rvm_paths')

                for path in rvm_paths:
                    path = os.path.expanduser(path)
                    if is_executable(path):
                        self.settings.set('cmd', [path, '-S'])
                        return


    def reset_selections(self):
        self.view.sel().clear()

        for selection in self.selections:
            pos = self.view.text_point(selection['row'], selection['col'])
            region = selection['region']
            if region.empty():
                self.view.sel().add(sublime.Region(pos, pos))
            elif region.a < region.b:
                self.view.sel().add(sublime.Region(pos, pos + region.size()))
            else:
                self.view.sel().add(sublime.Region(pos + region.size(), pos))
