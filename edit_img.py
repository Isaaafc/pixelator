import imageio
import numpy as np
import argparse
import copy

def swap_top(img, proportion=0.5):
    shape = img.shape

    new_img = np.zeros(shape)
    thres = int(img.shape[0] * proportion)

    new_img[thres:, :, :] = copy.deepcopy(img[:-thres, :, :])
    new_img[:-thres, :, :] = copy.deepcopy(img[thres:, :, :])

    return new_img

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--img_path', '-i')
    parser.add_argument('--out_path', '-o')
    parser.add_argument('--proportion', '-p', type=float)

    args = parser.parse_args()

    img = imageio.imread(args.img_path)
    img = swap_top(img, proportion=args.proportion)
    
    imageio.imwrite(args.out_path, img)