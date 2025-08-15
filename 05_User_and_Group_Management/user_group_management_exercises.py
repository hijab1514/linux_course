"""
🐧 User & Group Management Exercises — Linux Learning

This script helps beginners **practice user and group management commands**.
It provides instructions and simulated execution in a safe environment.

Note: This script does NOT create real users/groups. It prints commands
and explanations for learning purposes.
"""

import os

def print_heading(text):
    print("\n" + "="*len(text))
    print(text)
    print("="*len(text) + "\n")

# 1️⃣ Add a User
print_heading("Exercise 1: Add a User")
print("Command to add user 'alice':")
print("sudo adduser alice")
print("\nSet password:")
print("sudo passwd alice")

# 2️⃣ Add a Group
print_heading("Exercise 2: Add a Group")
print("Command to create group 'team':")
print("sudo groupadd team")

# 3️⃣ Add User to Group
print_heading("Exercise 3: Add User to Group")
print("Command to add 'alice' to 'team':")
print("sudo usermod -aG team alice")

# 4️⃣ Check User Groups
print_heading("Exercise 4: Check User Groups")
print("Command to view groups for 'alice':")
print("groups alice")

# 5️⃣ Create a Directory and Assign Ownership
print_heading("Exercise 5: Directory Ownership")
print("Commands:")
print("mkdir project")
print("sudo chown alice:team project")
print("ls -l project  # Verify ownership")

# 6️⃣ Remove User & Group
print_heading("Exercise 6: Remove User & Group")
print("Commands:")
print("sudo deluser alice --remove-home")
print("sudo groupdel team")

# 7️⃣ Suggested Practice
print_heading("Suggested Practice")
print("1. Try switching users using 'su - alice'")
print("2. Run a command as another user using 'sudo -u alice command'")
print("3. Experiment with chmod and chown for file permissions")
print("4. Observe /etc/passwd and /etc/group contents safely in VM")
