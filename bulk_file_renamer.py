import os

def rename_files_in_directory(directory_path, new_prefix):
    try:
        # Change the current working directory to the specified path
        os.chdir(directory_path)

        # Get the list of files in the directory
        files = os.listdir()

        # Iterate through each file and rename it with a new prefix
        for index, file_name in enumerate(files):
            file_extension = os.path.splitext(file_name)[1]  # Get the file extension
            new_name = f"{new_prefix}_{index + 1}{file_extension}"

            # Rename the file
            os.rename(file_name, new_name)

            print(f"Renamed: {file_name} -> {new_name}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace 'DIRECTORY_PATH' with the path of the directory containing the files
    directory_path = 'DIRECTORY_PATH'

    # Replace 'NEW_PREFIX' with the new prefix you want for the files
    new_prefix = 'NEW_PREFIX'

    rename_files_in_directory(directory_path, new_prefix)
