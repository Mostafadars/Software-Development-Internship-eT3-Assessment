import os

def organize_folder(folder_path: str):
    folder_contents = os.listdir(folder_path)

    # files extensions
    image_extensions = ['.png', '.jpg', '.jpeg']
    video_extensions = ['.mp4', '.mkv', '.mov', '.wav']
    audio_extensions = ['.mp3', '.m4a']
    document_extensions = ['.pdf', '.txt', '.xlsx', '.docx', '.md']

    summary = {
        "Images": 0,
        "Videos": 0,
        "Audio": 0,
        "Documents": 0,
        "Others": 0
    }

    # Split the files on the folder path with file extension
    for file in folder_contents:
        extension = os.path.splitext(file)[1].lower()

        if extension == '':
            continue  # that means skip the existing folders and didn't do anything
        elif extension in image_extensions:
            target_folder = os.path.join(folder_path, 'Images')
            os.makedirs(target_folder, exist_ok=True)
            os.rename(os.path.join(folder_path, file), os.path.join(target_folder, file))
            summary["Images"] += 1
        elif extension in video_extensions:
            target_folder = os.path.join(folder_path, 'Videos')
            os.makedirs(target_folder, exist_ok=True)
            os.rename(os.path.join(folder_path, file), os.path.join(target_folder, file))
            summary["Videos"] += 1
        elif extension in audio_extensions:
            target_folder = os.path.join(folder_path, 'Audio')
            os.makedirs(target_folder, exist_ok=True)
            os.rename(os.path.join(folder_path, file), os.path.join(target_folder, file))
            summary["Audio"] += 1
        elif extension in document_extensions:
            target_folder = os.path.join(folder_path, 'Documents')
            os.makedirs(target_folder, exist_ok=True)
            os.rename(os.path.join(folder_path, file), os.path.join(target_folder, file))
            summary["Documents"] += 1
        else:
            target_folder = os.path.join(folder_path, 'Others')
            os.makedirs(target_folder, exist_ok=True)
            os.rename(os.path.join(folder_path, file), os.path.join(target_folder, file))
            summary["Others"] += 1

    for category, count in summary.items():
        print(f"Category: {category} - Number of files: {count}")


if __name__ == "__main__":
    file_path = str(input("Enter the folder path to organize: "))

    finish_correct = organize_folder(file_path)

    print("The Folder is Successfully Organized.")