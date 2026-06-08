members = []

def register_member():

    name = input("Enter member name: ")

    member = {
        "name": name
    }

    members.append(member)

    print("Member registered successfully!")
