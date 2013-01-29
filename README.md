# Sublime Text 2 Ruby Markers #

A Sublime Text 2 plugin to execute ruby code and update `# =>` markers with the results using the xmpfilter component of [rcodetools][0].

## Installation ##

### rcodetools ###

The rcodetools gem **must** be installed on in order for the Ruby Markers plugin to function properly. Assuming you have [ruby][1] and [rubygems][2] installed, install the rcodetools gem:

    $ gem install rcodetools

### Sublime Text 2 Ruby Markers ###

Using [Package Control][3] (recommended):

 * Use `Cmd+Shift+P` or `Ctrl+Shift+P` to open the Command Palette, then select `Package Control: Install Package`.
 * Look for `Ruby Markers` and install it.

Or, determine the `Packages` path for your OS

 * OS X: `~/Library/Application\ Support/Sublime\ Text\ 2/Packages`
 * Windows: `%APPDATA%\Sublime Text 2\Packages\`
 * Linux: `~/.config/sublime-text-2/Packages/`

and clone the plugin via git:

    $ git clone https://github.com/mmims/sublime-text-2-ruby-markers.git "<Sublime Text 2 Packages folder>/Ruby Markers"

## Usage ##

Use `Alt+Shift+u` or `Tools -> Execute and Update '# =>' Markers` to run the Ruby code through the `xmpfilter` and update the current buffer with the results.

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


 [0]: http://rubyforge.org/projects/rcodetools
 [1]: http://www.ruby-lang.org
 [2]: http://rubyforge.org/projects/rubygems
 [3]: http://wbond.net/sublime_packages/package_control
