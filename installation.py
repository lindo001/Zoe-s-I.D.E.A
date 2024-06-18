# Intalls a bash script 
import os
def install():
    available_attempts:int = 10
    current_dir = working_dir = os.getcwd()
    #should remove itself after installing
    while True:
        print("We are :"+ current_dir)
        # should check if its in root 
        # if true head to bach else one step higher and repeat process
        if available_attempts ==0:break
        if current_dir == "/": 
            print ("Found it")
            os.chdir("bin")
            install_script(working_dir)
            break
   
        current_dir = os.path.dirname(current_dir)
        os.chdir(current_dir)
        available_attempts-=1
        
def install_script(working_dir):
    
    print("ff "+ working_dir)
    # os.remove
    pass

if __name__=="__main__":
    install()
  