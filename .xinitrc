# Compositor
exec picom --vsync &

# Wallpaper
feh --no-fehbg --bg-fill /home/nqtural/Pictures/astolfo_wp/astolfo_crust.png

# Keyboard layout
setxkbmap -layout se

# Monitor
xrandr --output DP-2 --mode 1920x1080 --rate 144.00

# Remove mouse acceleration
xinput set-prop "Glorious Model O Wireless" "libinput Accel Speed" -1

# Start spotifyd
spotifyd -u $(sed -n 1p $HOME/.config/i3/spotify-info) -p $(sed -n 2p $HOME/.config/i3/spotify-info)

# Dwm
exec dwm

# Dwm statusbar
dwmblocks &

# Shortcut handeling
sxhkd &

# Notification handeling
dunst &

# Disable default behaviour of power button
systemd-inhabit --what=handle-power-key sleep infinity

# Set display resolution and refresh rate
xrandr --output DP-2 --mode 1920x1080 --rate 144.00

# Disable screensaver/blackout
xset s off
xset -dpms
xset s noblank
