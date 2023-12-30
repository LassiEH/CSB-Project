**Cyber security base - 2023 project 1**

This project contains a web application that has multiple cyber security flaws in its design.

The flaws:
  1. The lack of CSRF tokens.
  2. No logging for noticing breaches.
  3. Flaws in security configuration, debug mode on.
  4. SQL injection.
  5. Indentification and authentication failures, hashing.

Download the project and then run it with

```
python3 manage.py runserver
```

Now the application can be found at:
http://localhost:8000/polls/

In the case that it doesn't work run the following commands as well:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

**Account:**
```
Username: john
Password: password
```

[**FLAW 1:**](https://github.com/LassiEH/CSB-Project/blob/b34fcf15f3a962548316a8ee654b242978b0137a/mysite/polls/templates/polls/detail.html#L13)
 CSRF
 
[**FLAW 2:**](https://github.com/LassiEH/CSB-Project/blob/31f8efd1bf4247eb59634f24b3865b76601fd577/mysite/mysite/settings.py#L116)
 Logging and monitoring failures

[**FLAW 3:**](https://github.com/LassiEH/CSB-Project/blob/31f8efd1bf4247eb59634f24b3865b76601fd577/mysite/mysite/settings.py#L27)
 Security misconfiguration

[**FLAW 4:**](https://github.com/LassiEH/CSB-Project/blob/31f8efd1bf4247eb59634f24b3865b76601fd577/mysite/polls/views.py#L23)
 SQL injection

[**FLAW 5:**](https://github.com/LassiEH/CSB-Project/blob/31f8efd1bf4247eb59634f24b3865b76601fd577/mysite/mysite/settings.py#L150)
 Identification and authentication failures
