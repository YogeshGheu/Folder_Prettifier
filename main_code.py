import os
import time
user_input_path = input("\nEnter the Folder Path Which You Want to Prettify: ")
user_input_important_file = input("\nEnter the File Name Which You want to Skip From all Operations "
                                  "\n(Keep Blank to Skip this Option)..............................:")
user_input_FileFormat = input("\nEnter a File Format(without '.') to Rename all These Type of Files to Rename As: 1 2 3 4 5 ... "
                              "\n(Keep Blank to Skip this Option)..............................................................:")
try:
    def Soldier(path, important_file, format):
        os.chdir(path)
        files = os.listdir()
        number = 0
        for item in files:
            is_dir = str(os.path.isdir(item))
            if is_dir == "True":
                pass
            elif item == important_file:
                pass
            else:
                #print("current file is: ", item)
                split = item.split(".")
                file_format = split[1]
                if file_format == format:
                    number += 1
                    os.renames(item, f"{number}.{file_format}")
                else:
                    file_name = split[0].capitalize()
                    file_name = file_name.capitalize()
                    os.renames(item, f"{file_name}.{file_format}")
        print("\nOperation Copmleted Successfully!")
        time.sleep(1.5)
    Soldier(user_input_path, user_input_important_file, user_input_FileFormat)
except FileNotFoundError:
    print("Path not found, Please Try again !")


