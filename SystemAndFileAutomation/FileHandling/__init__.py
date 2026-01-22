from FileHandling.ZipBackup import Files

if __name__ == "__main__":
    path_to_backup = input("Enter path to backup: ")
    backup_manager = Files(path_to_backup)
    backup_manager.run_backup()