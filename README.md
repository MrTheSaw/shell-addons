# shell-addons
Tools related to extending BASH capability. Or, it seems, zsh capability.

**lsfun.py** is a python3 program used by a shell function to show shell functions with
some internal documentation. The documentation is added to functions using a line starting with ": doc ".
The rest of the line is used as a doc string. It probably ought to be short. You can have more that one
doc line. 

```bash
myFun ()
{
    : doc "This is my function"
	: doc "This is another line"
    echo Mine all mine
}
```

You'll want to install this into a binary directory in your path. I have one at the top level of my home directory i.e. $HOME/bin, which is also at the start of $PATH, in case I want to supersede some system utility, which is rare.

I use the ':' command mainly because it's prettier. It's sort of a do nothing command, save that it does do expansions, which may mean side effects might be a thing. 

The doc strings probably don't need quotes, and they won't show up in the listing, but it's a little prettier with them, IMHO.

There is a regex argument that is unused at the moment. One could add code to limit the listing if you have a lot of functions. I might in the future, but it's mostly an artifact of the skeleton I used to make such things. See the repo [CatHerd](https://github.com/MrTheSaw/CatHerd).

**bashinterfuncs** is a small collection of convenience functions for bash. They are documented internally,
and that can be nicely displayed with the program lsfunc.py. 

I use these by renaming bashinterfuncs to .bashinterfuncs (hiding it), putting it into my home directory,
and then I "source" it in my .profile.

You could also name it .zshinterfuncs, and source it in the equivalent zsh profile.

