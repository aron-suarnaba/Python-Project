import os
import zipfile
import time

class Files:
    def __init__(self, path=None):
        self.path = path
        
    def UserInterface(self):
        print("""
              ==============================================
                            SynthFlow - Zip Backup
              ==============================================
              """)
        
    def ZipBackup(self):
        self.UserInterface()
        
        while True:
            print("1. Zip a Single File\n2. Zip a Whole Folder\n3. Exit")
            try:
                option = int(input(">>> "))
            except ValueError:
                continue

            if option == 3:
                break

            print("Enter the path to backup:")
            filepath = input(">>> ").strip('"') # Strips quotes if user copied path as link
            filepath = os.path.abspath(filepath)

            if not os.path.exists(filepath):
                print("Error: That path does not exist.")
                continue

            # --- Logic to create a unique backup name ---
            # e.g., "mydata.docx" becomes "mydata_2.zip"
            counter = 1
            base_path = os.path.splitext(filepath)[0]
            while True:
                new_zip_name = f"{base_path}_{counter}.zip"
                if not os.path.exists(new_zip_name):
                    break
                counter += 1

            # --- Option 1: Single File ---
            if option == 1:
                if not os.path.isfile(filepath):
                    print("Error: The path provided is not a file.")
                    continue
                
                with zipfile.ZipFile(new_zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
                    print(f"Zipping file: {os.path.basename(filepath)}...")
                    zipf.write(filepath, arcname=os.path.basename(filepath))
                print(f"Successfully backed up to: {new_zip_name}\n")

            # --- Option 2: Folder ---
            elif option == 2:
                if not os.path.isdir(filepath):
                    print("Error: The path provided is not a folder.")
                    continue

                with zipfile.ZipFile(new_zip_name, "w", zipfile.ZIP_DEFLATED) as zipf:
                    print(f"Zipping folder: {os.path.basename(filepath)}...")
                    for root, dirs, files in os.walk(filepath):
                        for file in files:
                            # Avoid zipping the backup file if it's created inside the same folder
                            file_path = os.path.join(root, file)
                            if file_path == new_zip_name:
                                continue
                            
                            # Create relative path for the zip structure
                            arcname = os.path.relpath(file_path, os.path.dirname(filepath))
                            zipf.write(file_path, arcname)
                print(f"Successfully backed up to: {new_zip_name}\n")
            
            else:
                print("Invalid option.")

# To run the code:
backup_manager = Files()
backup_manager.ZipBackup()