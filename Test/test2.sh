#!/bin/bash

clear

echo " _____ ______   ________  ___       ________  _________  ________  ________" 
echo "|\   _ \  _   \|\   __  \|\  \     |\   ____\|\___   ___|\   __  \|\   __   \ "    
echo "\ \  \|\__\ \  \ \  \|\  \ \  \    \ \  \___|\|___ \  \_\ \  \|\  \ \  \|\   \ "  
echo " \ \  \||__| \  \ \   __  \ \  \    \ \_____  \   \ \  \ \ \  \|\  \ \   ___ / " 
echo "  \ \  \    \ \  \ \  \ \  \ \  \____\|____|\  \   \ \  \ \ \  \|\  \ \  \ \  \ "
echo "   \ \__\    \ \__\ \__\ \__\ \_______\____\_\  \   \ \__\ \ \_______\ \__\ \  \ "
echo "    \|__|     \|__|\|__|\|__|\|_______|\_________\   \|__|  \|_______|\|__|  \__\ "
echo "                                      \|_________|                              "
                                                                                
                                                                                

echo "\n\t\t\t\tWelcome to MalStor\n\n\n\n"

cd \/home\/wildcat\/Lockheed\/laikaboss

ls

.\/laika.py 0.exe | jq '.scan_result[]' > demo\/out.txt








