# shell-addons
Tools related to extending BASH capability.

**lsfunc.y** is a python3 program used by an eponymous shell function to show shell functions with have some internal documentation. The documentation is added to functions using a line starting with ": doc ". The rest of the line is used as a doc string. It probably ought to be short. See the *lsfunc* function in bashinterfuncs for a good way to use it.

**bashinterfuncs** is a small collection of convenience functions for bash. They are documented internally, and that can be nicely displayed with the program lsfunc.py.

I use these by renaming bashinterfuncs to .bashinterfuncs (hiding it), putting it into my home directory, and then I "source" it in my .profile.

