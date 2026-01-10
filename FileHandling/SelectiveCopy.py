import shutil
import os
import re

#SELECTIVE COPY 
#Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or .jpg). 
#Copy these files from whatever location they are in to a new folder.

def copier(extension, source, destination):
    imgPattern = re.compile(r".+\." + extension)

    for cdir, subdir, files in os.walk(source):

        for file in files:
            match = imgPattern.search(file)

            if match:
                if match == None:
                    continue

                textFiles = match.group(0)

                abspath = os.path.abspath(source)

                destination_path = os.path.join(destination, textFiles)
                source_path = os.path.join(abspath, textFiles)
            
                shutil.copy(source_path, destination_path)
            

print_info = """"

=========== Aether Copy version 1.0 ===========

How to:
1. Copy the file path of source folder and destination folder
2. Put the extension of the specific file that you want to copy
3. Paste it in input 

"""
print(print_info)
try:
    source_path = input("Source Path: ")
    destination_path = input("Destination Input")
    extension = input("Extension: ")
    copier(extension, source_path, destination_path)
except:
    print("Theres something wrong with your input!")