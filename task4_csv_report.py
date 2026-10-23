import csv

online_count = 0
offline_count = 0

with open("network.csv", "r") as file:
    reader = csv.DictReader(file)

    with open("offline_devices.txt", "w") as output:
        for row in reader:
            device = row["Device"]
            ip = row["IP"]
            status = row["Status"]

            if status == "Online":
                online_count += 1

            elif status == "Offline":
                offline_count += 1
                output.write(f"{device} - {ip}\n")

print("Online:", online_count)
print("Offline:", offline_count)
print("Results saved to offline_devices.txt")