import dbus
import dbus.mainloop.glib 
from gi.repository import GLib

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SystemBus()


def call_added(path, properties):
	print(f"Incoming call from: {properties.get('LineIdentification', 'Unknown')}")
	print(f"Call state: {properties.get('State', 'Unknown')}")
	
bus.add_signal_receiver(
	call_added,
	signal_name="CallAdded",
	dbus_interface="org.ofono.VoiceCallManager",
	bus_name="org.ofono"
)

print("monitoring for incoming calls..")
GLib.MainLoop().run()



#/home/dom/Desktop/user_interface/call-monitor.py
