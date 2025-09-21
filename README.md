# Pylot: A Python PC Control Tool

Pylot is a command-line tool written in Python that allows you to control your computer's mouse, keyboard, and system with simple, text-based commands. It's a fun and practical project for learning about system automation and the capabilities of Python libraries like `pyautogui` and `subprocess`.

# Features

Pylot is packed with a wide range of functionalities to give you command-line control over your PC:

- # System Actions: Shutdown or restart your computer.

- # Window Management: Maximize, minimize, or close the active window.

- # File & Folder Operations: Create, delete, rename, and list files and folders.

- # Process Control: Start a program or terminate a running process by name.

- # Clipboard: Copy text to the clipboard and paste its contents.

- # Mouse Control: Move the mouse, simulate clicks, and control the scroll wheel.

- # Keyboard Automation: Type text, press individual keys, or use complex hotkey combinations (e.g., ctrl alt del).

- # Volume Control: Adjust system volume up or down.

- # Timed Commands: Pause the script for a specified duration to create automation sequences.

- # Information Retrieval: Get the current system time and screen resolution.

- # Web Automation: Open a URL and take a screenshot after a delay.

   1. Installation

  #  This tool requires Python and a few external libraries.   #

   2.  Clone this repositor:

     `git clone [https://github.com/notcristi14/Pylot.git](https://github.com/notcristi14/Pylot.git)
     cd Pylot`

 

  #  3. Install dependencies:  #

   `pip install pyautogui
    pip install pyperclip`

#  4. Usage  #

   Run the script from your terminal and enter commands when prompted.

   `python main.py`
                
   

#  5.   Avaliable Commands  #

   #  Command                 Syntax                                    Description    


                                                                         
   `start`                    `start [program_name]`                     Executes a program (e.g., `start chrome.exe`).

   `open`                  `open [url/path]`                             Opens a URL in your default browser or a folder/file.  

   `open_and_screenshot`   `open_and_screenshot [url]`                   Opens a URL, waits 5 seconds, and takes a screenshot.  

   `window`                `window [maximize/minimize/close]`            Manages the active window.  

   `type`                  `type [text]`                                 Types a string of text.  

   `press`                 `press [key]`                                 Simulates a single key press (e.g., `enter`, `space`).  

   `hotkey`                `hotkey [key1] [key2]...`                     Simulates a key combination (e.g., `hotkey ctrl c`).  

   `move_mouse`            `move_mouse [x] [y]`                          Moves the cursor to the specified coordinates.  
   
   `click`                 `click [left/right] [x] [y]`                  Clicks the mouse at the given coordinates.  

   `volume`                `volume [up/down]`                            Controls the system volume.  

   `wait`                  `wait [seconds]`                              Pauses the script for a specified time.  

   `calculate`             `calculate [expression]`                      Opens the Calculator app and solves the expression.  

   `copy`                  `copy [text]`                                 Copies the provided text to the clipboard.  

   `paste`                 `paste`                                       Pastes text from the clipboard.  

   `create_file`           `create_file [path]`                          Creates a new, empty file.  

   `delete_file`           `delete_file [path]`                          Deletes a file.  

   `rename_file`           `rename_file [old_path] [new_path]`           Renames a file.  

   `list_files`            `list_files [path]`                           Lists files and folders in a directory.  
  
   `kill`                  `kill [process_name]`                         Terminates a process (e.g., kill notepad.exe).  

   `list_processes`       `list_processes`                               Displays a list of all running processes.  

   `get_screen_size`      `get_screen_size`                              Shows your screen resolution.  
   
   `show_time`            `show_time`                                    Displays the current system time.  

   `system`               `system [shutdown/restart]`                    Shuts down or restarts the system.  

   `screenshot`           `screenshot`                                   Takes a screenshot and saves it as a PNG file.  

   `get_displays`        `get_displays`                                  Shows information about connected monitors (name, refresh rate, etc.).

   `exit`                 `exit`                                         Quits the application.  
   



#  6.  ⚠️ Important Disclaimer ⚠️ #

   This tool gives you direct control over your computer. Please be careful when using it. The `system shutdown`, `system restart`, and `kill` commands will take immediate action on your PC. Use at your own risk.



#  7.   License #

   This project is licensed under the MIT License.



#  8.  Contributing  #

  Contributions are welcome! If you have an idea for a new command or a bug fix, feel free to open an issue or submit a pull request.
