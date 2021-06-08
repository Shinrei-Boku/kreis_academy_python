import subprocess
#import shutil
import datetime
#import os

subprocess.run(['ls'])
subprocess.run(['ls','-al'])

now = datetime.datetime.now()
print(now)
print(now.isoformat())
print(now.strftime('%y/%m/%d_%H%M%S%f'))

# file_name = "lesson_file_08.py"
# if os.path.exists(file_name):
#     shutil.copyfile(file_name,"{}.{}".format(
#         file_name, now.strftime('%Y_%m_%d_%H_%M_%S')



#     ))