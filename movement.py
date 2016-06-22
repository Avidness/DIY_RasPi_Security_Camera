# Lib for sending commands to the Dream Cheeky Thunder missile launcher

# Manufacturer:
# http://dreamcheeky.com/thunder-missile-launcher

# Code modified from: 
# https://github.com/nbehary/Retribution

# Alan Ness
# https://github.com/Avidness

import sys
import platform
import time
import socket
import re
import json
import base64

import usb.core
import usb.util

# Protocol command bytes
DOWN    = 0x01
UP      = 0x02
LEFT    = 0x04
RIGHT   = 0x08
FIRE    = 0x10
STOP    = 0x20

DEVICE = None

def setup_usb():
    global DEVICE
    global DEVICE_TYPE

    DEVICE = usb.core.find(idVendor=0x2123, idProduct=0x1010)

    # On Linux we need to detach usb HID first
    if "Linux" == platform.system():
        try:
            DEVICE.detach_kernel_driver(0)
        except Exception:
            pass # already unregistered

    DEVICE.set_configuration()

def send_cmd(cmd):
    DEVICE.ctrl_transfer(0x21, 0x09, 0, 0, [0x02, cmd, 0x00,0x00,0x00,0x00,0x00,0x00])

def led(cmd):
    DEVICE.ctrl_transfer(0x21, 0x09, 0, 0, [0x03, cmd, 0x00,0x00,0x00,0x00,0x00,0x00])

def send_move(cmd, duration_ms):
    send_cmd(cmd)
    time.sleep(duration_ms / 1000.0)
    send_cmd(STOP)

def right(value):
	send_move(RIGHT, value)

def left(value):
	send_move(LEFT, value)

def up(value):
	send_move(UP, value)

def down(value):
	send_move(DOWN, value)

def led_toggle(onOff):
	if(onOff):
		led(0x00)
	else:
		led(0x01)

def fire():
	send_cmd(FIRE)

def init():
	setup_usb()
