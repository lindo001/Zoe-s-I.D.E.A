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





# if __name__ == "__main__":
#     print(Converter("txt_files/rss_links.json").get_data()["Development News"])

# improve unit tests - everyone should work on unit tests - run tests before and after pushing