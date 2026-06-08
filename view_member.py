from register_member import members

def view_members():

    if not members:
        print("No members found.")
        return

    print("\nMEMBER LIST")

    for index, member in enumerate(members, start=1):
        print(f"{index}. {member['name']}")
