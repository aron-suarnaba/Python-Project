import os
from pathlib import Path
import time
import sys
import shutil
import zipfile
from FileManagement import FileManagementCLI


def progressBar():
    TOTAL_COUNT = 100
    
    for i in range(1, TOTAL_COUNT + 1):
        progress = (i / TOTAL_COUNT) * 100
        
        sys.stdout.write(f'\rProgress: [{i}/{TOTAL_COUNT}] {progress:.2f}% complete')
        sys.stdout.flush()
        
        time.sleep(0.1)


            
            
        
        
try:
    FileManagementCLI()
except Exception as e:
    print(f"Error: {e}")
    