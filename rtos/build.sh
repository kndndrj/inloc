#!/bin/sh

[ -z "$1" ] && echo "please provide a port" && exit 1

set -e

# build
avr-gcc -Wall -g -Os -mmcu=atmega328p -o rtos.bin rtos.c

# convert to hex
avr-objcopy -j .text -j .data -O ihex rtos.bin rtos.hex

# upload
sudo avrdude -p atmega328p -c arduino -U flash:w:rtos.hex -P "$1"
