import random
import colorsys

def get_random_contrasting_color():
    while True:
        h = random.random()
        s = random.uniform(0.5, 1.0)
        l = random.uniform(0.7, 0.9)
        r, g, b = colorsys.hls_to_rgb(h, l, s)

        # Convert RGB to linear values
        def linearize(c):
            if c <= 0.03928:
                return c / 12.92
            else:
                return ((c + 0.055) / 1.055) ** 2.4

        rl, gl, bl = linearize(r), linearize(g), linearize(b)
        luminance_bg = 0.2126 * rl + 0.7152 * gl + 0.0722 * bl
        luminance_black = 0  # Luminance of black
        contrast_ratio = (luminance_bg + 0.05) / (luminance_black + 0.05)

        # Check if contrast ratio is at least 4.5:1
        if contrast_ratio >= 4.5:
            r = int(r * 255)
            g = int(g * 255)
            b = int(b * 255)
            return '#{:02X}{:02X}{:02X}'.format(r, g, b)
