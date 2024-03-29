import os
import shutil

def organize_files(directory, destination_directory=None, skip_duplicates=True):
    if destination_directory is None:
        destination_directory = directory
    
    # Create a dictionary to store file extensions and their corresponding directories
    extensions = {}
    
    # Iterate through all files and directories in the directory
    for root, _, files in os.walk(directory):
        for filename in files:
            # Get the full path of the file
            file_path = os.path.join(root, filename)
            
            # Get the file extension
            extension = filename.split('.')[-1]
            
            # Check if extension already exists in the dictionary
            if extension not in extensions:
                # Create a new directory for the extension
                os.makedirs(os.path.join(destination_directory, extension), exist_ok=True)
                
                # Store the extension-directory mapping
                extensions[extension] = os.path.join(destination_directory, extension)
            
            # Determine the destination directory for the file
            dest_dir = extensions[extension]
            
            # Check for duplicate files
            if skip_duplicates and os.path.exists(os.path.join(dest_dir, filename)):
                print(f"Skipping duplicate file: {file_path}")
                continue
            
            # Move the file to the appropriate directory
            shutil.move(file_path, os.path.join(dest_dir, filename))

if __name__ == "__main__":
    # Specify the directory to organize
    directory_to_organize = input("Enter the directory to organize: ")
    
    # Specify the destination directory (optional, default is the same as the source directory)
    destination_directory = input("Enter the destination directory (press Enter to use the same as source): ").strip()
    
    # Convert empty input to None
    destination_directory = destination_directory or None
    
    # Organize files in the specified directory
    organize_files(directory_to_organize, destination_directory)
    
    print("Files organized successfully!")