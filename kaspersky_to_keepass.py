import csv

# Define input and output files
input_file = 'kaspersky_passwords.txt'  # Update this with the actual .txt file name
output_file = 'kaspersky_passwords.csv'

# Create empty lists to hold the parsed data
entries = []

# Open the .txt file and parse it
with open(input_file, 'r', encoding='utf-8') as file:
    entry = {}
    for line in file:
        line = line.strip()
        
        if "Website name:" in line:
            entry['Title'] = line.replace("Website name:", "").strip()
        elif "Website URL:" in line:
            entry['URL'] = line.replace("Website URL:", "").strip()
        elif "Login name:" in line:
            # Login name field seems unused; skipping it.
            pass
        elif "Login:" in line:
            entry['Username'] = line.replace("Login:", "").strip()
        elif "Password:" in line:
            entry['Password'] = line.replace("Password:", "").strip()
        elif "---" in line:
            # End of an entry, append it to the list if it contains data
            if entry:
                entries.append(entry)
                entry = {}  # Reset for the next entry

# Write the parsed data to a CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Title', 'Username', 'Password', 'URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(entries)

print(f"Data has been successfully converted and saved to {output_file}")
