#!/bin/bash
# tint2 &
feh --bg-scale /home/samarth/Pictures/wallpapers/pen.jpeg &
amixer sset Master 100% &
picom --config /home/samarth/.config/picom/picom.conf --experimental-backends &

