import getpass as gp
import os
from pathlib import Path

def test_hi():
    print('hi')

def save(file_name,contents):
    # Open a file in write mode ('w')
    file_string = f'{os.path.dirname(os.path.abspath(__file__))}{file_name}.txt'
    file = Path(file_string)

    user_dir = Path("C:/Users") / gp.getuser() / "pythonsavedata"

    # Get the directory of the current file
    current_dir = Path(__file__).parent

    # Build full path
    file_path = user_dir / current_dir.relative_to(current_dir.anchor) / f"{file_name}.txt"
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with open(file_path, "w") as file:
        file.write(contents)

def load(python_script_path,file_name):
    user_dir = Path("C:/Users") / gp.getuser() / "pythonsavedata"
    txt_file = Path(file_name + '.txt')
    current_dir = Path(__file__).parent
    if python_script_path == True:
        build = user_dir / current_dir.relative_to(current_dir.anchor) / txt_file
        
        try:
            with open(build, 'r') as file:
                return(file.read())
        except Exception as e:
            return f"Couldn't get file {build}; Error : {e}"

    script_path = Path(python_script_path)

    if script_path.suffix:
        build = Path(user_dir) / script_path.parent / txt_file
    else:
        build = Path(user_dir) / script_path / txt_file
    
    try:
        with open(build, 'r') as file:
            return(file.read())
    except Exception as e:
        return f"Couldn't get file {build}; Error : {e}"