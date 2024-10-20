# 🚫 Website Blocker Script
Website Blocker is a simple Python script that automatically blocks access to specified websites for a set period of time by editing the system's hosts file. This tool can help you stay focused by preventing access to distracting websites.

## ⚡ Features
Block access to distracting websites until a predefined end date.
Automatically redirects blocked websites to 127.0.0.1.
Easily configurable to add or remove websites from the blocked list.
Once the end time is reached, the script unblocks the websites, restoring normal access.
Lightweight and runs continuously in the background, checking every 5 seconds.
## 🛠️ Requirements
Python 3.x
Administrative privileges (since the script modifies the system's hosts file).
Windows OS (the script is set up to modify the Windows hosts file, but can be adjusted for Linux/Mac by changing the hosts_path).
## 🚀 How It Works
The script blocks websites by modifying the system’s hosts file. For the duration of the block, any attempts to access the listed sites will be redirected to 127.0.0.1, effectively blocking access.

When the blocking period ends, the script restores the original state of the hosts file, removing the blocks and allowing normal browsing.

### 👨‍💻 Author
Created by Shashank Tiwari
