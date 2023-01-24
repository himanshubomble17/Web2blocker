import os

# Function to block a website
def block_website(website):
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    blocked_website = website + " localhost"
    with open(hosts_path, "r") as file:
        content = file.read()
    if blocked_website in content:
        print("Website is already blocked.")
    else:
        with open(hosts_path, "a") as file:
            file.write("\n" + blocked_website)
        print("Website blocked.")

# Function to unblock a website
def unblock_website(website):
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
    blocked_website = website + " localhost"
    with open(hosts_path, "r") as file:
        content = file.read()
    if blocked_website in content:
        content = content.replace(blocked_website, "")
        with open(hosts_path, "w") as file:
            file.write(content)
        print("Website unblocked.")
    else:
        print("Website is not blocked.")

# Take input from user
website = input("Enter the website to block or unblock: ")

# Take input from user
operation = input("Enter 'block' to block the website or 'unblock' to unblock the website: ")

# Call the appropriate function based on user input
if operation == "block":
    block_website(website)
elif operation == "unblock":
    unblock_website(website)
else:
    print("Invalid operation.")
