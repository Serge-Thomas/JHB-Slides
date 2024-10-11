poke_dict = {}

def data_load():
    with open("poke.txt", "r") as file:
        file_content = file.readlines()
        # print(file_content)
        for poke in file_content:
            file_content_split = poke.strip("\n").split(", ")
            poke_dict[file_content_split[0]] = [file_content_split[1], file_content_split[2], file_content_split[3]]


def change_stats():
    poke_name = input("Enter pokemon name: ").lower()
    if poke_name in poke_dict:
        poke_new_stat = int(input("Enter new poke stat: "))
        poke_dict[poke_name][0] = poke_new_stat
        print(f"{poke_name} is now at a level {poke_dict[poke_name][0]}")
    else:
        print("Pokemon does not exist.")


def update_to_file():
    with open("poke.txt", "w+") as file:
        for key, value in poke_dict.items():
            file.write(f"{key}, {value[0]}, {value[1]}, {value[2]}\n")
        print("File has been updated Successfully!")
      

data_load()
# print(poke_dict)        

while True:
    print("1. Change stats")
    print("2. Change type")
    print("3. Change personality")
    print("4. Exit")
    
    user_option = input("Enter option: ")
    
    if user_option == "1":
        change_stats()
    elif user_option == "2":
        pass
    elif user_option == "3":
        pass
    elif user_option == "4":
        update_to_file()
        print("Byeeeeeeeeee")
        break
    else:
        print("Incorrect option entered.")
        