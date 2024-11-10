two type of user 
1. Standard user 
2. Root user (Admin/Root)
 its more powerfull than standard 

# cat command help you to view inside 

#shadow file In Linux, the /etc/shadow file stores information about the user's passwords on a Linux system. Moreover,
it is an important file for system administration and security, as it allows the system to verify the user's identity and enforce password policie

it's mstly encrpted 
![1-45](https://github.com/user-attachments/assets/f0208fba-5ef5-403c-abc2-12cac1cfdaa2)

# For adding user and password 
In Ubuntu (and most Linux distributions), you can add a user with a password by using the `useradd` and `passwd` commands, or the `adduser` command, which is a friendlier, interactive command.

### 1. Adding a User with `adduser`

`adduser` is the simplest way to create a user, as it prompts you for all the necessary information, including the password.

```bash
sudo adduser new_username
```

Replace `new_username` with the desired username. You’ll be prompted to enter and confirm a password and provide additional user information (e.g., full name, room number), which you can leave blank by pressing Enter. 

### 2. Adding a User with `useradd` and Setting a Password

The `useradd` command is less interactive and requires additional options to set up a user fully.

1. **Create the User**:

   ```bash
   sudo useradd -m -s /bin/bash new_username
   ```

   - `-m`: Creates a home directory for the new user.
   - `-s /bin/bash`: Sets the default shell to Bash. You can specify a different shell if needed.

2. **Set a Password for the User**:

   ```bash
   sudo passwd new_username
   ```

   Enter the desired password when prompted.

### 3. Adding the User to Specific Groups (Optional)

By default, a new user has their own group, but you may want to add them to other groups for additional permissions. For example, adding the user to the `sudo` group grants administrative privileges.

```bash
sudo usermod -aG group_name new_username
```

Replace `group_name` with the desired group, like `sudo`:

```bash
sudo usermod -aG sudo new_username
```

### Summary Example

Here’s an example of adding a user named `alice`, setting a password, and adding them to the `sudo` group:

```bash
sudo adduser alice            # Creates the user and prompts for a password
sudo usermod -aG sudo alice   # Grants sudo privileges
```

Now, `alice` is ready to log in with their password and has administrative privileges if needed.
''' useradd tabi '''
for deleting 
''' userdel tabi '''
if you want to detail like add directory 
''' useradd -m tabi '''
to add bash too and caption name perfect too 
''' useradd -c "tabi fatima" -m -s "/bin/bash" tabi 
# for password 
passwd tabi ....
to lock accound 

'''usermod -l tabi 

to unlock

''' usermod -u tabi '''
to change screen name

''' usermod -c "Turrab Fatima " tabi 
if you wnat delete account along with directory 
''' userdel -r tabi '''

## Groups 

![Screenshot (51)](https://github.com/user-attachments/assets/5ec6d18b-2f34-49db-94f4-9370284fcc49)
Two types of group 
1. admin group
2. user group
   to check where the admin group is
   in /etc/ seudos file
   use cat function

   for group id
   cat group
   in 'gsshadow' file all the group password are stored in encrpted form
   # creating a Group
   groupadd mesam

   # adding user to the group
   usermod -G mesam tabi

   #Removing a user from the group
   groupdel mesam
