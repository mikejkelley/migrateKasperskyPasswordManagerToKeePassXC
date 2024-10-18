# migrateKasperskyPasswordManagerToKeepasXC
The accompanying script (kaspersky_to_keepass.py) takes Kaspersky Password Manager's outputted text file, reformats the account and password information, strips unnecessary data, and re-writes it as a comma-separated-value file that KeePassXC can read. It allows you to migrate from Kaspersky's proprietary, paid software, to KeePassXC: an open source and free password manager.

If you haven't already, download and install Python from https://python.org. Export your password database by opening Kaspersky Password Manager and navigating to Settings > Import/Export. Then, scroll down and click "Export." Rename the exported file to "kaspersky_passwords.txt" so that it can be properly referenced. Download kaspersky_to_keepass.py, placing it in the same directory as your exported .txt file. Run a command prompt as administrator and change directory to the same said directory with the aformentioned files in it. Enter the following command:    
`python kaspersky_to_keepass.py`

The script will create a kaspersky_passwords.csv file. Open KeePass and go to File > Import and select the kaspersky_passwords.csv file. Be sure to securely delete both the .txt and .csv files as they contain all your passwords in plain text. Follow the on-screen prompts. That's it, you're done!
