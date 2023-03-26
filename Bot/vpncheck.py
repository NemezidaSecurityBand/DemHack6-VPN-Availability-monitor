import random
from evpn import ExpressVpnApi

def evpn_check(location):
    with ExpressVpnApi() as api:
        locations = api.locations
        loc = random.choice(locations)
        api.connect(loc["id"])
    if api.is_connected():
        return 1
    else:
        return 0
