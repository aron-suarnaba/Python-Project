import logging
import time
from pathlib import Path

logging.basicConfig(filename="SynthFlow\debugLogs.txt", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')

def loadingAnimation():
    spinner = ['|', '/', '-', '\\']
    for i in range(101):
        symbol = spinner[i % len(spinner)]
        print(f"loading {symbol} {i}%", end="\r")
        time.sleep(0.05)
    print("Done!\n")  # fixed

home_cli = """
==================================================
                SynthFlow
==================================================

1. System & File Automation
2. Web Automation & Scraping
3. Data Processing & Analysis
4. DevOps & Infrastructure
5. Communication & Social Media
6. Testing & QA Automation
7. Desktop & GUI Automation
8. Multimedia Automation
9. Others (NLP, scientific calculations, code generation, etc.)
"""

def sysfiauto():
    loadingAnimation()
    while True:
        sysfiauto_command = input(">> ")

def phase_one():
    print(home_cli)
    while True:
        command = input(">> ")
        match command:
            case "1":
                logging.debug("Executing sysfiauto ... ")
                sysfiauto()
                logging.debug("")
            case "exit" | "quit":
                print("Exiting program. Bye!")
                break
            case _:
                print("Unknown command. Please try again.")

phase_one()
