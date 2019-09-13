import imagehash
from PIL import Image
import numpy as np
import os
import shutil
import matplotlib.pyplot as plt
import glob
import imghdr
import pathlib


def showImage(title, imagefile):
    """ Basic image show method

    Arguments:
        title {string} -- name above the image file
        imagefile {numpy.ndarray} -- [the image to be shown]
    """
    plt.figure(figsize=(16, 16))
    plt.title(title)
    plt.imshow(imagefile)
    plt.show()


def convertPNGToJPG_Save(path, filename, relocate=False, relocateDirName="WrongFormatImages"):
    """ Converts a PNG image to JPG file

    Arguments:
        filename {string} -- full path to image(string) including its name and extension

    Keyword Arguments:
        imageFormat {str} -- image original format (default: {"png"})
        relocate {bool} -- [if isolating/moving original image is desired] (default: {False})
        relocateDirName {str} -- [relcation directory name] (default: {"WrongFormatImages"})
    """

    img = Image.open(filename)

    rgb_img = img.convert('RGB')

    rgb_img.save(filename.replace(pathlib.PurePosixPath(
        filename).suffix, ".jpg"), quality=100)
    if(relocate):
        relocateImages(path, filename, relocateDirName)


def processSimilarImages(path):
    """ Finds and isolate similar images

    Arguments:
        path {string} -- path to root directory of images
    """
    hash_keys = dict()
    for idx, filename in enumerate(path('.')):
        if(os.path.isfile(filename)):
            image_hash = imagehash.average_hash(Image.open(filename))
            if image_hash in hash_keys:
                # Remove the image to another place
                relocateImages(filename)
            else:
                hash_keys[image_hash] = idx


def relocateImages(path, file, relocateDirName="DuplicateImages", copy=False):
    """ relocate files to a certain destination

    Arguments:
        filename {string} -- file name with its extension

    Keyword Arguments:
        relocateDirName {string} -- name of the dir (default: {"DuplicateImages"})
    """

    fullpath = path + relocateDirName

    if not os.path.exists(fullpath):
        os.makedirs(fullpath)
    if copy == True:
        shutil.copy(file, fullpath)
    else:
        shutil.move(file, fullpath)


def is_Image(filename):

"""[check if a file is an image that ends with a certain format]

Arguments:
    filename {[string]} -- file name with full path

Returns:
    [Boolean] -- Either True or False
"""
 f = filename.lower()

  return f.endswith(".png") or f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".bmp") or f.endswith(".gif") or '.jpg' in f


def check_images(path):

"""Verify image type and convert it if it is not a jpeg

Arguments:
    path {string} -- full path to a directory of images
"""
 images_dict = {}
  for file in glob.glob(path + "/*.*"):
        if(is_Image(file)):
            if(imghdr.what(file) != "jpeg" or file.endswith(".jpeg")):
                conv_imag = convertPNGToJPG_Save(path, file, relocate=True)


def process_images(path):

"""relocate only the duplicate images

Arguments:
    path {string} -- [full path to the directory]
"""
 check_images(path)

  images_dict = {}

   for file in glob.glob(path + "/*.*"):
        if(is_Image(file)):

            hash = imagehash.whash(Image.open(file))

            if hash in images_dict:
                relocateImages(path, file)
                print(file, " is a duplicate",
                      "to retrieve use the hash: ", hash)
            else:
                images_dict[hash] = file

    for k, v in images_dict.items():
        print(k, v)
