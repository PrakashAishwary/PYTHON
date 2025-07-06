import subprocess

# List of users to create
users = ["name-1", "name-2", "name-3", "name-4"]

def create_user(username):
    try:
        # Run the useradd command
        subprocess.run(["sudo", "useradd", username], check=True)
        print(f"User '{username}' created successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to create user '{username}'. (Maybe already exists?)")
    except Exception as e:
        print(f"Error creating user '{username}': {e}")

# Loop through the list and create users
for user in users:
    create_user(user)

## Note: check=True will raise error by calling subprocess.CalledProcessError if user does not exist otherwise without it, it will not fail or stop or complain if useradd fails

## Add on feature: if user names are in a file:

with open("users.txt", "r") as file:
    users = [line.strip() for line in file if line.strip()]
for user in users:
    create_user(user)
    