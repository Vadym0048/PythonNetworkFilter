failed_attempts = {}

with open("auth.log", "r") as file:
    for line in file:
        time, ip, status = line.split()

        if status == "FAILED":
            if ip not in failed_attempts:
                failed_attempts[ip] = 0

            failed_attempts[ip] += 1

with open("suspicious_ips.txt", "w") as file:
    for ip, count in failed_attempts.items():
        if count >= 3:
            file.write(f"{ip}: {count} FAILED attempts\n")

print("Suspicious IP analysis completed!")
print("Results saved to suspicious_ips.txt")