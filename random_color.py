import random
import colorsys

def get_random_contrasting_color():
    while True:
        # Generate random hue and saturation for color variety
        h = random.random()
        s = random.uniform(0.5, 0.8)
        # Set lightness to a low value for dark colors
        l = random.uniform(0.2, 0.3)
        # Convert HLS to RGB
        r, g, b = colorsys.hls_to_rgb(h, l, s)

        # Convert RGB to linear values for luminance calculation
        def linearize(c):
            if c <= 0.03928:
                return c / 12.92
            else:
                return ((c + 0.055) / 1.055) ** 2.4

        rl, gl, bl = linearize(r), linearize(g), linearize(b)
        # Calculate luminance of the background color
        luminance_bg = 0.2126 * rl + 0.7152 * gl + 0.0722 * bl
        luminance_white = 1.0  # Luminance of white
        # Calculate contrast ratio between white text and background
        contrast_ratio = (luminance_white + 0.05) / (luminance_bg + 0.05)

        # Ensure contrast ratio is at least 4.5:1 for accessibility
        if contrast_ratio >= 4.5:
            # Scale RGB values to 0-255 and format as hex color code
            r_int = int(r * 255)
            g_int = int(g * 255)
            b_int = int(b * 255)
            return '#{:02X}{:02X}{:02X}'.format(r_int, g_int, b_int)