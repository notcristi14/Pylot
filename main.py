import subprocess
import pyautogui
import time
import webbrowser
import datetime
import os
import pyperclip

# --- P R E - P R O M P T ---
# WARNING: This tool directly controls your Windows PC using Python's subprocess, pyautogui, and webbrowser functions.
# The AI will respond with the result of any commands that return a value.
# You can use this information to decide what commands to generate next.
# ---

def execute_command(command):
    """
    Executes a given command on the system.
    """
    try:
        # Use subprocess for direct command execution
        subprocess.Popen(command, shell=True)
        print(f"Successfully executed: {command}")
    except FileNotFoundError:
        print(f"Error: The command '{command}' was not found. Please check the spelling and path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def take_screenshot():
    """
    Captures a screenshot of the entire screen and saves it as a file.
    """
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"screenshot_{timestamp}.png"
        pyautogui.screenshot(filename)
        print(f"Screenshot saved as: {filename}")
    except Exception as e:
        print(f"An error occurred while taking the screenshot: {e}")

def press_key(key):
    """
    Simulates a key press.
    """
    try:
        pyautogui.press(key)
        print(f"Successfully pressed key: {key}")
    except Exception as e:
        print(f"An error occurred while pressing the key: {e}")

def mouse_click(button, x=None, y=None):
    """
    Simulates a mouse click.
    """
    try:
        if x is not None and y is not None:
            pyautogui.click(x=x, y=y, button=button)
            print(f"Successfully clicked {button} button at ({x}, {y})")
        else:
            pyautogui.click(button=button)
            print(f"Successfully clicked {button} button at current position")
    except Exception as e:
        print(f"An error occurred while clicking the mouse: {e}")

def control_volume(action):
    """
    Controls the system volume.
    """
    try:
        if action == 'up':
            pyautogui.press('volumeup')
            print("Volume increased.")
        elif action == 'down':
            pyautogui.press('volumedown')
            print("Volume decreased.")
        else:
            print("Invalid volume action. Please use 'up' or 'down'.")
    except Exception as e:
        print(f"An error occurred while controlling volume: {e}")

def open_and_screenshot(url):
    """
    Opens a URL and then takes a screenshot after a delay.
    """
    try:
        print(f"Opening URL: {url}")
        webbrowser.open(url)
        time.sleep(5)  # Wait for the page to load
        take_screenshot()
    except Exception as e:
        print(f"An error occurred during the complex command: {e}")

def manage_window(action):
    """
    Controls the active window (maximize, minimize, close).
    """
    try:
        if action == 'maximize':
            pyautogui.hotkey('win', 'up')
            print("Active window maximized.")
        elif action == 'minimize':
            pyautogui.hotkey('win', 'down')
            print("Active window minimized.")
        elif action == 'close':
            pyautogui.hotkey('alt', 'f4')
            print("Active window closed.")
        else:
            print("Invalid window action. Please use 'maximize', 'minimize', or 'close'.")
    except Exception as e:
        print(f"An error occurred while managing the window: {e}")

def type_text(text):
    """
    Simulates typing a string of text.
    """
    try:
        pyautogui.write(text, interval=0.1)
        print("Text typed successfully.")
    except Exception as e:
        print(f"An error occurred while typing text: {e}")

def copy_to_clipboard(text):
    """
    Copies text to the clipboard.
    """
    try:
        pyperclip.copy(text)
        print("Text copied to clipboard.")
    except Exception as e:
        print(f"An error occurred while copying to clipboard: {e}")

def paste_from_clipboard():
    """
    Pastes text from the clipboard.
    """
    try:
        text = pyperclip.paste()
        pyautogui.write(text)
        print("Pasted from clipboard.")
    except Exception as e:
        print(f"An error occurred while pasting from clipboard: {e}")

def create_file(file_path):
    """
    Creates an empty file.
    """
    try:
        with open(file_path, 'w') as f:
            print(f"File created successfully at: {file_path}")
    except Exception as e:
        print(f"An error occurred while creating the file: {e}")

def delete_file(file_path):
    """
    Deletes a specified file.
    """
    try:
        os.remove(file_path)
        print(f"File deleted successfully at: {file_path}")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred while deleting the file: {e}")

def rename_file(old_path, new_path):
    """
    Renames a file.
    """
    try:
        os.rename(old_path, new_path)
        print(f"File '{old_path}' renamed to '{new_path}' successfully.")
    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred while renaming the file: {e}")

def system_control(action):
    """
    Shuts down or restarts the system.
    """
    try:
        if action == 'shutdown':
            subprocess.Popen('shutdown /s /t 1', shell=True)
            print("System is shutting down.")
        elif action == 'restart':
            subprocess.Popen('shutdown /r /t 1', shell=True)
            print("System is restarting.")
        else:
            print("Invalid system action. Please use 'shutdown' or 'restart'.")
    except Exception as e:
        print(f"An error occurred while controlling the system: {e}")

def wait(seconds):
    """
    Pauses the script for a specified number of seconds.
    """
    try:
        seconds = float(seconds)
        print(f"Pausing for {seconds} seconds...")
        time.sleep(seconds)
        print("Pause finished.")
    except ValueError:
        print("Invalid number of seconds. Please enter a numerical value.")
    except Exception as e:
        print(f"An error occurred during the wait command: {e}")

def kill_process(process_name):
    """
    Terminates a process by name on Windows.
    """
    try:
        subprocess.Popen(f'taskkill /f /im {process_name}', shell=True)
        print(f"Attempting to kill process: {process_name}")
    except Exception as e:
        print(f"An error occurred while trying to kill the process: {e}")

def calculate(expression):
    """
    Opens the PC calculator, types a mathematical expression, and hits enter.
    """
    try:
        subprocess.Popen('calc.exe')
        time.sleep(2)  # Wait for the calculator to open
        pyautogui.write(expression)
        pyautogui.press('enter')
        print(f"Sent expression '{expression}' to Calculator.")
    except Exception as e:
        print(f"An error occurred while trying to use the calculator: {e}")

def get_screen_size():
    """
    Prints the screen resolution.
    """
    try:
        width, height = pyautogui.size()
        print(f"Screen resolution: {width}x{height}")
    except Exception as e:
        print(f"An error occurred while getting screen size: {e}")

def show_time():
    """
    Prints the current system time.
    """
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current system time: {current_time}")

def move_mouse(x, y):
    """
    Moves the mouse cursor to a specific coordinate.
    """
    try:
        pyautogui.moveTo(x, y)
        print(f"Mouse moved to ({x}, {y}).")
    except Exception as e:
        print(f"An error occurred while moving the mouse: {e}")

def send_hotkey(*keys):
    """
    Simulates a keyboard hotkey combination.
    """
    try:
        pyautogui.hotkey(*keys)
        print(f"Hotkey {keys} pressed successfully.")
    except Exception as e:
        print(f"An error occurred while pressing the hotkey: {e}")

def open_path(path):
    """
    Opens a file or folder using the default application.
    """
    try:
        os.startfile(path)
        print(f"Successfully opened path: {path}")
    except FileNotFoundError:
        print(f"Error: The path '{path}' was not found.")
    except Exception as e:
        print(f"An error occurred while opening the path: {e}")

def list_files(path):
    """
    Lists all files and directories in a given path.
    """
    try:
        files = os.listdir(path)
        print(f"Files and directories in '{path}':")
        for item in files:
            print(f"- {item}")
    except FileNotFoundError:
        print(f"Error: The path '{path}' was not found.")
    except Exception as e:
        print(f"An error occurred while listing files: {e}")

def list_processes():
    """
    Lists all running processes on the system.
    """
    try:
        output = subprocess.run(['tasklist'], capture_output=True, text=True, check=True)
        print("Running processes:")
        print(output.stdout)
    except FileNotFoundError:
        print("Error: 'tasklist' command not found. This command is available on Windows systems.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running tasklist: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_display_info():
    """
    Prints information about connected monitors, including name and refresh rate.
    Note: This command is designed for Windows and may not work on other operating systems.
    """
    try:
        # Use WMIC command to get display info on Windows
        command = 'wmic path Win32_VideoController get Name,CurrentRefreshRate,DriverVersion'
        output = subprocess.run(command.split(), capture_output=True, text=True, check=True)
        lines = output.stdout.strip().split('\n')
        
        # Parse the output
        if len(lines) > 1:
            headers = lines[0].split()
            data_lines = lines[1:]
            
            print(f"Found {len(data_lines)} display(s) connected:")
            for line in data_lines:
                # Split the line by a variable number of spaces
                parts = line.strip().split()
                if len(parts) >= 2:
                    name = ' '.join(parts[:-2])
                    refresh_rate = parts[-2]
                    driver_version = parts[-1]
                    print(f" - Name: {name}, Max Refresh Rate: {refresh_rate} Hz, Driver Version: {driver_version}")
        else:
            print("No display information found.")
    except FileNotFoundError:
        print("Error: 'wmic' command not found. This command is available on Windows systems.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running wmic: {e.stderr}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    while True:
        user_command = input("What command do you want to execute? (e.g., 'start chrome.exe', 'open https://www.google.com', 'screenshot', 'press enter', 'click left 100 200', 'volume up', 'window maximize', 'type hello world', 'copy my_text', 'paste', 'wait 5', 'calculate 2+2', 'get_screen_size', 'show_time', 'kill notepad.exe', 'create_file C:\\test.txt', 'rename_file old.txt new.txt', 'system shutdown', 'move_mouse 100 200', 'hotkey ctrl shift s', 'open_path C:\\Users', 'list_files C:\\', 'list_processes', 'get_displays', or 'exit' to quit): ")

        if user_command.lower() == 'exit':
            print("Exiting the control tool.")
            break
        
        # Confirmation prompt
        proceed = input(f"Do you want to proceed with executing '{user_command}'? (y/n): ")
        if proceed.lower() == 'y':
            print(f"Executing: {user_command}")
            
            command_parts = user_command.split(' ', 1)
            action = command_parts[0].lower()
            
            if action == 'screenshot':
                take_screenshot()
            elif action == 'paste':
                paste_from_clipboard()
            elif action == 'get_screen_size':
                get_screen_size()
            elif action == 'show_time':
                show_time()
            elif action == 'list_processes':
                list_processes()
            elif action == 'get_displays':
                get_display_info()
            elif len(command_parts) > 1:
                argument = command_parts[1]
                
                if action == 'start':
                    execute_command(argument)
                elif action == 'open':
                    # Check if it's a folder or URL
                    if argument.lower().startswith('http://') or argument.lower().startswith('https://'):
                        webbrowser.open(argument)
                    else:
                        execute_command(f'explorer "{argument}"')
                elif action == 'press':
                    press_key(argument)
                elif action == 'click':
                    click_parts = argument.split(' ')
                    button = click_parts[0].lower()
                    x, y = None, None
                    if len(click_parts) > 2:
                        try:
                            x = int(click_parts[1])
                            y = int(click_parts[2])
                        except ValueError:
                            print("Invalid coordinates. Please use 'click [left/right] [x] [y]'.")
                            continue
                    mouse_click(button, x, y)
                elif action == 'volume':
                    control_volume(argument.lower())
                elif action == 'window':
                    manage_window(argument.lower())
                elif action == 'type':
                    type_text(argument)
                elif action == 'copy':
                    copy_to_clipboard(argument)
                elif action == 'wait':
                    wait(argument)
                elif action == 'calculate':
                    calculate(argument)
                elif action == 'kill':
                    kill_process(argument)
                elif action == 'create_file':
                    create_file(argument)
                elif action == 'delete_file':
                    delete_file(argument)
                elif action == 'rename_file':
                    rename_parts = argument.split(' ', 1)
                    if len(rename_parts) > 1:
                        rename_file(rename_parts[0], rename_parts[1])
                    else:
                        print("Invalid rename command. Please use 'rename_file [old_path] [new_path]'.")
                elif action == 'system':
                    system_control(argument.lower())
                elif action == 'open_and_screenshot':
                    open_and_screenshot(argument)
                elif action == 'move_mouse':
                    coords = argument.split(' ')
                    if len(coords) == 2:
                        try:
                            x = int(coords[0])
                            y = int(coords[1])
                            move_mouse(x, y)
                        except ValueError:
                            print("Invalid coordinates. Please use 'move_mouse [x] [y]'.")
                    else:
                        print("Invalid move_mouse command. Please use 'move_mouse [x] [y]'.")
                elif action == 'hotkey':
                    keys = argument.split(' ')
                    send_hotkey(*keys)
                elif action == 'open_path':
                    open_path(argument)
                elif action == 'list_files':
                    list_files(argument)
                else:
                    print(f"Unknown command: '{action}'.")
            else:
                print("Command not recognized. Please provide a command and an argument.")
        else:
            print("Command execution cancelled.")
        
        time.sleep(1) # Give the user a moment to see the output

if __name__ == "__main__":
    main()
