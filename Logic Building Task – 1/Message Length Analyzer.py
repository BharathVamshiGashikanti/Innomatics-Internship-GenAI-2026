# List of messages
messages = ["Hi", "Welcome to the platform", "OK"]

# Loop through each message
for message in messages:
    # Calculate the length of the message
    length = len(message)
    
    # Print the message and its length
    print("Message:", message)
    print("Length:", length)
    
    # Check if the message is longer than 10 characters
    if length > 10:
        print("Status: Long message (more than 10 characters)")
    else:
        print("Status: Short message")
    
    print()  # Blank line for better readability
