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
