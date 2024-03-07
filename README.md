

# Switchbot library for python
## Description
This library provides easy use to [SwitchBotAPI](https://github.com/OpenWonderLabs/SwitchBotAPI).

## Installation
Run command in terminal.
```
pip install easy-switchbot
```

## usage
```python
from pprint import pprint
from switchbot_api.api import SwitchbotAPI
from switchbot_api.devices import *
import time

sAPI = SwitchbotAPI(
    token="",
    secret=""
)

devices = sAPI.devices
smart_plug: PlugMiniJP = devices[0]

print("target:", smart_plug)
pprint(sAPI.status(smart_plug))


print("turn on")
sAPI.run(smart_plug.command_turn_on())

time.sleep(3)

print("turn off")
sAPI.run(smart_plug.command_turn_off())

```

## Limitation
This library can only get status and operate your devices.
Not compatible with Scenes and Webhook.

## Device
I have only `Plug Mini (JP)`. I cannot debug other devices.

