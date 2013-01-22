# Sublime Text 2 Ruby Markers #

A Sublime Text 2 plugin to execute ruby code and update `# =>` markers with the results. The plugin relies on the xmpfilter component of [rcodetools][0].

## Installation ##

### rcodetools ###

Assuming you have [ruby][1] and [rubygems][2] installed, install the rcodetools gem:

    $ gem install rcodetools

### Sublime Text 2 Ruby Markers ###

Using [Package Manager][3]:

 * Use `Cmd+Shift+P` or `Ctrl+Shift+P` to open the Command Palette, then select `Package Control: Install Package`.
 * Look for `Ruby Markers` and install it.

Manually, via git:

    $ git clone https://github.com/mmims/sublime-text-2-ruby-markers.git "<Sublime Text 2 Packages folder>/Ruby Markers"

## Usage ##

 * Add `# => ` after any Ruby statement you would like to see the result of.
 * Use `Alt+Shift+u` or `Tools -> Execute and Update '# =>' Markers` to execute the Ruby code and update the `# => ` markers.

 [0]: http://rubyforge.org/projects/rcodetools
 [1]: http://www.ruby-lang.org
 [2]: http://rubyforge.org/projects/rubygems
 [3]: http://wbond.net/sublime_packages/package_control