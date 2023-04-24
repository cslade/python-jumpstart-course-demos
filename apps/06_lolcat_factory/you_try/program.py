import os
import shutil
import requests
import subprocess

def main():
# Print Program Header
    header()
    folder = cat_directory()
    
# Create Folder
    cat_directory()
# Download cat imagines 
    get_cat(folder)
    view_files()    


def header():
    print("-------------------------------")
    print("--------Crazy Cats------------")
    print("-------------------------------")
    
    
def cat_directory():
    parent_directory = r"C:\Users\slade\crepo\python-jumpstart-course-demos\python-jumpstart-course-demos\apps\06_lolcat_factory"
    file_folder = "cat_pictures"
    cat_folder = os.path.join(parent_directory, file_folder)
    if not os.path.exists(cat_folder):
        os.mkdir(cat_folder)
    return cat_folder
    

def get_cat_from_url(url):
    response = requests.get(url, stream=True)    
    return response.raw
   
       
def get_cat(folder):
    url = "http://consuming-python-services-api.azurewebsites.net/cats/random"
    data = get_cat_from_url(url)
    nums = [1,2,3,4,5,6,7,8,9]
    for i in nums:
        name = "lolcat_0{}".format(i)
        print("Downloading cat " + name)
        save_files(data, name, folder)
   
    

def save_files(data, name, folder):
    cat_location = os.path.join(folder, name + ".jpg")
    with open(cat_location, "wb") as cf:
        shutil.copyfileobj(data, cf)
        
def view_files():
    folder = cat_directory()
    subprocess.call(["explorer", folder])
             
if __name__ == "__main__":
     main()