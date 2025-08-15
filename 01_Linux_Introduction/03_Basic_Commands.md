# 📜 Basic Linux Commands — Beginner’s Guide

Welcome to the **Basic Linux Commands** guide.  
Here you’ll learn the **essential commands** to navigate and manage files in Linux.

---

## 1️⃣ Navigation Commands

| Command | Description | Example |
|---------|-------------|---------|
| `pwd`   | Shows the current working directory (full path). | `pwd` → `/home/user` |
| `ls`    | Lists files and directories. | `ls` |
| `ls -l` | Lists files with details (permissions, size, date). | `ls -l` |
| `ls -a` | Lists all files including hidden (`.` prefix). | `ls -a` |
| `cd`    | Change directory. | `cd /home` |
| `cd ..` | Go up one directory. | `cd ..` |
| `cd ~`  | Go to home directory. | `cd ~` |

💡 **Tip:** Use `TAB` for auto-completion of file and folder names.

---

## 2️⃣ File & Directory Management

| Command | Description | Example |
|---------|-------------|---------|
| `touch` | Creates an empty file. | `touch file.txt` |
| `mkdir` | Creates a directory. | `mkdir myfolder` |
| `cp`    | Copies files/directories. | `cp file.txt /home/user` |
| `mv`    | Moves or renames files/directories. | `mv old.txt new.txt` |
| `rm`    | Deletes files. | `rm file.txt` |
| `rm -r` | Deletes directories recursively. | `rm -r foldername` |

⚠️ **Warning:** `rm -r` permanently deletes data — no recycle bin.

---

## 3️⃣ Viewing File Content

| Command | Description | Example |
|---------|-------------|---------|
| `cat`   | Displays file content. | `cat notes.txt` |
| `less`  | Scroll through file content (press `q` to quit). | `less bigfile.txt` |
| `head`  | Shows first 10 lines of a file. | `head log.txt` |
| `tail`  | Shows last 10 lines of a file. | `tail log.txt` |
| `tail -f` | Live updates while file changes (useful for logs). | `tail -f /var/log/syslog` |

---

## 4️⃣ File Permissions

Linux uses **permissions** to control who can read, write, and execute files.

- **r** → Read  
- **w** → Write  
- **x** → Execute

| Command | Description | Example |
|---------|-------------|---------|
| `ls -l` | Shows file permissions. | `ls -l` |
| `chmod` | Changes permissions. | `chmod 755 script.sh` |
| `chown` | Changes file owner. | `sudo chown user:user file.txt` |

📌 **Example Output of `ls -l`:**
