
## **📄 04\_Intermediate\_Commands.md**

**(Inside `02_File_And_Directory_Management/`)**

````markdown
# ⚙️ Linux Intermediate Commands

After learning the basic commands, it's time to explore **more powerful Linux commands** that will help you manage processes, permissions, packages, and networks.

---

## 1️⃣ Process Management

A **process** is any running program or command in Linux.

| Command | Description | Example |
|---------|-------------|---------|
| `ps`    | Show running processes for current shell. | `ps` |
| `ps aux`| Show all running processes on system. | `ps aux` |
| `top`   | Real-time view of running processes. | `top` |
| `htop`  | Improved interactive process viewer (needs installation). | `htop` |
| `kill PID` | Kill a process by its PID. | `kill 1234` |
| `killall name` | Kill all processes with given name. | `killall firefox` |

💡 **Tip:** Press `q` to exit `top` or `htop`.

---

## 2️⃣ File Permissions & Ownership

Permissions control **who can read, write, or execute** a file.

### Viewing Permissions
```bash
ls -l
````

Example output:

```
-rwxr-xr--
```

* **First character:** File type (`-` for file, `d` for directory)
* **rwx:** Owner permissions (read/write/execute)
* **r-x:** Group permissions
* **r--:** Others

### Changing Permissions

| Command | Description              | Example               |
| ------- | ------------------------ | --------------------- |
| `chmod` | Change file permissions. | `chmod 755 script.sh` |

Modes:

* **Number mode:** `chmod 644 file.txt`

  * 7 = read + write + execute
  * 6 = read + write
  * 4 = read only
* **Symbolic mode:** `chmod u+x file.sh` (add execute for owner)

### Changing Ownership

| Command | Description        | Example                         |
| ------- | ------------------ | ------------------------------- |
| `chown` | Change file owner. | `sudo chown user:user file.txt` |

---

## 3️⃣ Package Management

### Debian/Ubuntu (APT)

```bash
sudo apt update      # Update package list
sudo apt upgrade     # Upgrade installed packages
sudo apt install git # Install a package
sudo apt remove git  # Remove a package
```

### CentOS/Fedora (YUM/DNF)

```bash
sudo yum install git
sudo yum remove git
```

---

## 4️⃣ Archiving & Compression

| Command                     | Description              | Example                        |
| --------------------------- | ------------------------ | ------------------------------ |
| `tar -cvf archive.tar file` | Create tar archive.      | `tar -cvf backup.tar file.txt` |
| `tar -xvf archive.tar`      | Extract tar archive.     | `tar -xvf backup.tar`          |
| `gzip file`                 | Compress file with gzip. | `gzip log.txt`                 |
| `gunzip file.gz`            | Decompress gzip file.    | `gunzip log.txt.gz`            |
| `zip archive.zip file`      | Create zip archive.      | `zip myfiles.zip file1 file2`  |
| `unzip archive.zip`         | Extract zip archive.     | `unzip myfiles.zip`            |

---

## 5️⃣ Searching & Filtering

| Command                 | Description                        | Example                       |
| ----------------------- | ---------------------------------- | ----------------------------- |
| `grep "text" file`      | Search for text in file.           | `grep "error" log.txt`        |
| `grep -i`               | Case-insensitive search.           | `grep -i "linux" file.txt`    |
| `grep -r`               | Search recursively in directories. | `grep -r "main()" /home/user` |
| `find /path -name file` | Find file by name.                 | `find /home -name file.txt`   |

💡 Combine `grep` with `pipe (|)` to filter results:

```bash
ps aux | grep firefox
```

---

## 6️⃣ Networking Commands

| Command       | Description                     | Example                             |
| ------------- | ------------------------------- | ----------------------------------- |
| `ip addr`     | Show IP address.                | `ip addr`                           |
| `ping host`   | Test connectivity.              | `ping google.com`                   |
| `wget url`    | Download file from web.         | `wget https://example.com/file.zip` |
| `curl url`    | Fetch data from URL.            | `curl https://api.github.com`       |
| `ssh user@ip` | Remote login to another system. | `ssh user@192.168.1.10`             |

---

## 7️⃣ Disk Usage & System Info

| Command         | Description              | Example             |
| --------------- | ------------------------ | ------------------- |
| `df -h`         | Show disk space usage.   | `df -h`             |
| `du -sh folder` | Show folder size.        | `du -sh /home/user` |
| `free -h`       | Show memory usage.       | `free -h`           |
| `uname -a`      | Show system information. | `uname -a`          |

---

## 8️⃣ Practice Challenge

Try this small project:

```bash
# 1. Create a directory
mkdir project

# 2. Create a file with content
echo "Linux is powerful!" > project/info.txt

# 3. Change file permissions
chmod 644 project/info.txt

# 4. Archive and compress the folder
tar -czvf project_backup.tar.gz project/

# 5. Search for the word "Linux" inside the file
grep "Linux" project/info.txt

Do you want me to make **Advanced Commands** now?
```
