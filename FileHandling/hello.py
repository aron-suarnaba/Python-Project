import os
import sys
import time
import zipfile
import shutil

# def loadingAnimation():
#     spinner = ['|', '/', '-', '\\']
#     for i in range(101):
#         symbol = spinner[i % len(spinner)]
#         print(f"loading ... {symbol} {i}%", end="\r")
#         time.sleep(0.05)
#     print("Done!\n")  


class Files:
    def __init__(self):
        pass
        # self.abspath = os.path.dirname(os.path.abspath(__file__))
        
        
    # Backup the file or folder in zip format
    def ZipBackup(self, filepath):
        print("1. Zip Files\n2. Zip Folder")
        option = int(input(">>> "))

        if option == 1:
            confirmation = bool(input("Confirm? \n1. Yes\n2. No\n>>>"))

            if confirmation:

                counter = 2

                # Creating New Name
                while True:
                    separatedFile = filepath.rsplit('.', 1)
                    rawFilePath = separatedFile[0]
                    extension = separatedFile[1]
                    stringCounter = str(counter)
                    newFilePath = rawFilePath + "_" + stringCounter + "." + extension

                    if os.path.exists(newFilePath):
                        print(f"{newFilePath} is exist ... \Creating new filename ... ")
                        counter += 1
                    else:
                        print(newFilePath)
                        break

                with open(newFilePath) as filepath:
                    print(filepath)

            else:
                print("Aborting ... ")

        else:
            print("The option that you provide does not exist ... ")


files = Files()
files.ZipBackup("C:/Users/aron.suarnaba/Downloads/Image (1).jpg")