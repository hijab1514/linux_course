# changing ownership 
To change the owner of a file, use the following syntax:
''' sudo chown new_owner filename '''
for already in root user 
''' chown new_owner filename '''
To change only the owner recursively (keeping the existing group unchanged):
''' sudo chown -R new_owner /path/to/directory
example 
'''sudo chown -R alice /home/alice/documents

# 2. Changing the Group of a File
To change the group of a file, use this syntax:
''' sudo chown :new_group filename
example 
'''sudo chown :new_group filename
example 
'''sudo chown :developers myfile.txt

To change only the group recursively (keeping the existing owner unchanged):
''' sudo chown -R :new_group /path/to/directory
Example:
sudo chown -R :developers /home/alice/documents

# . Changing Both Owner and Group
To change both the owner and the group at the same time:
''' sudo chown new_owner:new_group filename
For example
''' sudo chown alice:developers myfile.txt

To change ownership for a directory and all its contents, use the -R option:
''' sudo chown -R new_owner:new_group directory_name
For example:
''' sudo chown -R alice:developers /path/to/directory

In Linux, file and directory permissions control who can read, write, or execute a file or directory. You can use the `chmod` command to change these permissions.

### 1. Understanding Linux Permissions

Each file or directory has three permission sets:
- **Owner**: The user who owns the file.
- **Group**: The group assigned to the file.
- **Others**: All other users.

Each set has three types of permissions:
- **Read (r)**: Allows reading the file’s contents or listing a directory’s contents.
- **Write (w)**: Allows modifying a file or creating/deleting files within a directory.
- **Execute (x)**: Allows running a file as a program or accessing a directory.

# 2. Numeric Permission Representation
Permissions are represented by three digits, with each digit corresponding to `Owner`, `Group`, and `Others`, respectively. Each permission type has a numeric value:
- **4** for Read (r)
- **2** for Write (w)
- **1** for Execute (x)

To set multiple permissions, add the values together:
- **7** = Read + Write + Execute
- **6** = Read + Write
- **5** = Read + Execute
- **4** = Read only
- **0** = No permissions

For example, `chmod 755 filename` sets:
- **7** (Read, Write, Execute) for Owner
- **5** (Read, Execute) for Group
- **5** (Read, Execute) for Others

### 3. Changing Permissions Using `chmod`

#### Basic Syntax
```bash
chmod [permissions] filename
```

#### Examples

1. **Setting Permissions Using Numeric Values**:
   - `chmod 755 myfile.txt`: Gives read, write, and execute to Owner, and read and execute to Group and Others.
   - `chmod 644 myfile.txt`: Gives read and write to Owner, and read-only to Group and Others.

2. **Changing Permissions Recursively**
   Use `-R` to apply permissions to all files and directories within a directory.
   ```bash
   chmod -R 755 /path/to/directory
   ```

3. **Using Symbolic Permissions**

You can also use symbolic representations to add, remove, or set specific permissions.

- **Add permissions**:
  ```bash
  chmod u+x filename  # Adds execute permission for the owner (u)
  chmod g+w filename  # Adds write permission for the group (g)
  chmod o+r filename  # Adds read permission for others (o)
  ```

- **Remove permissions**:
  ```bash
  chmod u-x filename  # Removes execute permission for the owner
  chmod g-w filename  # Removes write permission for the group
  chmod o-r filename  # Removes read permission for others
  ```

- **Set specific permissions**:
  ```bash
  chmod u=rwx,g=rx,o=r filename  # Sets owner as rwx, group as rx, others as r
  ```

# Checking Permissions

You can check current permissions with:

```bash
ls -l filename
```

The output format looks like this:
```
-rwxr-xr--
```

This shows permissions for **Owner**, **Group**, and **Others** in the order: Read, Write, Execute.

