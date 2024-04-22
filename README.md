# Log Monitoring and Analysis Script

## Overview
This script automates the analysis and monitoring of log files. It continuously monitors a specified log file for new entries and performs basic analysis on the log entries.

1) import sys: Imports the sys module, which provides access to some variables used or maintained by the   Python interpreter and to functions that interact with the interpreter.
    import time: Imports the time module, which provides various time-related functions.
    import signal: Imports the signal module, which provides mechanisms to handle asynchronous events such as signals.
    import re: Imports the re module, which provides support for regular expressions.
    from collections import Counter: Imports the Counter class from the collections module, which is used for counting occurrences of elements in a sequence.

2) Defines a function signal_handler that handles the SIGINT signal (Ctrl+C) and exits the script gracefully when it's received.

3) Defines a function monitor_log_file that continuously monitors a specified log file for new entries.
It opens the log file in read mode and moves to the end of the file.
Inside a while True loop, it reads each line from the file, checks if the line contains any of the specified keywords, prints the line if a keyword is found, and then calls the analyze_log_entry function to perform analysis on the log entry.
If the end of the file is reached, it sleeps for a short interval before checking for new lines again.
Error handling is implemented to catch exceptions such as FileNotFoundError and other general exceptions, printing error messages and exiting the script if an error occurs.

4) Defines a placeholder function analyze_log_entry that should contain the logic to analyze each log entry. This function is meant to be implemented by the user according to their specific requirements.

5) hecks if the script is being run as the main program (__name__ == "__main__").
Registers the signal_handler function to handle the SIGINT signal (Ctrl+C).
Parses command-line arguments to extract the log file path and keywords to search for.
Calls the monitor_log_file function to start monitoring the log file with the specified path and keywords.

## Requirements
- Python 3.x

## Usage
1. Clone the repository:

```bash

# git clone https://github.com/bishukali/log-monitoring-script.git


2. Navigate to the directory containing the script:

```bash

# cd log-monitoring-script

3. Run the script using the following command:

```bash

# python log_monitor.py <log_file_path> <keyword1> <keyword2> ... 

// Replace <log_file_path> with the path to the log file you want to monitor and <keyword1>, <keyword2>, etc., with the keywords you want to search for in the log entries.


Example : 

# python log_monitor.py /var/log/syslog error warning -- > This command will monitor the syslog file for new entries containing the keywords "error" and "warning".


4. Stopping the Script : 

Press Ctrl+C to stop the monitoring loop.



