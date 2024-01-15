import os
import shutil

def move_and_arrange(desk_path, inp1, inp2):
    # Join the folder name with desktop path
    dst_path = os.path.join(desk_path, inp1)

    # Make desktop the default directory
    # and make a list of all its contents
    src_dst = os.chdir(desk_path)
    lst = os.listdir()

    # Loop through the list and move the files
    for file in lst:
        if file.endswith(inp2):
            file_path = os.path.join(desk_path, file)
            if not os.path.exists(os.path.join(dst_path, file)):
                print(f"Moving {file} to {dst_path}")
                shutil.move(file_path, dst_path)
            else:
                print(f"File {file} already exists in {dst_path}")

    # Ask for user permission to auto-arrange the desktop
    user_input = input('Do you want to auto-arrange the desktop? (yes/no): ').lower()
    if user_input == 'yes':
        auto_arrange(desk_path)

def auto_arrange(desk_path):
    # Create standard folders if they don't exist
    standard_folders = ['Documents', 'Images', 'Videos']
    for folder in standard_folders:
        folder_path = os.path.join(desk_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Move files to appropriate folders
    for file in os.listdir(desk_path):
        file_path = os.path.join(desk_path, file)
        if os.path.isfile(file_path):
            category = get_file_category(file)
            if category:
                category_path = os.path.join(desk_path, category)

                # Handle the case where a file with the same name already exists
                count = 1
                new_file_path = os.path.join(category_path, file)
                while os.path.exists(new_file_path):
                    base_name, extension = os.path.splitext(file)
                    new_file_path = os.path.join(category_path, f"{base_name}_{count}{extension}")
                    count += 1

                print(f"Moving {file} to {new_file_path}")
                shutil.move(file_path, new_file_path)

def get_file_category(file_name):
    # Customize this function based on your file categorization logic
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    video_extensions = ['.mp4', '.avi', '.mkv', '.mov']
    document_extensions = ['.txt', '.docx', '.pdf', '.xlsx']

    ext = os.path.splitext(file_name)[1].lower()

    if ext in image_extensions:
        return 'Images'
    elif ext in video_extensions:
        return 'Videos'
    elif ext in document_extensions:
        return 'Documents'
    else:
        pass

# Collect user's input
inp1 = input('Enter the destination folder -- ')
inp2 = input('Enter the file format -- ')
desk_path = r"C:\users\this pc\desktop"

# Move and arrange files
move_and_arrange(desk_path, inp1, inp2)
