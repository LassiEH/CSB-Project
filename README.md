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

**Account:**
```
**Username** - john
**password** - password
```

[**Flaw 1**](https://github.com/LassiEH/CSB-Project/blob/b34fcf15f3a962548316a8ee654b242978b0137a/mysite/polls/templates/polls/detail.html#L13)
CSRF
