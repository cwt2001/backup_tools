import os
import shutil

def backup_folder(source_folder, destination_folder):
    """
    Copy files the entire source folder to destination folder
    (and do not copy files that have not changed since the last time);
    Keep the destination folder and the source folder synchronized 
    (i.e. delete files and paths that are in the destination folder 
    but are no longer in the source folder)
    """
    try:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                source_path = os.path.join(root, file)
                destination_path = os.path.join(destination_folder, os.path.relpath(source_path, source_folder))
                if not os.path.exists(destination_path) or os.stat(source_path).st_mtime - os.stat(destination_path).st_mtime > 1:
                    shutil.copy2(source_path, destination_path)
                    # print(file+" is copied to destination folder.")

            for dir in dirs:
                dirpath = os.path.join(destination_folder, os.path.relpath(os.path.join(root,dir),source_folder))
                if not os.path.exists(dirpath):
                    os.makedirs(dirpath)
                    # print(dirpath+" is created in destination folder.")
    except Exception as e:
        print("An error occurred during "+source_folder+" backup:", e,"\n")
        print(root)

    try:
        for root, dirs, files in os.walk(destination_folder):
            for file in files:
                destination_path = os.path.join(root, file)
                source_path = os.path.join(source_folder, os.path.relpath(destination_path, destination_folder))
                if not os.path.exists(source_path):
                    os.remove(destination_path)
                    # print(file+" is removed in destination folder.")

            for dir in dirs:
                source_dirpath = os.path.join(source_folder, os.path.relpath(os.path.join(root,dir),destination_folder))
                if not os.path.exists(source_dirpath):
                    dirpath = os.path.join(root,dir)
                    shutil.rmtree(dirpath)
                    # print(dirpath+" is removed in destination folder.")
    except Exception as e:
        print("An error occurred during "+destination_folder+" backup update:", e,"\n")
        print(root)
    print(source_folder+" backup completed.\n")
    
if __name__ == "__main__":
    source_folder = "D:/Files/Research"
    destination_folder = "E:/LaptopBackup/Research"
    backup_folder(source_folder, destination_folder)
    input()

