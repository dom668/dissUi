import dbus
import dbus.mainloop.glib
from gi.repository import GLib
import subprocess

AUDIO_FILE = "/home/dom/Desktop/user_interface/RUNNIN FROM DA POLICE.mp3"

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
bus = dbus.SystemBus()

ringtone_process = None

def call_added(path, properties):
    global ringtone_process
    state = properties.get('State', '')
    caller = properties.get('LineIdentification', 'Unknown')
    
    if state == 'incoming':
        print(f"Incoming call from: {caller}")
        ringtone_process = subprocess.Popen(['pw-play', AUDIO_FILE])
        
        # monitor the call for state changes
        bus.add_signal_receiver(
            call_state_changed,
            signal_name="PropertyChanged",
            dbus_interface="org.ofono.VoiceCall",
            path=path)
            
def call_state_changed(name, value):
    global ringtone_process
    if name == "State":
        state = str(value)
        print(f"Call state changed to: {state}")
        if state in('active', 'disconnected', 'alerting'):
            stop_ringtone()

def stop_ringtone():
    global ringtone_process
    if ringtone_process and ringtone_process.poll() is None:
        ringtone_process.terminate()
        ringtone_process = None
        print("Ringtone stopped")

bus.add_signal_receiver(
    call_added,
    signal_name="CallAdded",
    dbus_interface="org.ofono.VoiceCallManager",
    bus_name="org.ofono")

print("Monitoring for incoming calls...")
GLib.MainLoop().run()



#python3 /home/dom/Desktop/user_interface/call-monitor.py - to run
