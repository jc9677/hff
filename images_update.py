import os
import requests

txt = "f-list.txt"

with open(txt, "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]
    print(lines)

    for line in lines:
        # Each line is a url for an image. If the image is already in the images folder, skip it. Otherwise, download it to the images folder.


        images_folder = "images"
        if not os.path.exists(images_folder):
            os.makedirs(images_folder)

        image_name = os.path.basename(line)
        image_path = os.path.join(images_folder, image_name)

        if os.path.exists(image_path):
            print(f"Skipping {image_name}, already exists.")
            continue

        response = requests.get(line)
        if response.status_code == 200:
            with open(image_path, "wb") as f:
                f.write(response.content)
            print(f"Downloaded {image_name}.")
        else:
            print(f"Failed to download {image_name}.")