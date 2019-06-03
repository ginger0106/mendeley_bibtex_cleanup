# import sys 
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i',type=str)
# parser.add_argument('-o',type=str)
args = parser.parse_args()

dir_path = args.i
new_path = dir_path+'/fixed/'
os.system(f'mkdir {new_path }')
files= os.listdir(dir_path)
for file_name in files:
    if file_name.endswith('bib'):
        print(file_name)
        file_path = os.path.join(dir_path,file_name)
        os.system(f'python3 clean_library.py -i "{file_path}" -o "{new_path}/{file_name[:-4]}_fixed.bib"')




