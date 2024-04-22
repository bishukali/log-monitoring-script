import sys                          # Imports the sys module, which provides access to some variables used or maintained by the Python interpreter and to functions that interact with the interpreter.
import time                         # Imports the time module, which provides various time-related functions.
import signal                       # Imports the signal module, which provides mechanisms to handle asynchronous events such as signals.
import re                           # Imports the re module, which provides support for regular expressions.
from collections import Counter     # Imports the Counter class from the collections module, which is used for counting occurrences of elements in a sequence.

# Function to handle Ctrl+C and exit gracefully so that Defines a function signal_handler that handles the SIGINT signal (Ctrl+C) and exits the script gracefully when it's received.
def signal_handler(sig, frame):
    print("\nMonitoring stopped.")
    sys.exit(0)

# Function to monitor log file so that 
def monitor_log_file(log_file_path, keywords):
    try:
        print(f"Monitoring log file: {log_file_path}")
        with open(log_file_path, 'r') as file:
            # Move to the end of the file
            file.seek(0, 2)
            while True:
                line = file.readline()
                if line:
                    # Check for keywords in the line
                    for keyword in keywords:
                        if re.search(keyword, line):
                            print(line.strip())
                            analyze_log_entry(line)
                else:
                    time.sleep(0.1)
    except FileNotFoundError:
        print(f"Error: Log file '{log_file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

# Function to analyze log entry
def analyze_log_entry(log_entry):
    # Implement your analysis logic here
    pass

if __name__ == "__main__":
    # Register signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)
    
    # Check command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python log_monitor.py <log_file_path> <keyword1> <keyword2> ...")
        sys.exit(1)
    
    log_file_path = sys.argv[1]
    keywords = sys.argv[2:]
    
    # Start monitoring log file
    monitor_log_file(log_file_path, keywords)
