import os
import sys
import time
import zipfile

# def loadingAnimation():
#     spinner = ['|', '/', '-', '\\']
#     for i in range(101):
#         symbol = spinner[i % len(spinner)]
#         print(f"loading ... {symbol} {i}%", end="\r")
#         time.sleep(0.05)
#     print("Done!\n")  


class Files:
    def __init__(self):
        self.abspath = os.path.dirname(os.path.abspath(__file__))
        
        
    # Backup the file or folder in zip format
    def ZipBackup(self, unzipFile):
        print("""1. File\n2. Folder""")
        try:
            option = int(input(">>> "))
            if option == 1:
                fileToBeZip = str(input("Enter the filename ... \n>>> "))
                filepathToBeZip = os.path.abspath(fileToBeZip)
                print(filepathToBeZip)
            else:
                print("The option that you provide does not exist ... ")
        except Exception as e:
            print(f"Error: {e}")
            
            
        


files = Files()
files.ZipBackup('hello.py')