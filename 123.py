import os
import shutil
import time as t

root_path = "C:/Users/home/Desktop/dhanya's folder"
folders_path = os.path.join(root_path, "Folders")
images_path = os.path.join(root_path, "Images")
videos_path = os.path.join(root_path, "Videos")

files = os.listdir(root_path)

folders = []
images = []
videos = []

for file in files:
    name, extension = os.path.splitext(file)

    if extension == '':
        folders.append(file)
    elif extension in ['.png', '.jpg', '.jpeg', '.tiff']:
        images.append(file)
    elif extension in ['.mp3', '.mp4', '.avi']:
        videos.append(file)

def move_files(file_list, destination_path):
    if not os.path.exists(destination_path):
        print(f"Creating destination {destination_path}...")
        os.mkdir(destination_path)
    
    for file in file_list:
        pfrom = os.path.join(root_path, file)
        pto = os.path.join(destination_path, file)
        print(f"Moving {file} to its destination...")
        t.sleep(2)  # wait for 2 seconds
        shutil.move(pfrom, pto)
        print(f"{file} successfully moved!")

move_files(folders, folders_path)
move_files(images, images_path)
move_files(videos, videos_path)