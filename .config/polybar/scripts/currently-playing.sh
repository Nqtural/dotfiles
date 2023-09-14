#!/usr/bin/fish
# MOC is currently playing
if [ "$(mocp -i | awk '/^State/{print $2}')" = "PLAY" ];
    set response "%{F#313244}|%{F-} %{F#74c7ec}%{F-} $(mocp -i | awk '/^Title/{first = $2; $1=""; $2=""; print $0}' | sed "s/^ *//g")"
# PulseAudio is currently playing
else if [ "$(playerctl status)" = "Playing" ];
    set response "%{F#313244}|%{F-} %{F#74c7ec}%{F-} $(playerctl metadata -f "{{artist}} - {{title}}")"
# MOC is paused
else if [ "$(mocp -i | awk '/^State/{print $2}')" = "PAUSE" ];
    set response "%{F#313244}|%{F-} %{F#fab387}%{F-} $(mocp -i | awk '/^Title/{first = $2; $1=""; $2=""; print $0}' | sed "s/^ *//g")"
# PulseAudio is paused
else if [ "$(playerctl status)" = "Paused" ];
    set response "%{F#313244}|%{F-} %{F#fab387}%{F-} $(playerctl metadata -f "{{artist}} - {{title}}")"
end

if [ (test -n "$response"; echo "$status") = 1 ];
    echo "%{F#313244}|%{F-} %{F#74c7ec}%{F-} Nothing playing"
end

if [ (string length "$response") -ge 77 ];
    echo "$(string sub -l 73 "$response")..."
else
    echo "$response"
end
