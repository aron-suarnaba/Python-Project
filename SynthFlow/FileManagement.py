from pathlib import Path
import os
import sys
import zipfile

    

def backupFile(folder_path_str):
    
    #1. Validate if the value is a string
    folder = Path(folder_path_str)     
    if not folder.is_dir():
        raise FileNotFoundError(f"Directory not found: {folder_path_str}")
        
    #2. Create a folder name
    number = 1
    while True:
        zip_filename = folder.parent / f"{folder.name}_{number}.zip"
        
        if not zip_filename.exists():
            print(f"Creating backup file: {zip_filename}")
            break
        number += 1
        
    
    print("Starting backup ... ")
    
    #3. Create a zipfile folder 
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as backup_zip:
    
        #4. Walk the entire folder tree and compress the files in each folder
        for dirpath_str, subfolders, filenames in os.walk(folder):
            
            dirpath = Path(dirpath_str)
            
            archive_path_header = dirpath.relative_to(folder.parent)
            
            print(f"archive_path_header: {archive_path_header}")
            
            for filename in filenames:
                
                file_to_write = dirpath / filename
                                
                backup_zip.write(file_to_write, archive_path_header)
                
    print(f"\nBackup complete and saved as: {zip_filename.resolve()}")


        
def FileManagementCLI():
    display = """
    1. Log File Analyzer
    2. Word Counter & Frequency
    3. Simple Data Transformation
    4. File Organizer
    5. Backup File
    6. PDF/Word Metadata Extractor
    7. Text File Encryption/Decryption Tool
    8. Document Management System
    9. Automated Backup Scheduler
    10. Log Monitoring Dashboard
    11. Checksum Generator and Verifier
    """
    print(display)
    command = ""
    while True:
        command = int(input(">>> "))
        if command == 5:
            path = str(input("Folder Path: "))
            backupFile(path)