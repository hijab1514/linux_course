

## **📄 05\_User\_and\_Group\_Management/user\_group\_management.md**

````markdown
# 👥 Linux User & Group Management

Managing users and groups is a **fundamental skill in Linux**.  
It ensures **security, proper permissions, and organized access** for multiple users on the system.

---

## 1️⃣ Why User & Group Management Matters
- Controls who can access files and directories.
- Protects sensitive system files.
- Essential for multi-user systems, servers, and collaborative environments.
- Helps in **assigning permissions** efficiently via groups.

---

## 2️⃣ Linux Users

### Types of Users
| User Type | Description |
|-----------|-------------|
| Root      | Superuser with full access to all files and commands. |
| Regular   | Standard users with limited privileges. |
| System    | Users created by system processes or services (e.g., `www-data`, `mysql`). |

### Viewing Users
All users are listed in `/etc/passwd`:
```bash
cat /etc/passwd
````

**Sample line:**

```
john:x:1001:1001:John Doe:/home/john:/bin/bash
```

* `john` → username
* `x` → password placeholder (encrypted in `/etc/shadow`)
* `1001` → UID (User ID)
* `1001` → GID (Primary Group ID)
* `John Doe` → full name/description
* `/home/john` → home directory
* `/bin/bash` → default shell

---

## 3️⃣ Linux Groups

Groups allow multiple users to **share permissions** for files and directories.

### Viewing Groups

All groups are in `/etc/group`:

```bash
cat /etc/group
```

**Sample line:**

```
developers:x:1002:john,mary
```

* `developers` → group name
* `x` → password placeholder
* `1002` → GID
* `john,mary` → group members

---

## 4️⃣ Adding Users

```bash
sudo adduser john
```

* Prompts for password, full name, and optional info.
* Creates a home directory: `/home/john`.

Set password separately (if needed):

```bash
sudo passwd john
```

View user info:

```bash
id john
```

---

## 5️⃣ Adding Groups

Create a new group:

```bash
sudo groupadd developers
```

Add a user to a group:

```bash
sudo usermod -aG developers john
```

Verify user groups:

```bash
groups john
```

---

## 6️⃣ Deleting Users & Groups

Delete a user:

```bash
sudo deluser john
```

Delete a group:

```bash
sudo groupdel developers
```

⚠ **Caution:** Use `deluser --remove-home john` to also delete the user’s home directory.

---

## 7️⃣ Changing Ownership of Files

Assign file ownership to user and group:

```bash
sudo chown john:developers file.txt
```

Verify:

```bash
ls -l file.txt
```

Output:

```
-rw-r--r-- 1 john developers 123 Aug 15 12:00 file.txt
```

* Owner → `john`
* Group → `developers`

---

## 8️⃣ Switching Users

Switch to another user:

```bash
su - john
```

Run a command as another user:

```bash
sudo -u john whoami
```

---

## 9️⃣ User Permissions Recap

Linux **permissions (rwx)** depend on:

1. Owner (user)
2. Group
3. Others

Example:

```bash
ls -l file.txt
-rw-r----- 1 john developers 123 Aug 15 12:00 file.txt
```

* Only `john` can read/write.
* Group `developers` can read.
* Others have no access.

---

##  Practical Exercises

1. Create a user `alice` and a group `team`.

```bash
sudo adduser alice
sudo groupadd team
```

2. Add `alice` to `team`.

```bash
sudo usermod -aG team alice
```

3. Create a folder `project` and assign ownership to `alice:team`.

```bash
mkdir project
sudo chown alice:team project
```

4. Test access with another user.

5. Delete the user and group after practice:

```bash
sudo deluser alice --remove-home
sudo groupdel team
```

---

 **Pro Tips**

* Always check permissions before granting root access.
* Use groups to manage multiple users efficiently.
* Take notes of UID and GID when administering multiple systems.
* Combine `chmod`, `chown`, and groups to secure sensitive files.

---

📷 **Screenshots / Illustrations**

* Screenshot of `/etc/passwd` content
* Screenshot of `/etc/group` content
* Example of `ls -l` after changing ownership
* VM terminal showing adding users and groups


```
