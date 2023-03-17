#!/bin/bash
# Make prioritizing of player commentable
if [ 1 = 0 ]; then
    echo
# Prioritize spotifyd
#if [ "$(playerctl -p spotifyd status)" = "Playing" ]; then
#    echo "%{F#313244}|%{F-} %{F#cba6f7}%{F-} $(playerctl -p spotifyd metadata -f "{{artist}} - {{title}}")"
#elif [ "$(playerctl -p spotifyd status)" = "Paused" ]; then
#    echo "%{F#313244}|%{F-} %{F#f38ba8}%{F-} $(playerctl -p spotifyd metadata -f "{{artist}} - {{title}}")"
# Check other players
elif [ "$(playerctl status)" = "Playing" ]; then
    echo "%{F#313244}|%{F-} %{F#f38ba8}%{F-} $(playerctl metadata -f "{{artist}} - {{title}}")"
elif [ "$(playerctl status)" = "Paused" ]; then
    echo "%{F#313244}|%{F-} %{F#f38ba8}%{F-} $(playerctl metadata -f "{{artist}} - {{title}}")"
fi
