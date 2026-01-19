import os
folder_path = r"C:\Users\ubkk\OneDrive\Documents\python-mastery\beginner\Exercise 7"

files = os.listdir(folder_path)                    #get all the files in the folder
file_count = {}                                                                                              #dict to store count of each file type

for file in files:
    name, extension = os.path.splitext(file)                                                          #spilt filename and extension 
    
    if extension == "":                                 #skip folder or file without extension
        continue

#Initialze count for new extension
    if extension not in file_count:
        file_count[extension] = 1
    else:
        file_count[extension]  += 1
    
    new_name = f"{file_count[extension]}{extension}"              #create new file name


    #full old and new paths
    old_path = os.path.join(folder_path, file)
    new_path = os.path.join(folder_path, new_name)

    os.rename(old_path, new_path)                       #rename the file

print("Folder clean sucessfully")

# ------------Harry's Code--------------------
# import os

# files = os.listdir("clutteredfolder")
# i = 1
# for file in files:
#     if file.endswith(".png"):
#         print(file)
#         os.rename(f"clutteredFolder/{file}", f"clutteredFolder/{i}.png")
#         i = i + 1