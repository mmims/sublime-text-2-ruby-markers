# Sublime Text Ruby Markers #

A Sublime Text plugin to execute ruby code and update `# =>` markers with the results using the xmpfilter component of [rcodetools][0].

## Installation ##

Installation consists of two parts: the *rcodetools* gem (*Ruby Markers* requires the use of *xmpfilter* which is a tool packaged with this gem) and the *Ruby Markers* Sublime Text package.

### rcodetools ###

The *rcodetools* gem **must** be installed on in order for the Ruby Markers plugin to function properly. Assuming you have [ruby][1] and [rubygems][2] installed, install the *rcodetools* gem:

    $ gem install rcodetools

*rbenv* users, please note that you will have to run `$ rbenv rehash` after installing the gem in order for *rbenv* to recognize the *xmpfilter* command.

### Sublime Text Ruby Markers ###

Using [Package Control][3] (recommended):

 * Use `Cmd+Shift+P` or `Ctrl+Shift+P` to open the Command Palette, then select `Package Control: Install Package`.
 * Look for `Ruby Markers` and install it.

Or, determine the `Packages` path for your OS

 * OS X: `~/Library/Application\ Support/Sublime\ Text\ 2/Packages` or `~/Library/Application\ Support/Sublime\ Text\ /Packages`
 * Windows: `%APPDATA%\Sublime Text 2\Packages\` or `%APPDATA%\Sublime Text 3\Packages\`
 * Linux: `~/.config/sublime-text-2/Packages/` or `~/.config/sublime-text-3/Packages/`

and clone the plugin via git:

    $ git clone https://github.com/mmims/sublime-text-2-ruby-markers.git "<Sublime Text Packages folder>/Ruby Markers"

## Usage ##

Use `Alt+Shift+u` or `Tools -> Execute and Update '# =>' Markers` to run the Ruby code through the *xmpfilter* and update the current buffer with the results.

### Capturing STDOUT ###

If you have a Ruby script that looks like:

```ruby
3.times { puts "Hello, World!" }
```
Running the plugin will update the buffer with:

```ruby
3.times { puts "Hello World!" }
# >> Hello World!
# >> Hello World!
# >> Hello World!
```

### Code Annotation ###

Code annotation is performed by using typing `# =>` at the end of the line you want to annotate. There is a ruby snippet that can speed up using this by typing `#` then `tab`.
 
If you have a Ruby script that looks like:

```ruby
def fib(n)
    n < 2 ? n : fib(n-1) + fib(n-2)
end

fib(11)     # => 
fib(23)     # => 
```

Running the plugin will update the buffer with:

```ruby
def fib(n)
    n < 2 ? n : fib(n-1) + fib(n-2)
end

fib(11)     # => 89
fib(23)     # => 28657
```

## Settings ##

Settings are accessible through via `Preferences -> Package Settings -> Ruby Markers`. The `Settings - Default` 
option contains the defaults for all settings. When configuring settings, use the `Settings - User` option so that 
your changes will not be overwritten by updates to the plugin. The settings files use `json` syntax.

### rbenv_paths ###

Specifies a list of paths to search for the *rbenv* tool. Default setting:
```json
"rbenv_paths": [
    "~/.rbenv/bin/rbenv",
    "/usr/local/bin/rbenv"
]
```

### ruby_manager ###

Specifies which ruby version manager to use. Valid settings are: `auto`, `rbenv`, `rvm`, or `none`. Default setting:
```json
"ruby_manager": "auto"
```

### rvm_paths ###

Specifies a list of paths to search for the *rvm* tool. Default setting:
```json
"rvm_paths": [
    "~/.rvm/bin/rvm-auto-ruby",
    "/usr/local/rvm/bin/rvm-auto-ruby"
]
```

### strip_stdout ###

Set to true to strip stdout comments (`# >> `) before updating the buffer. Default setting:
```json
"strip_stdout": false
```

### xmpfilter_bin_posix ###

Specifies the location of the xmpfilter executable for Linux & OSX systems. Default setting:
```json
"xmpfilter_bin_posix": ["xmpfilter"]
```

### xmpfilter_bin_win ###

Specifies the location of the xmpfilter executable for Windows systems. Default setting:
```json
"xmpfilter_bin_win": ["xmpfilter.bat"]
```

### xmpfilter_quiet ###

Set to true to suppress standard output. Default settings:
```json
"xmpfilter_quiet": false
```

### xmpfilter_rails ###

Set to true to replace `# =>` with Test::Unit assertions instead of annotations. Default setting:
```json
"xmpfilter_rails": false,
```

### xmpfilter_warnings ###

Set to false to ignore warnings ruby warnings in annotations. Default setting:
```json
"xmpfilter_warnings": true
```

### check_for_rbenv ###

Deprecated. Use `ruby_manager` instead.

### check_for_rvm ###

Deprecated. Use `ruby_manager` instead.

### rbenv_path ###

Deprecated. Use `rbenv_paths` instead.

 [0]: http://rubyforge.org/projects/rcodetools
 [1]: http://www.ruby-lang.org
 [2]: http://rubyforge.org/projects/rubygems
 [3]: http://wbond.net/sublime_packages/package_control
