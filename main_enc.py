"""main_enc.py: script
This file is responsible for interfacing with ffmpeg or use PIL to produce a terminal sized
ASCII art of a picture or video
"""

from ffmpeg_interface import extract_frames_with_terminal_size
from Encoding import get_frame_as_RGB_array, convert_rgb_to_hsl, get_ascii_from_lightness
from PIL import Image
import os
import sys
import pickle
term_size = os.get_terminal_size()

#frame = get_frame_as_RGB_array(Image.open("0.jpg"))
#for y in frame:
#    print(y)

print("Extracting frames...")
extract_frames_with_terminal_size("test.mkv", "tmp")

#os.chdir("./tmp")
#frames = os.listdir()

ASCIIBrightnessLevel = " .-+*wGHM#&%"

def main():
    dir = "./tmp/"
    fname = os.listdir(dir)

    frames = list()
    
    for frame_index in range(1, len(fname) + 1): # for frame_image in fname
        print("Reading and resizing {}.bmp, out of {} files".format(frame_index, len(fname)), end="\r")
        img = Image.open(dir + "{}.bmp".format(frame_index))
        #img = img.resize((term_size.columns, term_size.lines), Image.ANTIALIAS)
        frames.append(img)
    
    print("")

    for i in range(len(frames)):
        print("Converting images to RGB array: {} out of {}".format(i + 1, len(frames)), end="\r")
        frames[i] = get_frame_as_RGB_array(frames[i])

    print("")

    # Converting every pixel to lightness
    for i, frame in enumerate(frames):
        print("Converting RGB arrays to ASCII: {} out of {}".format(i, len(frames)), end="\r")
        for y in range(len(frame)):
            for x in range(len(frame[y])):
                print("Converting frame:{}, x:{}, y:{}".format(i + 1, x, y), end="\r")
                r = frame[y][x][0]; g = frame[y][x][1]; b = frame[y][x][2]
                frame[y][x] = convert_rgb_to_hsl(r, g, b)[2]
                frame[y][x] = get_ascii_from_lightness(frame[y][x])

    print("")

    # for i, frame in enumerate(frames):
    #     input("Press enter to show the {}th frame".format(i+1))
    #     for y in range(len(frame)):
    #         for x in range(len(frame[y])):
    #             print(frame[y][x], end="")
    #         print("", end="\n")

    with open("bapple.mascii", "wb") as f:
        pickle.dump({
            "width": len(frames[0]), 
            "height": len(frames[0][0]),
            "frames": frames
            },
        f, 5)

    print("MotionASCII file saved to badapple.mascii")
    
    #sys.exit(0)

if __name__ == "__main__":
    main()
