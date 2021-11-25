# MotionASCII

MotionASCII is a type of "video" that plays in your console or terminal. Inspired by the Music Video "Bad Apple!!" and CmdPlay.

## Encoding

The encoding part of any video to MotionASCII, is to first convert the video into frames, and crush the resolution to the terminal's width and height.

Normally, to ensure "quality", as you run the program, the program will first take the video, encode it, and plays it, this approach has some problems:
- Everytime you run the program, you have to wait for the conversion
- If you have a different terminal window width and height, you have to convert it again
- If you change the width/height, the program will not work anymore

This program will make no attempts at fixing above listed problem, but just FYI: known bugs.

## Technical details

The encoding part is carried out by ffmpeg, by converting the video into frames/pictures at a desired resolution (in this case, the user's terminal width and height).

The program then reads all of the images produced by ffmpeg, and reads the luminosity of every pixel of every image, every image's "frame" will probably stored as an array.

Then, the program can optionally just do playback, or it can save the resulting MotionASCII video to disk (either compressed or uncompressed, I'll probably go with gz or LZMA if I needed compression).

## Playback

The playback should be simple, we'll map the audio timeline to the video frames linearly. Then we'll play it back based on the audio's current position.

## Future: color support?

In regards of the color support... Although I don't think it's too complicated to implement, but the terminal is just limited to 16 colors, you may alter the shades to get more "colours", but at current stage, I'm not planning to add any colors.

## FAQ

### Just... Why?

Why not?