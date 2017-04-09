import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk as G

win = G.Window()

label = G.Label()
label.set_label("Game on..")
label.set_angle(30)
label.set_halign(G.Align.END)
win.add(label)

print (label.get_properties("angle"))

win.connect("delete-event",G.main_quit)
win.show_all()
G.main()