#!/bin/bash
musicLocation="/home/pi/Desktop/Face Detection/Music/SpotifyMusic"
playlist="/home/pi/Desktop/Face Detection/purduesmartspeaker/playlist.txt"
songLocation="/home/pi/Desktop/Face Detection/purduesmartspeaker/song.txt"


omxplayer "$musicLocation/$(cat "$songLocation")"


#IFS=$'\012'
#for song in $(cat "$playlist")
#do
#    omxplayer "$musicLocation/$song"
#done