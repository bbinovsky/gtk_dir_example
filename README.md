gtk_dir_example
===============

pyGTK Directory Example

What is it?

This is purely an example of pyGTK TreeView with a scrollable list.
It's a list of the files on /usr/bin/ available on most *nix systems.
The list can be drag & drop reordered.
The list of files can be sorted into alphabetical order by clicking the 1st column header.

What does it show?

Shows object-oriented programming.
Shows a basic understading of the GTK GUI library.
Shows event handling in GTK using Python.

Shortcomings?

Doesn't have much in the way of file system error handling right now.

What does it need?

Written in Python 2.6.6 with pyGTK installed.  pyGTK depends on gtk2 and gtk2_devel.
Does not use range, dict, map, filter zip so that should be fine for Python 3.0.
Might call print not as a function in one or 2 places so that might need to be changed.
Please be aware that in Python 3.1+ and up pyGTK is effectively replaced by pyGI (Instrospection).
Try pygtkcompat and if that fails port to pyGI but you will need gtk3 for that.

