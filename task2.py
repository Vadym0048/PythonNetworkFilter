
devices = []
device = {}

with open("network_config.txt", "r") as file:
    for line in file:
        key, value = line.strip().split(": ", 1)

        if key == "hostname":
            if device:
                devices.append(device)
            device = {}

        device[key] = value

if device:
    devices.append(device)

with open("devices.txt", "w") as file:
    for device in devices:
        file.write(f"DEVICE: {device['hostname']}\n")
        file.write(f"IP: {device['ip']}\n")
        file.write(f"MASK: {device['mask']}\n")
        file.write(f"GATEWAY: {device['gateway']}\n")
        file.write(f"DNS: {device['dns']}\n")
        file.write("--------------------\n")

        ip = device["ip"]

        if ip.startswith("192.168.1."):
            print(device["hostname"], "- Network OK")
        else:
            print(device["hostname"], "- Wrong network!")

print("Results saved to devices.txt")
