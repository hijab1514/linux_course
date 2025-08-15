# 📂 Linux File & Directory Management — Basic Commands

In Linux, almost everything is treated as a **file**, including directories.  
Mastering file and directory commands is essential for everyday Linux use.

---

## 1️⃣ Navigation Basics

| Command | Description | Example |
|---------|-------------|---------|
| `pwd`   | Show current working directory. | `pwd` → `/home/user` |
| `cd`    | Change directory. | `cd /etc` |
| `cd ..` | Go up one directory. | `cd ..` |
| `cd ~`  | Go to your home directory. | `cd ~` |
| `ls`    | List files and folders. | `ls` |
| `ls -l` | Long format listing. | `ls -l` |
| `ls -a` | Show hidden files. | `ls -a` |

💡 **Tip:** Use `TAB` to auto-complete names.

---

## 2️⃣ Creating Files & Directories

| Command | Description | Example |
|---------|-------------|---------|
| `touch` | Create an empty file. | `touch file.txt` |
| `mkdir` | Create a new directory. | `mkdir myfolder` |
| `mkdir -p` | Create nested directories. | `mkdir -p folder1/folder2` |

---

## 3️⃣ Copying, Moving, Renaming

| Command | Description | Example |
|---------|-------------|---------|
| `cp file.txt /path` | Copy file to path. | `cp notes.txt /home/user` |
| `cp -r dir/ /path` | Copy directory recursively. | `cp -r project/ /home/user` |
| `mv old.txt new.txt` | Rename a file. | `mv old.txt new.txt` |
| `mv file.txt /path` | Move file to another directory. | `mv report.txt /tmp` |

---

## 4️⃣ Deleting Files & Directories

| Command | Description | Example |
|---------|-------------|---------|
| `rm file.txt` | Delete a file. | `rm hello.txt` |
| `rm -r folder` | Delete a directory recursively. | `rm -r myfolder` |
| `rmdir folder` | Remove an empty directory. | `rmdir old_folder` |

⚠️ **Warning:** `rm -r` is permanent — no recycle bin.

---

## 5️⃣ Viewing Files

| Command | Description | Example |
|---------|-------------|---------|
| `cat file.txt` | Show file content. | `cat notes.txt` |
| `less file.txt` | Scroll through file. | `less bigfile.txt` |
| `head file.txt` | Show first 10 lines. | `head log.txt` |
| `tail file.txt` | Show last 10 lines. | `tail log.txt` |
| `tail -f file.txt` | Watch file updates in real time. | `tail -f /var/log/syslog` |

---

## 6️⃣ Practice Exercise
Try these commands in your Linux terminal:
```bash
pwd
mkdir practice_folder
cd practice_folder
touch file1.txt
echo "Hello Linux!" > file1.txt
cat file1.txt
cp file1.txt copy.txt
mv copy.txt renamed.txt
rm renamed.txt
cd ..
rm -r practice_folder
