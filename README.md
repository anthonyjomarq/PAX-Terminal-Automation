# PAX-Terminal-Automation
A Python-based tool leveraging Sikuli to automate PAX terminal setup and merchant onboarding. Reduces configuration time by 65%+ and dynamically adjusts settings for retail and restaurant environments. Enhances efficiency and minimizes errors.

# Terminal Management Automation

This project automates terminal management tasks using SikuliX for automation and Python for data handling. The script reads terminal information from a CSV file and performs various actions such as pushing apps to terminals and configuring settings.

# Prerequisites

- [Python](https://www.python.org/downloads/)
- [SikuliX](https://sikulix.github.io/)
- A CSV file (`terminal_datacsv.csv`) with the following columns:
  - MID
  - Merchant Name
  - Terminal Name
  - SN (Serial Number)
  - TID
  - Model
  - Phone number (NO -)
  - Email
  - City
  - Customer Name
  - Zip Code
  - Street

## Installation

1. Clone the repository:

2. Install Python, SikuliX and Java 64 bit.

## Usage

1. Place your `terminal_datacsv.csv` file in the project directory.

2. Run the script in SikuliX:

3. The script will read the CSV file and perform the necessary actions, including configuring terminal settings and pushing apps.

# Script Breakdown

- Read CSV File: Extracts data from `terminal_datacsv.csv`.
- Handle Email Popup: Closes email pop-ups if they appear.
- Open PAX Portal and Search Merchant: Opens the portal and searches for the merchant.
- Add Terminal: Adds a new terminal with provided details.
- Push and Configure Apps: Pushes and configures multiple apps (e.g., Omaha, TermLink, DynaPay).
- Configure Various Settings: Configures terminal settings such as refund, void, debit, EBT, cash, and receipt settings.
- DataWire Configuration: Configures MID and TID settings.
- DynaPay AgilPay Configuration: Configures terminal settings for DynaPay AgilPay.

## License

This project is licensed under the MIT License.
