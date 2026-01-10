import os, zipfile

def backuptoZip(folder):

    folder = os.path.abspath(folder)

    number = 1
    while True:
        fileName = os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(fileName):
            break
        number += 1

    with zipfile.ZipFile(fileName , "w", zipfile.ZIP_DEFLATED) as backupZip:
        print(f"Copying all files from {folder}")

        for working_directory, sub_directory, files in os.walk(folder):
            for file in files:
                print(f"Copying {file}")
                file_path = os.path.join(working_directory, file)

                if file_path.startswith(file) and file_path.endswith(".zip"):
                    continue

                backupZip.write(working_directory ,os.path.relpath(working_directory, file))
                print(f"Files successfully backup to {working_directory ,os.path.relpath(working_directory, file)}")

filepath = input("Enter filepath: ")
backuptoZip(filepath)