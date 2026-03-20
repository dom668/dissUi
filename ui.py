### stuff to make it work fr
# import subprocess
# subprocess.run(["/usr/share/ofono/scripts/dial-number", "+447305874435"]) - this places a call when run on the pi :)



# command to place call - /usr/share/ofono/scripts/dial-number +447305874435
# command to end call - /usr/share/ofono/scripts/hangup-active
# command to recive call - /usr/share/ofono/scripts/answer-calls

import dbus
import time
import subprocess
import keyboard

bus = dbus.SystemBus()

manager = dbus.Interface(
	bus.get_object('org.ofono', '/'),
	'org.ofono.Manager')

modems = manager.GetModems()
modem_path = modems[0][0]

vcm = dbus.Interface(
	bus.get_object('org.ofono', modem_path),
	'org.ofono.VoiceCallManager')

current_number = ""

while True:
	try:
		calls = vcm.GetCalls()
		if calls:
			for path, properties in calls:
				state = str(properties.get('State', 'unknown'))
		else:
			state = "none"
			
			
		if (state == "none"):
			print("state none")
				
			if keyboard.is_pressed('1'):
				time.sleep(0.2)
				current_number = current_number + "1"
			if keyboard.is_pressed('2'):
				time.sleep(0.2)
				current_number = current_number + "2"
			if keyboard.is_pressed('3'):
				time.sleep(0.2)
				current_number = current_number + "3"
			if keyboard.is_pressed('4'):
				time.sleep(0.2)
				current_number = current_number + "4"
			if keyboard.is_pressed('5'):
				time.sleep(0.2)
				current_number = current_number + "5"
			if keyboard.is_pressed('6'):
				time.sleep(0.2)
				current_number = current_number + "6"
			if keyboard.is_pressed('7'):
				time.sleep(0.2)
				current_number = current_number + "7"
			if keyboard.is_pressed('8'):
				time.sleep(0.2)
				current_number = current_number + "8"
			if keyboard.is_pressed('9'):
				time.sleep(0.2)
				current_number = current_number + "9"
			if keyboard.is_pressed('0'):
				time.sleep(0.2)
				current_number = current_number + "0"
				
			if keyboard.is_pressed('enter'):
				subprocess.run(["/usr/share/ofono/scripts/dial-number", current_number])
				current_number = ""
				
			
			print(current_number)
				
				
		if (state == "alerting"):
			print("state alerting")
		
		if (state == "incoming"):
			print("state incoming")
			if keyboard.is_pressed('enter'):
				subprocess.run("/usr/share/ofono/scripts/answer-calls")
			if keyboard.is_pressed('.'):
				subprocess.run("/usr/share/ofono/scripts/reject-calls")
			
		if (state == "active"):
			print("state active")
			if keyboard.is_pressed('.'):
				subprocess.run("/usr/share/ofono/scripts/hangup-active")
			
			
			
	except dbus.DBusException as e:
		print(f"DBus error: {e}")

time.sleep(1)






#sudo python3 /home/dom/Desktop/user_interface/ui.py - to run
