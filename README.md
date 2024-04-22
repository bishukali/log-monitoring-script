# Log Monitoring and Analysis Script

## Overview
This script automates the analysis and monitoring of log files. It continuously monitors a specified log file for new entries and performs basic analysis on the log entries.

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



