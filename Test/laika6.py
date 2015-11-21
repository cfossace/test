#!/usr/bin/python
import sys
import platform
from subprocess import Popen

messages = 'This is Console1', 'This is Console2'

new_window_command = "x-terminal-emulator -e".split()

# open new consoles, display messages
echo = [sys.executable, "-c",
        "import sys; print(sys.argv[1]); input('Press Enter..')"]
processes = [Popen(new_window_command + echo + [msg])  for msg in messages]

# wait for the windows to be closed
for proc in processes:
    proc.wait()
