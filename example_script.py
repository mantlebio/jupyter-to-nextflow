#!/usr/bin/env python3

"""
Script to preprocess all the images in a given input directory
and save to the given output directory.

Usage:
./example_script.py <input_dir> -o <output_dir>
"""

import argparse
import os
import glob
import tqdm
import numpy as np
import skimage
import cv2

def preprocess(img_path: str) -> np.array:
    """
    Reads in, normalizes, and thresholds a single image.
    Returns np.array of preprocessed image.
    """

    # Read in
    img = skimage.io.imread(img_path)

    # Normalize
    norm = np.zeros_like(img)
    cv2.normalize(img, norm, 0, 255, cv2.NORM_MINMAX)

    # Threshold
    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

    return thresh

def main():

    # Instatiate argument parser
    parser = argparse.ArgumentParser(
        prog='preprocess_images',
        description="Loads images and preprocesses by normalizing and thresholding."
    )
    # Add arguments to the argument parser
    parser.add_argument(
        'input_dir',
        type=str,
        help="Directory containing input images."
    )
    parser.add_argument(
        '-o',
        '--output_dir',
        dest='output_dir',
        type=str,
        help="Directory to which to save outputs."
    )
    # Run argument parser and extract data
    args = parser.parse_args()

    all_image_paths = glob.glob(os.path.join(args.input_dir, "*.tif"))

    # Make sure output directory exists
    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)

    # Preprocess all the images in the input directory
    # and write out to the output directory
    for path in all_image_paths:

        # Apply preprocessing
        processed_img = preprocess(path)

        # Save
        basename = os.path.basename(path)
        extension_idx = basename.rfind(".")
        fname = os.path.join(args.output_dir, f"{basename[:extension_idx]}_preprocessed.tif")
        skimage.io.imsave(fname, processed_img, check_contrast=False)

if __name__ == "__main__":
    main()