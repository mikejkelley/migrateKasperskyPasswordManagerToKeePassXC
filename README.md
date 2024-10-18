# migrateKasperskyPasswordManagerToKeepasXC
This script takes Kaspersky Password Manager's text output file, reformats the account and password information, strips unnecessary data, and re-writes it as a comma-separated-value that KeePassXC can read. It allows you to migrate from Kaspersky's proprietary, paid software, to KeePassXC: an open source and free password manager.

First, download and install Python from https://python.org. Export your password database by opening Kaspersky Password Manager and navigating to Settings>Import/Export, scroll down and click "Export." Download the script and place it and your Kaspersky Password Manager's exported .txt file in the same directory. Run a command prompt as administrator and change directory to the same said directory with the aformentioned files in it. Enter the following command:

python script_name.py

The script will creat a kaspersky_passwords.csv file. Open KeePass and go to File > Import and select the kaspersky_passwords.csv file. Be sure to securely delete both the .txt and .csv files as they contain all your passwords in plain text. That's it, you're done!
