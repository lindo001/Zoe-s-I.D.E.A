import json
import random

def tips()-> None:
    print("Done Installing :e")
    
    file = "vault/tips.json"
    number = random.randint(0,10)
    with open(file,"r") as jsoon_file:
        data = json.load(jsoon_file)
        print(data["coding_principles"][number])
    jsoon_file.close()
    
    
    
    
if __name__ == "__main__":
    tips()
