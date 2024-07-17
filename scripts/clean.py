# clean.py removes all .gitkeep files used as placeholders
import os


def get_parent_directory():
    current_directory = os.getcwd()
    if os.path.basename(current_directory) == 'scripts':
        parent_directory = os.path.dirname(current_directory)
        return parent_directory
    else:
        print("Not in the `scripts` directory, please cd to scripts!!!")
        exit()


def remove_gitkeep_files(directory):
    counter = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file == ".gitkeep":
                file_path = os.path.join(root, file)
                os.remove(file_path)
                counter += 1
    print(f'Removed {counter} .gitkeep files from {directory}.')

def main():
    dir = get_parent_directory()
    print(f"Cleaning the {dir} directory.")
    remove_gitkeep_files(dir)
    print(f"{dir} is clean!")

if __name__ == "__main__":
    main()