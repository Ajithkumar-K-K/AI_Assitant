import keyboard  # Import the keyboard module
import os
import sys
import importlib.util

def import_main():
    try:
        if getattr(sys, 'frozen', False):
            # If the application is run as a bundle, use sys._MEIPASS
            script_dir = sys._MEIPASS
        else:
            # If running as a script, use the script's directory
            script_dir = os.path.dirname(os.path.abspath(__file__))
        
        main_path = os.path.join(script_dir, 'main.py')
        spec = importlib.util.spec_from_file_location("main", main_path)
        main_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(main_module)
        
        if hasattr(main_module, 'main'):
            return main_module.main
        else:
            return None
    except Exception as e:
        return None

run_main_program = import_main()

def run_program():
    if run_main_program:
        try:
            run_main_program()
        except Exception as e:
            pass  # Handle the error as needed
    else:
        pass  # Handle the case where the main function could not be imported

keyboard.add_hotkey('tab + h', run_program)  # Add hotkey for running the program
keyboard.wait('tab + x')  # Wait for the exit hotkey to be pressed
