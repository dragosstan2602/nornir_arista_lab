from nornir import InitNornir
from nornir.plugins.tasks import networking
from nornir.plugins.functions.text import print_result


nr = InitNornir(config_file="inventory/config.yaml")
test_hosts = nr.filter(role='spine')

results = test_hosts.run(task=networking.napalm_get, getters=["facts"])

for device in results.keys():
    print(device, ' - ', results[device][0].result)

