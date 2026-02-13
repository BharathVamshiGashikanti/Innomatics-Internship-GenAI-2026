# List of system log messages
logs = ["INFO", "ERROR", "WARNING", "ERROR"]

# Initialize a counter for ERROR messages
error_count = 0

# Loop through each log entry
for log in logs:
    # Check if the log entry is "ERROR"
    if log == "ERROR":
        error_count += 1  # Increase error counter

# Print the total number of ERROR messages
print("Total number of ERROR entries:", error_count)
