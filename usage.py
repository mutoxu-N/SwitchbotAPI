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
