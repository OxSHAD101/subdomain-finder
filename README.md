# Subdomain Finder Tool

A lightweight Python tool to enumerate subdomains of a given domain using `crt.sh`. Perfect for cybersecurity research and basic reconnaissance.

## Features
- Fetches subdomains from `crt.sh`.
- Saves subdomains to a file for further analysis.
- Command-line interface for ease of use.

## Prerequisites
- Python 3.x installed on your system.
- `requests` library installed (`pip install requests`).

## Installation
1. Download this repository as a ZIP file or clone it.
2. Navigate to the project directory.

## Usage
Run the tool from your terminal:
```bash
python3 subdomain_finder.py -d <domain> -o <output_file>
