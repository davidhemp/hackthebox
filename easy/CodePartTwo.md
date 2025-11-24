http-alt port open
```
└──╼ [★]$ nmap $IP
Starting Nmap 7.94SVN ( https://nmap.org ) at 2025-11-24 09:02 CST
Nmap scan report for 10.10.11.82
Host is up (0.15s latency).
Not shown: 998 closed tcp ports (reset)
PORT     STATE SERVICE
22/tcp   open  ssh
8000/tcp open  http-alt

Nmap done: 1 IP address (1 host up) scanned in 2.58 seconds
```
We can see there is a website and it has a few links and buttons.
```
└──╼ [★]$ curl $IP:8000 | grep href
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2212  100  2212    0     0   7609      0 --:--:-- --:--:-- --:--:--  7627
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Poppins:wght@400;500;700&display=swap">
    <link rel="stylesheet" href="/static/css/styles.css">
                <a href="/login" class="cta-button">Login</a>
                <a href="/register" class="cta-button">Register</a>
            <br><br><a href="/download" class="cta-button">Download App</a>
```

Looks like I can create an account
```
└──╼ [★]$ curl --data "username=test&password=somepassword" $IP:8000/register
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/login">/login</a>. If not, click the link.
```

Login seems to work and returns a cookie
```
└──╼ [★]$ curl -d "username=test&password=somepassword" --dump-header headers $IP:8000/login
<!doctype html>
<html lang=en>
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to the target URL: <a href="/dashboard">/dashboard</a>. If not, click the link.
```

Said cookie identifies the Server: gunicorn/20.0.4  there is a CVE for that version. That said there doesn't seem to be an admin page I can access with it. 
https://security.snyk.io/vuln/SNYK-PYTHON-GUNICORN-9510910
