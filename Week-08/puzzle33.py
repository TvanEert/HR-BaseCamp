guest_list = [
    "Liam",
    "Emma",
    "Noah",
    "Olivia",
    "Lucas",
    "Mila",
    "Floris",
    "Sophie",
    "Levi",
    "Zwaantje",
    "Luuk",
    "Julia",
    "Sem",
    "Eva",
    "Daan",
    "Lynn",
    "Jayden",
    "Tess",
    "Mees",
    "Sara",
    "Lars",
    "Anna",
    "Bram",
    "Nora",
    "Thijs",
    "Fleur",
    "Jesse",
    "Liv",
    "Sam",
    "Noa",
    "Max",
    "Elin",
    "Thomas",
    "Roos",
    "Milan",
    "Nova",
    "Finn",
    "Emily",
    "Adam",
    "Isabella",
    "Daniel",
    "Lara",
    "Gijs",
    "Isabel",
    "Dylan",
    "Nina",
    "Stijn",
    "Evi",
    "Tijn",
    "Lotte"
]

sum_name_length = 0

for person in guest_list:
    friends = []
    for friend in guest_list:
        if not set(person) & set(friend):
            friends.append(friend)
    if len(friends) == 2:
        print(person,"friends: ",friends)
    if "Luuk" in friends and "Roos" in friends:
        sum_name_length += len(person)

print(sum_name_length)