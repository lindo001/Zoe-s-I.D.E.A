






from dowload_mode import download_mode_menu
from gcalender_mode import book,check


formater:dict={}
def main():
    while True:
        stdin = input("What should I do :")
        
        if "download" in stdin:
            download_mode_menu(stdin)
        elif "calender" in stdin:
            print("ppppp")
            if "set" in stdin:
                clean_and_book(stdin)
                print()
            else :
                check()

        elif "drive" in stdin:
            print("Connecting to drive")
        elif "rss" in stdin:
            print("Getting data from rss")
        elif "recall" in stdin:
            print("Trying recall feature")




def clean_and_book(io):
   
    
    indes = []
    #splet sentense
    for index,nu in enumerate(io):
        if "-" in nu:
            print(index)
            startindex = index            
            break


    hold = []
    sent = io[startindex:]
    #findes all -
    for i,letter in enumerate(sent):
        if "-" in letter:
            hold.append(i)
    
    
    new_list = []
    new_list.append(sent[hold[0]:hold[1]-1])
    new_list.append(sent[hold[1]:hold[2]-1])
    new_list.append(sent[hold[2]:hold[3]-1])
    new_list.append(sent[hold[3]:])
    for i in new_list:
    # print(sent[hold[0:]:hold[1]-1])
    
        if "-t" in i:
            formater["title"] = i[3:]
        elif "-s" in i:
            formater["summary"] = i[3:]
        elif "-l" in i:
            formater["location"]=i[3:]
        elif "-md" in i: 
            formater["date"]=i[4:]
    
    
    book(ititle=formater["title"],isummary=formater["summary"],ilocation=formater["location"],idate=formater["date"])
    
    
    
main()