"""main_dec.py: program/script
This script is the player for the mascii file produced in main_end.py
"""
import colorama
import pickle
import os
import time
import ctypes
from ctypes import c_long, c_wchar_p, c_ulong, c_void_p
from pybass3 import Song
import sys

print("Loading MotionASCII file...")

mascii_raw_file = open("bapple.mascii", "rb")
MotionASCII = pickle.load(mascii_raw_file)
columns = MotionASCII["width"] # This is probably swapped with height
lines = MotionASCII["height"] # This is probably swapped with width 
frames = MotionASCII["frames"]

print("Changing terminal size: {}, {}".format(columns, lines))
print("MotionASCII loaded: {} frames".format(len(frames)))
console_resize_command = "mode con: cols={} lines={}".format(lines + 1, columns + 1) # Windows only
#print(console_resize_command)
#time.sleep(5)
os.system(console_resize_command)
#print(console_resize_command)
print("Console resized")
#sys.exit(1)

current_frame = -1
def print_next_frame():
    global current_frame
    current_frame += 1
    frame = frames[current_frame]
    for y in range(len(frame)):
        for x in range(len(frame[y])):
            print(frame[y][x], end="")
        print("", end="\n")

gHandle = ctypes.windll.kernel32.GetStdHandle(c_long(-11))
def move(y, x):
    value = x + (y << 16)
    ctypes.windll.kernel32.SetConsoleCursorPosition(gHandle, c_ulong(value))

# current_t = time.perf_counter_ns()
# while True:
#     current_t = time.perf_counter_ns()
#     mod = current_t % 1000000000
#     if current_t % 100000000 == 0:
#         print("1 Second passed")
#     else: print(current_t, "% 1000000000 =", mod, end="\r")

song = Song("audio.wav")
song.play()
position_bytes = song.position_bytes
s_duration = song.duration
frame_count = len(frames)
len_bytes = song.duration_bytes
while position_bytes < len_bytes:
    current_audio_position_percentage = song.position / s_duration
    frame_index = int(current_audio_position_percentage * frame_count)
    move(0, 0)
    print("Playing frame {}".format(frame_index), end="\r")
    if frame_index > len(frames) - 1:
        break
    frame = frames[frame_index]
    for y in range(len(frame)):
        for x in range(len(frame[y])):
            print(frame[y][x], end="")
        print("", end="\n")

song.free_stream()
del song
sys.exit(0)
