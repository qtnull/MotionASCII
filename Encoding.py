from PIL import Image

def get_frame_as_RGB_array(ImageObject: Image.Image) -> tuple:
    """Reads a image, and turns them into an (r, g, b) array

    :param ImageObject: An opened `Image.Image` object
    :returns: a 2-dimensional `tuple`
    """
    frame = []
    for y in range(ImageObject.height):
        row = []
        for x in range(ImageObject.width):
            row.append(ImageObject.getpixel((x, y)))
        frame.append(row)

    return frame
        
def convert_rgb_to_hsl(r: int, g: int, b: int) -> tuple:
    """Converts a color specified in RGB to the HSL model
    
    :param r: RGB red value, 0-255
    :param g: RGB green value, 0-255
    :param b: RGB blue value, 0-255
    :returns: `tuple`
    """
    # https://zh.wikipedia.org/wiki/HSL%E5%92%8CHSV%E8%89%B2%E5%BD%A9%E7%A9%BA%E9%97%B4#%E4%BB%8EHSV%E5%88%B0RGB%E7%9A%84%E8%BD%AC%E6%8D%A2
    # I'm lazy, so I'm stealing the formula from here

    # # Converting RGB values in range [0, 1]
    r /= 255
    g /= 255
    b /= 255
    # These are some parameter which the conversion formula needs
    Cmax = max(r, g, b)
    Cmin = min(r, g, b)
    delta = Cmax - Cmin

    hue = -1; saturation = -1; lightness = -1

    # Hue
    if delta == 0:
        hue = 0
    elif Cmax == r:
        hue = 60 * ( ((g - b) / delta) % 6 )
    elif Cmax == g:
        hue = 60 * ( ((b - r) / delta) + 2 )
    elif Cmax == b:
        hue = 60 * ( ((r - g) / delta) + 4 )

    # Lightness
    lightness = (Cmin + Cmax) / 2
    
    # Saturation
    if delta == 0:
        saturation = 0
    else:
        saturation = delta / ( 1 - abs(2 * lightness - 1) )

    return (hue, saturation, lightness)

def get_ascii_from_lightness(lightness: float) -> str:
    """Returns a ASCII character for a specific lightness

    :param lightness: 0.0-1.0, lightness from the HSL color model
    :returns: str (single character)
    """

    lightnessASCII = " .-+*wGHM#&%"

    brightness_index = int(lightness * len(lightnessASCII))
    if brightness_index < 0:
        brightness_index = 0
    elif brightness_index >= len(lightnessASCII):
        brightness_index = len(lightnessASCII) - 1

    return lightnessASCII[brightness_index]
