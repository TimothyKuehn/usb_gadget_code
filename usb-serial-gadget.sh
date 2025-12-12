#!/bin/bash
set -e

G=/sys/kernel/config/usb_gadget/serialg

if [ -d "$G" ]; then
  echo "" > "$G/UDC" 2>/dev/null || true
  rm -rf "$G"
fi

mkdir -p "$G"
cd "$G"

echo 0x1d6b > idVendor
echo 0x0104 > idProduct
echo 0x0200 > bcdUSB

mkdir -p strings/0x409
echo "123456" > strings/0x409/serialnumber
echo "Raspberry Pi" > strings/0x409/manufacturer
echo "Pi USB Serial" > strings/0x409/product

mkdir -p configs/c.1/strings/0x409
echo "Config 1" > configs/c.1/strings/0x409/configuration
echo 250 > configs/c.1/MaxPower

mkdir -p functions/acm.usb0
ln -s functions/acm.usb0 configs/c.1/

UDC="$(ls /sys/class/udc | head -n 1)"
echo "$UDC" > UDC
