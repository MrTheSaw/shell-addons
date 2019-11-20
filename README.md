# shell-addons
Tools related to extending BASH capability. Or, it seems, zsh capability.

**lsfun.py** is a python3 program used by a shell function to show shell functions with have
some internal documentation. The documentation is added to functions using a line starting with ": doc ".
The rest of the line is used as a doc string. It probably ought to be short. You can have more that one
doc line, but the formatting isn't too pretty, yet. See the *lsfunc* function
in bashinterfuncs for a good way to use it. You'll want to install this into a binary directory in your path.
I have one at the top level of my home directory i.e. $HOME/bin, which is also at the start of $PATH, in case
I want to supersede some system utility, which is rare.

**bashinterfuncs** is a small collection of convenience functions for bash. They are documented internally,
and that can be nicely displayed with the program lsfunc.py. 

I use these by renaming bashinterfuncs to .bashinterfuncs (hiding it), putting it into my home directory,
and then I "source" it in my .profile.

You could also name it .zshinterfuncs, and source it in the equivalent zsh profile.

