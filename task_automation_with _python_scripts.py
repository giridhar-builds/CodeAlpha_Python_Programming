# =====================================================================
# TASK 3: TASK AUTOMATION WITH PYTHON SCRIPTS
# (Selected Idea: Move all .jpg files from a folder to a new folder)
# =====================================================================
import os
import shutil

def automate_file_movement():
    print("=== File Automation Script ===")
    
    # Solicit directory paths from user
    source_dir = input("Enter the path of the source folder: ").strip()
    destination_dir = input("Enter the path of the destination folder: ").strip()
    
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print("Error: The source directory does not exist.")
        return
        
    if not os.path.isdir(source_dir):
        print("Error: The source path provided is not a directory.")
        return

    # Create destination directory if it does not exist yet
    if not os.path.exists(destination_dir):
        try:
            os.makedirs(destination_dir)
            print(f"Created destination directory at: {destination_dir}")
        except Exception as e:
            print(f"Error creating destination directory: {e}")
            return

    moved_count = 0
    error_count = 0

    # Scan and process files
    try:
        files = os.listdir(source_dir)
        
        for file_name in files:
            source_file_path = os.path.join(source_dir, file_name)
            
            # Check if it is a file and has a .jpg or .jpeg extension
            if os.path.isfile(source_file_path) and file_name.lower().endswith(('.jpg', '.jpeg')):
                destination_file_path = os.path.join(destination_dir, file_name)
                
                try:
                    shutil.move(source_file_path, destination_file_path)
                    print(f"Successfully moved: {file_name}")
                    moved_count += 1
                except Exception as file_error:
                    print(f"Failed to move {file_name}. Error: {file_error}")
                    error_count += 1
                    
    except Exception as e:
        print(f"An unexpected error occurred during execution: {e}")
        return

    # Print execution metrics
    print("\n=== Automation Run Summary ===")
    print(f"Total .jpg files moved successfully: {moved_count}")
    if error_count > 0:
        print(f"Total files that encountered errors: {error_count}")
    print("===============================")

if __name__ == "__main__":
    automate_file_movement()
