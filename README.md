# choopster.py
A cohost bot for creating cohost! posts based on generated results from [Poopster](https://github.com/anvilsp/Poopster), using [Cohost.py](https://github.com/valknight/Cohost.py).

# Usage
Running `bot.py` will automatically send a post.

# Environment Variables
The `.env` file should be set up as follows:
```
COHOST_LOGIN="YOUR_COHOST_LOGIN_EMAIL_HERE"
COHOST_PASS="YOUR_COHOST_PASSWORD_HERE"
COHOST_PAGE="YOUR_COHOST_PAGE"
PARSE_URL="https://poopster.anvilsp.com/api?parse=web"
```