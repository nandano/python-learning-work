def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)

messages = ["hey there", "good morning", "Hello, how are you?", "I'm fine"]
empty_list = []

send_messages(messages, empty_list)

print(messages)
print(empty_list)