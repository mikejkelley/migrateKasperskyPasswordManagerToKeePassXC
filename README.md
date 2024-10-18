# migrateKasperskyPasswordManagerToKeepasXC
This script takes Kaspersky Password Manager's text output file, reformats the account and password information, strips unnecessary data, and re-writes it as a comma-separated-value that KeePassXC can read. This script allows you to migrate from Kaspersky's proprietary, paid software, to KeePassXC: an open source and free password manager.

First, download and install Python from https://python.org. Export your password database by opening Kaspersky Password Manager and navigating to Settings>Import/Export, scroll down and click "Export." Download the script and place it and your Kaspersky Password Manager's exported .txt file in the same directory.
