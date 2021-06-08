import os
import pathlib
import shutil

print(os.path.exists('lesson_file_07.py'))
print(os.path.isfile('lesson_file_07.py'))
print(os.path.isdir('file'))

#os.rename(XXXXX,XXXXX)
os.mkdir('test_dir')
#os.rmdir('test_dir')

shutil.copy('lesson_file_07.py',
            "cp_lesson_file_07.py")
#os.remove('cp_lesson_file_07.py')

os.getcwd()