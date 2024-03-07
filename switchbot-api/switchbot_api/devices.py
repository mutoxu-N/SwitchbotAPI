import json


class SwitchbotDevice:
    """parent class of switchbot devices
    """

    def __init__(
            self,
            device_id: str,
            device_name: str,
            enable_cloud_service: bool,
            hub_device_id: str) -> None:
        """the constructor for SwitchbotDevice

        Args:
            device_id (str): the id of the device
            device_name (str): the name of the device
            enable_cloud_service (bool): whether device enable the cloud service or not
            hub_device_id (str): if the device has any parents, show their ids.
        """

        self._device_id = device_id
        self._device_name = device_name
        self._enable_cloud_service = enable_cloud_service
        self._hub_device_id = hub_device_id

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id: {self._device_id}, name: {self._device_name})"

    @property
    def device_id(self) -> str:
        return self._device_id

    @property
    def device_name(self) -> str:
        return self._device_name

    @property
    def enable_cloud_service(self) -> bool:
        return self._enable_cloud_service

    @property
    def hub_device_id(self) -> str:
        return self._hub_device_id


class Bot(SwitchbotDevice):
    def __init__(
            self,
            device_id: str,
            device_name: str,
            enable_cloud_service: bool,
            hub_device_id: str) -> None:
        super().__init__(device_id, device_name, enable_cloud_service, hub_device_id)

    def command_turn_on(self) -> str:
        return json.dumps({
            "command": "turnOn",
            "commandType": "command",
            "parameter": "default",
        })

    def command_turn_off(self) -> str:
        return json.dumps({
            "command": "turnOff",
            "commandType": "command",
            "parameter": "default",
        })

    def command_press(self) -> str:
        return json.dumps({
            "command": "press",
            "commandType": "command",
            "parameter": "default",
        })


class PlugMiniJP(SwitchbotDevice):
    def __init__(
            self,
            device_id: str,
            device_name: str,
            enable_cloud_service: bool,
            hub_device_id: str) -> None:
        super().__init__(device_id, device_name, enable_cloud_service, hub_device_id)

    def command_turn_on(self) -> str:
        return json.dumps({
            "command": "turnOn",
            "commandType": "command",
            "parameter": "default",
        })

    def command_turn_off(self) -> str:
        return json.dumps({
            "command": "turnOff",
            "commandType": "command",
            "parameter": "default",
        })

    def command_toggle(self) -> str:
        return json.dumps({
            "command": "toggle",
            "commandType": "command",
            "parameter": "default",
        })
