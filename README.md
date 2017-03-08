A Wechat personal account based assistant designed for saving the article sharing it received to pocket.

## How to use
![](https://raw.githubusercontent.com/heshiyou/wechat-pocket/master/wechat-pocket-shots.jpg)
### Step 1:

add settings.py for your own to set tuling api token and pocket token.
```python

from settings_default import *
DEBUG = False

CONSUMER_KEY = '' # pocket consumer key
ACCESS_TOKEN = '' # pocket api access token

TULING_KEY = '' # tuling api key

```

### Step 2:

```bash
$~ settings=settings python main.py
```