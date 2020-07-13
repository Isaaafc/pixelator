import matplotlib.pyplot as plt
import numpy as np
import imageio
import argparse
from PIL import Image

def convert_color(img, greyscale, levels):
    """
    Convert colors into n_colors scales
    """
    _img = img[:, :, 0] if greyscale else img
    return np.digitize(_img, np.linspace(0, _img.max() + 1, levels)).astype('i')

def pixelate(img, res):
    pixel_size = img.size[0] // res

    img = img.resize(
        (img.size[0] // pixel_size, img.size[1] // pixel_size),
        Image.NEAREST
    )
    img = img.resize(
        (img.size[0] * pixel_size, img.size[1] * pixel_size),
        Image.NEAREST
    )

    return img

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_path', '-i')
    parser.add_argument('--out_path', '-o')
    parser.add_argument('--res', '-r', type=int)
    parser.add_argument('--greyscale', '-g', required=False, action='store_true')
    parser.add_argument('--levels', '-l', required=False, type=int)

    args = parser.parse_args()

    img = Image.open(args.img_path)
    img = pixelate(img, res=args.res)

    img = np.array(img)

    if args.levels:
        img = convert_color(img, args.greyscale, args.levels)

    imageio.imwrite(args.out_path, img)