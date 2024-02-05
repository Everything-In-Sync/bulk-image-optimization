import os
import colorama
from PIL import Image

from colorama import Fore, Back, Style


query = input()
if query == "prepare images":
        image_files = os.listdir("resize_images")
        if ".DS_Store" in image_files:
            image_files.remove(".DS_Store")
        print(image_files)
        print("\n" + "Files look good?, should I start? (y/n")
        process_answer = input()
        if process_answer == "y":
            print("New Width?" + "\n")
            image_width = input()
            image_width_int = int(image_width)
            print("New Height?" + "\n")
            image_height = input()
            image_height_int = int(image_height)
            new_size = (image_width_int, image_height_int)
            image_counter = 0
            for individual_image in image_files:
                im = Image.open(r"resize_images/" + individual_image)
                resized_image = im.resize(new_size)
                resized_image.save(
                    "resized_images/" + individual_image, quality=85, optimize=True
                )
                new_im = Image.open(r"resized_images/" + individual_image).convert(
                    "RGB"
                )
                new_im.save("resized_images_webp/" + individual_image + ".webp", "webp")
                image_counter += 1
                print(image_counter)
        else:
            print("Canceled")
if query == "optimize images":
    image_files = os.listdir("optimize_images/optimize")
    if ".DS_Store" in image_files:
        image_files.remove(".DS_Store")
    # Deletes the ds_store file every time.
    print(image_files)
    print(Fore.MAGENTA + "\n" + "Files look good?, should I start? (y/n")
    optimize_answer = input()
    if optimize_answer == "y":
        image_counter = 0
        for individual_image in image_files:
            im = Image.open(r"optimize_images/optimize/" + individual_image)
            # resized_image = im.resize(new_size)
            im.save(
                "optimize_images/optimized_images_jpg" + individual_image,
                quality=85,
                optimize=True,
            )
            new_im = Image.open(
                r"optimize_images/optimized_images_jpg/" + individual_image
            ).convert("RGB")
            new_im.save(
                "optimize_images/optimized_images_webp/"
                + individual_image
                + ".webp",
                "webp",
            )
            image_counter += 1
            print(image_counter)
    else:
        print("Canceled")