
connections = {}

with open("network.log", "r") as file:
    for line in file:
        ip, action = line.split()

        if ip not in connections:
            connections[ip] = 0

        if action == "CONNECT":
            connections[ip] += 1

with open("connections.txt", "w") as file:
    for ip, count in connections.items():
        file.write(f"{ip}: {count}\n")

print("Analysis completed!")
print("Results saved to connections.txt")
