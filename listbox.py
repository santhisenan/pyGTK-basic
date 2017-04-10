import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk

class listBoxWindow(Gtk.Window) :
    def __init__(self):
        Gtk.Window.__init__(self,title="Machine")
        self.set_border_width(10)
        listBox = Gtk.ListBox()
        listBox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listBox)

        #rows inside listboxes
        row1 = Gtk.ListBoxRow()
        box1 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing=100)
        row1.add(box1)

        #sample checkbox
        label = Gtk.Label("Sample Checkbox")
        check = Gtk.CheckButton()
        box1.pack_start(label, True, True, 0)
        box1.pack_start(check, True, True, 0)
        listBox.add(row1)

        #sample toggle switch in another row
        row2 = Gtk.ListBoxRow()
        box2 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 100)
        row2.add(box2)


        label = Gtk.Label("Sample Toggle")
        switch = Gtk.Switch()
        switch.props.valign = Gtk.Align.CENTER
        box2.pack_start(label, True, True, 0)
        box2.pack_start(switch, True, True, 0)
        listBox.add(row2)

win = listBoxWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
