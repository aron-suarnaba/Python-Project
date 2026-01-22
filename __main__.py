import logging
import time
from pathlib import Path
from SystemAndFileAutomation.FileHandling.ZipBackup import Files 

Path("SynthFlow").mkdir(exist_ok=True)

logging.basicConfig(
    filename=r"SynthFlow\debugLogs.txt", 
    level=logging.DEBUG, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.debug('Start of program')

def loadingAnimation():
    spinner = ['|', '/', '-', '\\']
    for i in range(101):
        symbol = spinner[i % len(spinner)]
        print(f"loading {symbol} {i}%", end="\r")
        time.sleep(0.02) # Speed up for better UX
    print("Done!\n")

home_cli = """
==================================================
                SynthFlow
==================================================
1. System & File Automation
2. Web Automation & Scraping
3. Data Processing & Analysis
3. Data Processing & Analysis
4. DevOps & Infrastructure
5. Communication & Social Media
6. Testing & QA Automation
7. Desktop & GUI Automation
8. Multimedia Automation
9. Others (NLP, scientific calculations, code generation, etc.)
(Type 'exit' to quit)
"""

def sysfiauto():
    loadingAnimation()
    backup_manager = Files()
    
    print("\n--- System & File Automation ---")
    print("Commands:\n 1. Backup,\n 0 Back (to main menu)")
    
    while True:
        sysfiauto_command = int(input("System & File Automation >> "))
        
        if sysfiauto_command == 1:
            path = input("Enter path to backup: ").strip('"')
            logging.debug(f"Starting backup for: {path}")
            backup_manager.ZipBackup(path)
            
        elif sysfiauto_command == 0:
            break
        else:
            print("Unknown command. Try 'backup' or 'back'.")

def phase_one():
    print(home_cli)
    while True:
        command = input("main >> ").lower().strip()
        match command:
            case "1":
                logging.debug("Executing sysfiauto ... ")
                sysfiauto()
            case "exit" | "quit":
                print("Exiting program. Bye!")
                logging.debug("Program exited by user")
                break
            case _:
                print("Unknown command. Please try again.")

if __name__ == "__main__":
    phase_one()