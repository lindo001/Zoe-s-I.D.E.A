import os
def install():
    available_attempts:int = 10
    current_dir = working_dir = os.getcwd()
    while True:
        if available_attempts ==0:
            print("failed to locate bin folder")
            break
        if current_dir == "/": 
            os.chdir("bin")
            install_script(working_dir)
            break
   
        current_dir = os.path.dirname(current_dir)
        os.chdir(current_dir)
        available_attempts-=1
        
def install_script(working_dir):
    script_path = os.path.join(working_dir, "main.py")
    delete_file = os.path.join(working_dir,"installation.py")
    with open("zoe", "w") as f:
        f.write(f"#!/bin/bash\npython3 {script_path}")
    os.chmod("zoe", 0o755)
    os.system("clear")
    print(f"Done Installing :,")
    os.remove(delete_file)


if __name__=="__main__":
    install()
  