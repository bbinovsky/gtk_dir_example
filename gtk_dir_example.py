#!/usr/bin/env python

import pygtk
import gtk
import os

class DirectoryExample(object):

    def delete_event(self, widget, event, data=None):
        gtk.main_quit()
        print "Exit"
        return False

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Directory Operations")
        self.window.set_default_size(200, 400)
        self.window.set_position(gtk.WIN_POS_CENTER)

        self.window.connect("delete_event", self.delete_event)

        self.liststore = gtk.ListStore(str, str, 'gboolean')
        self.treeview = gtk.TreeView(self.liststore)

        self.tvcolumn = gtk.TreeViewColumn('Filename')
        self.tvcolumn1 = gtk.TreeViewColumn('Access')

        path = "/usr/bin/"
        for file_name in os.listdir(path):
            file_access = 0
            if (os.access(path + file_name, os.R_OK)):
                file_access += 4
            if (os.access(path + file_name, os.W_OK)):
                file_access += 2
            if (os.access(path + file_name, os.X_OK)):
                file_access += 1
            self.liststore.append([file_name, file_access, False])

        self.treeview.append_column(self.tvcolumn)
        self.treeview.append_column(self.tvcolumn1)

        self.cell = gtk.CellRendererText()
        self.cell1 = gtk.CellRendererText()

        self.cell.set_property('cell-background', 'cyan')
        self.cell1.set_property('cell-background', 'pink')

        self.tvcolumn.pack_start(self.cell, True)
        self.tvcolumn1.pack_start(self.cell1, True)

        self.tvcolumn.set_attributes(self.cell, text=0)
        self.tvcolumn1.set_attributes(self.cell1, text=1,
                                      cell_background_set=2)

        self.treeview.set_search_column(0)
        self.tvcolumn.set_sort_column_id(0)
        self.treeview.set_reorderable(True)

        self.scrolltree = gtk.ScrolledWindow()
        self.scrolltree.set_policy(gtk.POLICY_NEVER, gtk.POLICY_AUTOMATIC)
        self.scrolltree.add(self.treeview)

        self.window.add(self.scrolltree)

        self.window.show_all()

    def main(self):
        gtk.main()

if __name__=="__main__":
    test = DirectoryExample()
    test.main()
