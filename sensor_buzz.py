import json
import time
import requests
import RPi.GPIO as GPIO
import sys


#function to sound the buzzer
def sound_buzzer(buzz_time, p):
    start_time = time.time()
    dc = 0
    while time.time() < start_time + buzz_time:
        #continually change duty cycle of buzzer to make it make sound
        if dc == 1:
            dc = 50
        else:
            dc = 1
        p.ChangeDutyCycle(dc)
        time.sleep(0.1)
    p.ChangeDutyCycle(0)
    return

#operative function to check all devices, sound buzzer if strength above given strength
def check_devs(cur_dev, max_allowable_strength, buzz_time, pulse):
    print (len(cur_dev))

    for dev in cur_dev:
        
        #extract info from json
        dev_name= str(dev["kismet.device.base.commonname"])
        dev_strength= dev['kismet.device.base.signal']['kismet.common.signal.last_signal']
        dev_type = dev["kismet.device.base.type"]

        if dev_type == "Wi-Fi Client":
            print ("\t{} is of type {}".format(dev_name, dev_type))

        #if strength of last signal is too high, sound the buzzer
        if (dev_type == "Wi-Fi Client") & (dev_strength > -max_allowable_strength):
            print ('\t\t{} with a signal of: {}'.format(dev_name, dev_strength))
            sound_buzzer(buzz_time, pulse)
            #only sound the buzzer for one device at a time
            return


#main function, continue until terminated
def main(sys_args):

    #set up buzzer
    GPIO.setmode(GPIO.BOARD)
    buzzer=15
    GPIO.setup(buzzer, GPIO.OUT)
    p= GPIO.PWM(buzzer, 1300)
    p.start(0)

    #args from cmd line
    max_str=int(sys_args[1])
    refresh_time=int(sys_args[2])

    while 1==1:

        #occur every so many seconds, based on sys arg
        time.sleep(refresh_time)
    
        #pull all devices active in the last x seconds
        r_dev = requests.get("http://root:toor@localhost:2501/devices/last-time/-{}/devices.json".format(refresh_time))
        print('JSON pulled at: {}'.format(int(time.time())))

        #turn the resulting json into python list of dicts
        cur_dev = r_dev.json()

        #call check_devs with cur_dev dict and command line argument (max allowable strength)
        check_devs(cur_dev, max_str, refresh_time, p)

if __name__ == '__main__':
    main(sys.argv)
