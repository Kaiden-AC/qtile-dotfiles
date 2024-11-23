#!/bin/bash

chosen=$(echo -e " Poweroff\n Restart\n Lock\n Logout" | rofi -dmenu -i -theme ~/.config/rofi/black_blue.rasi -p "System")

case "$chosen" in
    " Poweroff") poweroff ;;
    " Restart") reboot ;;
    " Lock") i3lock ;;
    " Logout") pkill -KILL -u $USER ;;
    *) exit 1 ;;
esac
