import re
from json_and_text import Converter  



converter = Converter("txt_files/recall.json", isJson=True)

def start_recall(user_input):
    scores = []
    
    for cached_data in converter.get_data():
        score = 0
        if "required_words" in cached_data:
            for word in cached_data["required_words"]:
                if word in user_input:
                    score += 1
        scores.append(score)
    
    max_score = max(scores)
    max_index = scores.index(max_score)
    
    if max_score > 0:
        return converter.get_data()[max_index]["bot_response"]
    else:
        recall_database = input("Couldn't find anything to help. Would you like to recall the database? (y/n): ")
        if recall_database.lower() == "y":
            return add_to_memory_bank(user_input)  
        else:
            return "Nothing was found"

def tokenize(sentence):
    return re.split(r'\s+|[,;?!.-]\s*', sentence.lower())

def recall_mode():
    while True:
        user_input = input("Ask: ")
        print("Recall:", start_recall(user_input))

def add_to_memory_bank(pre_user_input):   
    how_to_responsed = input("How to respond: ")
    required_words = input("Are there any special keywords to look out for ?")
    
    converter.set_json(pre_user_input,how_to_responsed,required_words)
   
    

if __name__ == "__main__":
    recall_mode()