import os
from datetime import datetime

print('test')

time_modify = os.path.getmtime(__file__)

print(datetime.utcfromtimestamp(time_modify).strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.utcfromtimestamp(os.path.getctime(__file__)).strftime('%Y-%m-%d %H:%M:%S'))

t = datetime.now().time()
print(t)

import time

print("Last modified: %s" % time.ctime(os.path.getmtime(__file__)))
print("Created: %s" % time.ctime(os.path.getctime(__file__)))
