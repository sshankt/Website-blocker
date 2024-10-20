import datetime
import time
import os

# Define the end time
end_time = datetime.datetime(2024, 10, 15)

# List of sites to block
site_blocker = [
    "www.facebook.com",
    "www.justdial.com"
]
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now() < end_time:
        print("Website Blocking......")
        with open(hosts_path, "r+") as hosts_file:
            content = hosts_file.read()
            # Move the file pointer back to the beginning of the file
            hosts_file.seek(0)
            for website in site_blocker:
                if website not in content:
                    hosts_file.write(redirect + " " + website + "\n")
            # Write back the existing content that is not blocked
            hosts_file.write(content)
            hosts_file.truncate()  # Truncate the file to the current position
        time.sleep(5)  # Check every 5 seconds
    else:
        print("Unblocking Websites......")
        with open(hosts_path, "r+") as hosts_file:
            content = hosts_file.readlines()
            hosts_file.seek(0)
            # Only write back lines that do not contain blocked websites
            for line in content:
                if not any(website in line for website in site_blocker):
                    hosts_file.write(line)
            hosts_file.truncate()  # Truncate the file to the current position
        break  # Exit the loop after unblocking
