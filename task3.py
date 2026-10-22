
allow_count = 0
deny_count = 0
denied_ips = {}

with open("firewall.log", "r") as file:
    for line in file:
        ip, action, port = line.split()

        if action == "ALLOW":
            allow_count += 1

        elif action == "DENY":
            deny_count += 1

            if ip not in denied_ips:
                denied_ips[ip] = 0

            denied_ips[ip] += 1

with open("blocked.txt", "w") as file:
    for ip, count in denied_ips.items():
        if count >= 3:
            file.write(f"{ip}: {count} DENY\n")

with open("report.txt", "w") as file:
    file.write("FIREWALL REPORT\n")
    file.write("--------------------\n")
    file.write(f"ALLOW: {allow_count}\n")
    file.write(f"DENY: {deny_count}\n")
    file.write("--------------------\n")

    for ip, count in denied_ips.items():
        file.write(f"{ip}: {count} DENY\n")

print("Firewall analysis completed!")
print("ALLOW:", allow_count)
print("DENY:", deny_count)
print("Results saved to blocked.txt and report.txt")
