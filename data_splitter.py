import image_processing
import glob
import os
# THIS SCRIPT ASSUMES THAT IMAGE_PROCESSING.PY SCRIPT has finished processing/cleaning the images first before using this script.
# Example of usage is:
# data_splitter.distribute_data(from_path, to_path, 0.2, 0.2, "tennisball")


def count_image_files(path):
    print("count_image_files path: ", path)
    counter = 0
    for file in glob.glob(path + "/*.jpg"):
        counter += 1
    return counter


def prepare_directories_only(path, dirs_names, class_dir_names):
    for dir_name in dirs_names:
        if (os.path.exists(path + dir_name) == False):
            os.makedirs(path + dir_name)
            for class_dir_name in class_dir_names:
                os.makedirs(path + dir_name + "/"+class_dir_name)
        else:
            print(dir_name, "already exists @ ", path)
            print(
                "==>Please manually remove any preexisting directories that you named here.")


def distribute_data(from_path, to_path, val_split, test_split, class_dir_name):
    total = count_image_files(from_path)
    print("Total images available: ", total)

    val_percentage = round(total * val_split)
    print("Validation split count is: ", val_percentage)

    test_percentage = round(total * test_split)
    print("Testing split count is: ", test_percentage)

    count = 0

    for file in glob.glob(from_path + "/*.jpg"):
        # Validtaion images
        if count < val_percentage:
            image_processing.relocateImages(
                to_path + "Validtaion" + "/", file, class_dir_name, copy=False)
            count += 1

    count = 0
    for file in glob.glob(from_path + "/*.jpg"):
        # Testing images
        if count < val_percentage:
            image_processing.relocateImages(
                to_path + "Testing" + "/", file, class_dir_name, copy=False)
            count += 1
    for file in glob.glob(from_path + "/*.jpg"):
        # Training images
        image_processing.relocateImages(
            to_path + "Training" + "/", file, class_dir_name, copy=False)
        count += 1
