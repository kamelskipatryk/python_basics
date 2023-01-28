# 'C:\Users\W00lfie\Desktop\zdj'
import os
from PIL import Image
from pathlib import Path

# assign directory where images are
path_to_directory = r'C:\Users\W00lfie\Desktop\zdj'


# create a new folder for resize images
dir_copy = 'resize_images'
resize_image_directory_path = os.path.join(path_to_directory, dir_copy)
os.mkdir(resize_image_directory_path)
os.chdir(resize_image_directory_path)

# files(images) in directory
images = Path(path_to_directory).glob('*')

# iterate over files in that directory

for image in images:
    try:
        # get file name
        image_name = os.path.basename(image)
        
        # rotate, change size of image and overwrite it
        im = Image.open(image)
        new_rotate = im.rotate(90, expand=True)
        new_image = new_rotate.resize((1000,1500))
        new_image.save(image_name)

        print(image_name)
    except:
        pass

print('done')


