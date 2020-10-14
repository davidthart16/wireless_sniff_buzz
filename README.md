# Open-Source PED Sniffer

## Hardware configuration:
* Raspberry Pi 3+ B or Raspberry Pi 4 (https://www.canakit.com/raspberry-pi-3-model-b-plus-starter-kit.html) $79.95 (includes Micro SD card)
* Small Enclosed Piezo w/Wires (https://www.adafruit.com/product/1740?gclid=CjwKCAjww5r8BRB6EiwArcckCznO0Vd0faIIqkvg2dH4-otmC92uMyFkqVvJIL3sg9MsG__lC8wrKhoCIWgQAvD_BwE) $0.95
  
## Software configuration:
* Kali Linux with Nexmon pre-patched (https://images.kali.org/arm-images/kali-linux-2020.3a-rpi3-nexmon.img.xz) includes Kismet pre-installed
* Python 3 (includes GPIO library, Requests library)
  
## Steps to set-up device:
1. Download Kali Linux, extract, and write to Micro SD card
1. Install Micro SD card into RPi
1. Plug in monitor, keyboard, and mouse for initial set-up
  
## Steps to run:
1. Turn on RPi
1. Log in to Kali (user:kali, pass:kali)
1. Run Kismet with wi-fi and bluetooth as sources ( sudo kismet -c wlan0 hci0)
1. In another terminal, run sensor_buzz (python3 sensor_buzz.py x 10) (experiment to see the correct signal strength to put for x, lower is higher signal)
1. Set up bash command to run on boot that will start kismet and sensor_buzz, to run device headless
