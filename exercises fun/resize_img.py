# 'C:\Users\W00lfie\Desktop\zdj'
import os
from PIL import Image
from pathlib import Path

# change currect working directory
cwd = os.getcwd()
print(cwd)
new_cwd_object = os.chdir(r'C:\Users\W00lfie\Desktop\zdj')
new_cwd = os.getcwd()
print(new_cwd)

# assign directory
directory = r'C:\Users\W00lfie\Desktop\zdj'

# files(images) in directory
images = Path(directory).glob('*')

# iterate over files in that directory
for image in images:
    # get file name
    file_name = os.path.basename(image)
    
    # change size of image and overwrite it
    im = Image.open(image)
    new_image = im.resize((1000,1500))
    new_image.save(file_name)

    print(file_name)
    


