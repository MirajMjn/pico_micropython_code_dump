from time import sleep
#from LM393Tachometer import Tachometer
from LM393Tachometer_PIO import Tachometer

# initializing tachometer objects and their GPIO pins

tch = Tachometer(17)

try:
    while True:
        rpm_reading = tch.get_rpm()
        print(rpm_reading)
        sleep(1)
except KeyboardInterrupt:
    print("Stopping...")

finally:
    tch.stop()
    print("Code Terminated")

