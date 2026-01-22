import os
import zipfile
import time

class Files:
    def __init__(self):
        pass
        
    def UserInterface(self):
        print("""
              ==============================================
                            SynthFlow - Zip Backup
              ==============================================
              """)
        
    def ZipBackup(self, filepath):
        self.UserInterface()
        filepath = os.path.abspath(filepath.strip('"'))

        if not os.path.exists(filepath):
            print(f"Error: Path '{filepath}' does not exist.")
            return

        print("1. Zip as Single File\n2. Zip as Whole Folder")
        option = int(input(">>> "))

        # Logic to create a unique backup name
        counter = 1
        base_path = os.path.splitext(filepath)[0]
        while True:
            new_zip_name = f"{base_path}_{counter}.zip"
            if not os.path.exists(new_zip_name):
                break
            counter += 1

        with zipfile.ZipFile(new_zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
            if option == 1:
                print(f"Zipping file: {os.path.basename(filepath)}...")
                zipf.write(filepath, arcname=os.path.basename(filepath))
            elif option == 2:
                print(f"Zipping folder: {os.path.basename(filepath)}...")
                for root, dirs, files in os.walk(filepath):
                    for file in files:
                        file_full_path = os.path.join(root, file)
                        if file_full_path == new_zip_name: continue
                        arcname = os.path.relpath(file_full_path, os.path.dirname(filepath))
                        zipf.write(file_full_path, arcname)
        
        print(f"Successfully backed up to: {new_zip_name}\n")