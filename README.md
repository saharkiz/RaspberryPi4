# RaspberryPi4
OS: Raspberian

Used as a USB Ethernet device

edit the file called config.txt, and append the following:
dtoverlay=dwc2

edit the file called cmdline.txt. Look for rootwait, and add immediately after:
modules-load=dwc2,g_ether

Connect Via USB and 
ssh pi@raspberrypi.local

TO create a file:
touch hello.py

To edit a file:
nano hello.py

To run a file:
python hello.py
