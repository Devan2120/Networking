from boltiot import Bolt
import conf

api_key = conf.bolt_api_key
device_id = conf.device_id
mybolt = Bolt(api_key, device_id)
response = mybolt.isOnline()
print(response)
