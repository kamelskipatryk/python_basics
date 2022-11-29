import glob
import os

os.chdir('g:\\')

files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))

