"""ffmpeg_interface.py: library/interface
This file is the responsible for interfacing with the ffmpeg bindings.
"""
import ffmpeg

def extract_frames_with_terminal_size(filename: str, output_directory: str) -> None:
    """extract_frames_with_terminal_size(filename: str, output_directory: str) -> None

    This function gets current console size via os.get_terminal_size(), runs ffmpeg with video filter `scale`, sets console's column and lines as width and height for the filter.
    Then outputs the frames as bmp to output_directory specified in this function's parameter.

    :param filename: Input file for `ffmpeg -i`, must be a str
    :param output_directory: Output directory for ffmpeg, must be a str
    :returns: `None`
    """
    from os import get_terminal_size
    terminal_size = get_terminal_size()
    t_width = terminal_size.columns
    t_height = terminal_size.lines
    
    print("Filename: {}, output_directory: {}, scale={}:{}".format(filename, output_directory, terminal_size.columns, terminal_size.lines))
    ffmpeg.input(filename) \
    .filter('scale', t_width, t_height) \
    .output("{}/%0d.bmp".format(output_directory)) \
    .run()
    
    # .filter(scale, param**), don't fucking pass string over there, instead of passing "120:30" to ffmpeg
    # you'll end up passing 120\\\\\\\\\\\\\\\\\\:30 to ffmpeg instead
