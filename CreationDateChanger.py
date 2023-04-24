import os
import win32api

# Function to change file properties
def change_file_properties(file_path, creation_time=None, author=None, last_modification_time=None):
    # Set the file creation time
    if creation_time is not None:
        os.system('powershell.exe (Get-Item "{}").creationtime=("{}")'.format(file_path, creation_time))
    
    # Set the file author
    if author is not None:
        win32api.SetFileAttributes(file_path, win32api.GetFileAttributes(file_path) & ~win32api.FILE_ATTRIBUTE_READONLY)
        os.system('powershell.exe (Get-Item "{}").author=("{}")'.format(file_path, author))
    
    # Set the file last modification time
    if last_modification_time is not None:
        os.system('powershell.exe (Get-Item "{}").lastwritetime=("{}")'.format(file_path, last_modification_time))

# Main function to prompt user for input and call change_file_properties()
def main():
    file_path = input("Enter the file path: ")
    
    creation_time = input("Enter the new creation time (in the format yyyy-mm-dd HH:MM:SS, or leave blank if not updating): ")
    author = input("Enter the new author name (or leave blank if not updating): ")
    last_modification_time = input("Enter the new last modification time (in the format yyyy-mm-dd HH:MM:SS, or leave blank if not updating): ")
    
    change_file_properties(file_path, creation_time, author, last_modification_time)
    
    print("File properties have been updated.")

if __name__ == '__main__':
    main()
