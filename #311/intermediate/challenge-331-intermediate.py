import ipaddress

challenge_addresses = ["192.168.0.0/16",
    "172.24.96.17/32", "172.50.137.225/32", "202.139.219.192/32",
    "172.24.68.0/24", "192.183.125.71/32", "201.45.111.138/32",
    "192.168.59.211/32", "192.168.26.13/32", "172.24.0.0/17",
    "172.24.5.1/32", "172.24.68.37/32", "172.24.168.32/32"]

length = len(challenge_addresses)

simplified_addresses = []

for a in range(length):
    simplified_addresses.append(challenge_addresses[a].split("/")[0])

to_remove = []

for b in range(length):
    for c in range(length):
        if b != c:
            if ipaddress.IPv4Address(str(simplified_addresses[b])) in ipaddress.IPv4Network(str(challenge_addresses[c])):
                to_remove.append(simplified_addresses[b])

for address in challenge_addresses:
    if address.split("/")[0] not in to_remove:
        print(address)
