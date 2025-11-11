import requests
import time
from datetime import datetime

# Configuration
URLS_TO_MONITOR = ["https://www.printwell.com.ph/"]
CHECK_INTERVAL_SESSIONS = 10 # seconds

def check_website(url):
    """Checks the website's status and latency."""
    try:
        response = requests.get(url, timeout=5)
        status_code = response.status_code
        latency = response.elapsed.total_seconds()
        
        if status_code == 200:
            status = "UP (OK)"
        else:
            # Note: status is corrected to show the code
            status = f"DOWN ({status_code})" 
        
        # FIX 1: Must return 3 values to match the while loop unpacking
        return status, latency, None 
        
    except requests.RequestException as e:
        # Returns 3 values: status, latency (0.0), and the error
        return "DOWN (REQUEST ERROR)", 0.0, str(e)
        
    except Exception as e:
        # FIX 2: Returns 3 values for unexpected errors
        return "DOWN (UNEXPECTED ERROR)", 0.0, f"Error: {e}"

def log_status(url, status, latency, error):
    """Logs the monitoring status to the console."""
    # FIX 3: Corrected the typo in the time format string
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Use formatted latency only if it's not 0.0 (from an error)
    latency_str = f"{latency:.4f}" if latency > 0.0 else "N/A"

    if error:
        log_line = f"[{timestamp}] URL: {url} | STATUS: {status} | LATENCY: {latency_str}s | ERROR: {error}"
    else:
        log_line = f"[{timestamp}] URL: {url} | STATUS: {status} | LATENCY: {latency_str}s"
        
    print(log_line)
    
# Added a try/except for a clean exit (Ctrl+C)
try:
    print("Starting Website Monitoring. Press Ctrl+C to stop.")
    while True:
        for url in URLS_TO_MONITOR:
            # Unpacks the 3 consistent return values
            status, latency, error = check_website(url)
            log_status(url, status, latency, error)
        
        print(f"The scanner is sleeping for {CHECK_INTERVAL_SESSIONS} seconds...")
        time.sleep(CHECK_INTERVAL_SESSIONS)
except KeyboardInterrupt:
    print("\nMonitoring stopped by user.")
except Exception as e:
    print(f"\nFATAL ERROR: Script terminated due to unhandled exception: {e}")