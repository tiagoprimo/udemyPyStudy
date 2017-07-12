import os

def rename_files(): #function creted
    #(1) get file names from a folder
    file_list = os.listdir("images")
    print(file_list)
    saved_path = os.getcwd()
    print ("Current Working Directory is: "+saved_path)
    os.chdir(r"/Users/tiagoprimo/Google Drive/Primo Backup/Softwares Desenvolvidos/UdemyStudy/udemyPyStudy/images/")
    #(2) for each file, rename the filename
    for file_name in file_list:
        print("Old Name - "+file_name)
        print("New Name - :"+file_name.translate(str.maketrans('', '', '0123456789')))
        os.rename(file_name, file_name.translate(str.maketrans('', '', '0123456789')))
    os.chdir(saved_path)
rename_files() #function called