import json


    
class Converter:
    file_path:str

    def __init__(self,path,isJson = False) -> str:
        f = open(path,"r")
        st = f.read()
        if isJson:
            self.file_path = json.loads(st)
        else:
            self.file_path = st
        f.close()
    
         
    def get_data(self)-> str:

        return self.file_path
    
    def set_data(self,data:dict):
        f = open(self.file_path,"w")
        f.write(data)
        f.close()



    def set_json(self,user_input:str,bot_response:str,required_words:str):


        # import json

        # Path to your JSON file
        json_file = "txt_files/recall.json"

        # Load existing JSON data
        with open(json_file, "r") as f:
            existing_data = json.load(f)

        # New data to add
        new_entry = {
            "bot_response": bot_response,
            "required_words": required_words.split(),
            "single_sentence": len(user_input)>1
        }

        # Append new entry to existing data
        existing_data.append(new_entry)

        # Write updated data back to JSON file
        with open(json_file, "w") as f:
            json.dump(existing_data, f, indent=4)

        print("New entry added to JSON file.")