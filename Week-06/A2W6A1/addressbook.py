import os
import sys
import json


def display(addressbook: list):
    for address in addressbook:
        emails = str(address.get('emails')).strip("[]").replace("'", "")
        phone_numbers = str(address.get('phone_numbers')).strip("[]").replace("'", "")
        print("======================================")
        print(f"Position: {address.get('id')}\nFirst name: {address.get('first_name')}",
              f"\nLast name: {address.get('last_name')}")
        print(f"Emails: {emails}\nPhone numbers: {phone_numbers}")


def list_contacts(addressbook: list):
    print("Sort options are first_name and last_name if left blank contacts will be unsorted.")
    sort = input("Sort by: ")
    if sort == "first_name" or sort == "last_name":
        addressbook.sort(key=lambda x: x[sort])

    return addressbook


def add_contact(addressbook, filename):
    first_name = input("First name: ")
    last_name = input("Last name: ")
    print("Emails and phone numbers should be separated by ,")
    emails = input("Emails: ").split(",")
    phone_numbers = input("Phone numbers:").split(",")
    if len(addressbook) == 0:
        contact_id = 1
    else:
        contact_id = max(contact["id"] for contact in addressbook) + 1
    contact = {
        "id": contact_id,
        "first_name": first_name,
        "last_name": last_name,
        "emails": emails,
        "phone_numbers": phone_numbers
    }
    addressbook.append(contact)
    write_to_json(filename, addressbook)


def remove_contact(id, addressbook, filename):
    # todo: implement this function
    for contact in addressbook:
        if contact['id'] == int(id):
            print(contact['id'])
            addressbook.remove(contact)
            break

    write_to_json(filename, addressbook)


def merge_contacts(addressbook, filename):
    duplicates = []

    for contact_main in addressbook:
        if not any(contact_main["id"] in duplicate for duplicate in duplicates):
            for contact_dupelicate in addressbook:
                if contact_main["first_name"] == contact_dupelicate["first_name"] and \
                   contact_main["id"] != contact_dupelicate["id"]:
                    if contact_main["last_name"] == contact_dupelicate["last_name"] and \
                       contact_main["id"] != contact_dupelicate["id"]:
                        duplicates.append([contact_main["id"], contact_dupelicate["id"]])

    for duplicate in duplicates:
        for contact in addressbook:
            if contact['id'] == duplicate[0]:
                main_contact = contact
            elif contact['id'] == duplicate[1]:
                duplicate_contact = contact
                for email in duplicate_contact["emails"]:
                    if email not in main_contact["emails"]:
                        main_contact["emails"].append(email)
                for phone_number in duplicate_contact["phone_numbers"]:
                    if phone_number not in main_contact["phone_numbers"]:
                        main_contact["phone_numbers"].append(phone_number)
                remove_contact(duplicate[1], addressbook, filename)
                break
    write_to_json(filename, addressbook)


def read_from_json(filename) -> list:
    addressbook = list()
    # read file
    with open(os.path.join(sys.path[0], filename)) as outfile:
        json_data = json.load(outfile)
        # iterate over each line in data and call the add function
        for contact in json_data:
            addressbook.append(contact)

    return addressbook


def write_to_json(filename, addressbook: list) -> None:
    json_object = json.dumps(addressbook, indent=4)

    with open(os.path.join(sys.path[0], filename), "w") as outfile:
        outfile.write(json_object)


def main(json_file):
    addressbook = read_from_json(json_file)
    running = True

    while running:
        print("\n [L] List contacts\n",
              "[A] Add contact\n",
              "[R] Remove contact\n",
              "[M] Merge contacts\n",
              "[Q] Quit program\n")
        operation_call = input("Select your operation: ").lower()
        if operation_call == "l":
            display(addressbook)
        elif operation_call == "a":
            add_contact(addressbook, json_file)
        elif operation_call == "r":
            contact_id = input("What is the ID of the contact you want to remove: ")
            remove_contact(contact_id, addressbook, json_file)
        elif operation_call == "m":
            merge_contacts(addressbook, json_file)
        elif operation_call == "q":
            running = False
        else:
            print("\ninput error")


if __name__ == "__main__":
    main('contacts.json')
