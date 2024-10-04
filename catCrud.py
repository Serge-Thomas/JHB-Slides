import os

pet_list = []
PET_DATA_FILE = "pet_list.txt"

# Loading the data into the program
if os.path.exists(PET_DATA_FILE):
    with open(PET_DATA_FILE, "r") as file:
        # pet_list = file.readlines()
        for line in file:
            # print(line)
            pet_list.append(line.strip("\n"))
        print("File data has been loaded into list")
        print(pet_list)
else:
    print("The file does exist, please check if in current folder.")

choice = 0

while True:
    # Create a menu that repeats
    print("\nPet Management System")
    print("1. Add a Pet")
    print("2. View a Pet")
    print("3. Update a Pet")
    print("4. Delete Pet")
    print("5. Exit")

    choice = int(input("Choose an option 1 - 5: "))

    if choice == 1:
        pet_name = input("What is the name of your pet: ")
        pet_species = input("Enter your pet species: ")
        pet_age = int(input("Enter your pet's age: "))

        pet_list.append(f"{pet_name}, {pet_species}, {pet_age}")
        print(f"{pet_name} has been added to out system.")

    elif choice == 2:
        # if list == 0 or list == 1
        if pet_list:
            for pet in pet_list:
                pet_n, pet_s, pet_a = pet.split(", ")
                print(f"Pet Name: {pet_n}")
                print(f"Pet Species: {pet_s}")
                print(f"Pet Age: {pet_a}\n")
        else:
            print("There are no pets in the system.")
    elif choice == 3:
        print(pet_list)
        for position, pet in enumerate(pet_list, 1):
            print(pet)
            pet_n, pet_s, pet_a = pet.split(", ")
            print(f"Pet No.: {position}")
            print(f"Pet Name: {pet_n}")
            print(f"Pet Species: {pet_s}")
            print(f"Pet Age: {pet_a}\n")
        # display lists pets
        # for loop check for pet (name, )

        user_pet_pick = int(input("Enter your pet number: \nor enter -1 to return to menu"))

        if user_pet_pick != -1:
            print("Leave blank if you do not want to update value.")
            updated_pet_name = input("What is the updated name of your pet: ")

            print("Enter 0 if not updating")
            updated_pet_age = int(input("Enter updated pet age: "))

            for position, pet in enumerate(pet_list, 1):
                pet_n, pet_s, pet_a = pet.split(", ")
                if position == user_pet_pick:
                    if updated_pet_name != "":
                        pet_list[user_pet_pick - 1] = f"{updated_pet_name}, {pet_s}, {pet_a}"
                    if updated_pet_age != 0:
                        pet_list[user_pet_pick - 1] = f"{pet_n}, {pet_s}, {updated_pet_age}"
        else:
            continue                
    elif choice == 4:
        pass
    elif choice == 5:
        with open(PET_DATA_FILE, "w+") as file:
            for pet in pet_list:
                file.write(f"{pet}\n")
        break
    else:
        print("Invalid option entered please try again.")
