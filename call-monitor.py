import dbus
import dbus.mainloop.glib
from gi.repository import GLib
import subprocess

AUDIO_FILE = "/home/dom/alert.wav"

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SystemBus()

def call_added(path, properties):
    state = properties.get('State', '')
    caller = properties.get('LineIdentification', 'Unknown')
    
    if state == 'incoming':
        print(f"Incoming call from: {caller}")
        subprocess.Popen(['pw-play', AUDIO_FILE])

bus.add_signal_receiver(
    call_added,
    signal_name="CallAdded",
    dbus_interface="org.ofono.VoiceCallManager",
    bus_name="org.ofono"
)

print("Monitoring for incoming calls...")
GLib.MainLoop().run()



#/home/dom/Desktop/user_interface/call-monitor.py
