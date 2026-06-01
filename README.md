# GoldProber

GoldProber is a fast, lightweight, and multi-threaded subdomain probing tool written in Python. It is designed for penetration testers, bug bounty hunters, and cybersecurity enthusiasts to quickly verify a massive list of subdomains, check their HTTP status codes, detect server information, and filter active targets during the reconnaissance phase.

---

## Features

* **Multi-Threading:** Scan thousands of subdomains within seconds by utilizing concurrent threads.
* **Smart Filtering:** Automatically extracts and categorizes HTTP response codes like `200 OK`, `301/302 Redirects`, and `403 Forbidden`.
* **Redirect Tracking:** Reveals the destination URL (`Location` header) for redirected targets.
* **Server Banner Grabbing:** Identifies the underlying web server technologies (e.g., Nginx, Apache, Cloudflare).
* **Clean Output:** Automatically logs and outputs all live subdomains into a clean, structured text file without cluttering the terminal with dead host errors.

---

## Installation

First, clone the repository to your local machine:

git clone https://github.com/AndrielSec/GoldProbber.git

cd GoldProbber


Make sure you have the required dependencies installed:

pip install requests

Usage

Running the tool is extremely simple. Just pass your target subdomain list and the desired thread count as arguments:
Bash

python3 goldprobber.py <subdomains_file> <threads>

Example:

python3 goldprobber.py subdomains.txt 30

Key Parameters:

    subdomains.txt: The input file containing one subdomain per line.
    
    30: The number of concurrent threads (adjust based on your network bandwidth and system performance).

Output

All active and live targets discovered during the scan are automatically written to a file named:

    canli_sublar.txt

The log file keeps a clean history of the status codes, response paths, and server configurations for later stages of your security assessment.
Disclaimer

This tool is intended solely for educational purposes, authorized security auditing, and bug bounty research. The developer assumes no liability for any misuse, unauthorized scanning, or damage caused by this program. Always ensure you have explicit permission before probing any target.
