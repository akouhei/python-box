import mkfolders


folders = mkfolders.read_csv(r"./folder_list.csv")
print(folders)

mkfolders.mkfolders("./", r"./folder_list.csv")
