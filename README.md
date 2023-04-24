File Properties Editor
File Properties Editor is a command-line program that allows users to update the creation time, author, and last modification time of a file. This program is designed for Windows operating systems and uses the os and win32api modules to modify the file properties.

Installation
There is no installation required for this program. Simply download the Python script file_properties_editor.py and run it in a command prompt or terminal.

Usage
To use this program, follow these steps:

Open a command prompt or terminal window.
Navigate to the directory where the file_properties_editor.py script is saved.
Run the script using the command python file_properties_editor.py.
Enter the file path of the file you wish to update.
Enter the new value for any or all of the following file properties:
Creation time (in the format yyyy-mm-dd HH:MM:SS)
Author name
Last modification time (in the format yyyy-mm-dd HH:MM:SS)
If you do not wish to update a particular file property, leave the field blank when prompted.
Press enter to update the file properties.
The program will display a message indicating that the file properties have been updated.
Note: If you wish to update the author property, you may need to remove the read-only attribute from the file. This program automatically removes the read-only attribute before updating the author property, but if you encounter any issues, you may need to manually remove the attribute.

License
This program is released under the MIT License.

Contributing
If you wish to contribute to this project, please feel free to submit a pull request or open an issue. All contributions are welcome!
