# PythonNetworkFilter

Educational Python project for network log analysis, device configuration validation, and basic firewall security monitoring.

## Overview

This project contains three practical Python exercises focused on networking and cybersecurity fundamentals.

The scripts read network-related text files, process information, and generate reports.

## Features

### 1. Network Connection Analysis
**Script:** `task1.py`

- Reads connection events from `network.log`.
- Identifies unique IP addresses.
- Counts CONNECT events for each IP address.
- Saves results to `connections.txt`.

### 2. Network Configuration Validation
**Script:** `task2.py`

- Reads device settings from `network_config.txt`.
- Extracts hostname, IP address, subnet mask, gateway, and DNS.
- Checks whether devices belong to the `192.168.1.0/24` network.
- Generates `devices.txt`.

### 3. Firewall Log Analysis
**Script:** `task3.py`

- Reads firewall events from `firewall.log`.
- Counts ALLOW and DENY events.
- Identifies IP addresses with three or more DENY events.
- Saves flagged addresses to `blocked.txt`.
- Generates statistics in `report.txt`.

## How to Run

Install Python 3 and execute the scripts from the project directory:

```bash
python task1.py
python task2.py
python task3.py
```

No external Python libraries are required for the basic exercises.

## Educational Purpose

This project was created as part of hands-on Python and networking studies.

It demonstrates file handling, dictionaries, loops, conditional statements, log parsing, and basic security monitoring concepts.

The project uses simulated network data and is intended for educational purposes only.

## License

MIT License.
