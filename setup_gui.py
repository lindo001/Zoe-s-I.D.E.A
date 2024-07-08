import curses
from installation import install
import agent_states as a  

menu_options = ["Try out", "Install", "Exit"]


def menuBox(std, screenHeight, screenWidth, current_index):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    ul_y2 = 2  
    ul_x2 = int(screenWidth / 2) + 1  
    lr_y2 = screenHeight - 2  
    lr_x2 = screenWidth - 2  
    
    menu = std.subwin(lr_y2 - ul_y2 + 1, lr_x2 - ul_x2 + 1, ul_y2, ul_x2)
    # menu.box()  
    curses.curs_set(0)
    
    h = int(screenHeight / 2)
    w = int(screenWidth / 2)
    # menu.addstr(h, 0, f"Height: {screenHeight}, Width: {screenWidth}")
    try:    
        for index, key in enumerate(menu_options):
            if index == current_index:
                menu.attron(curses.color_pair(1))
                menu.addstr(h + index + 1, int(w / 2) - 7, f"- {key}")
                menu.attroff(curses.color_pair(1))
            else:
                menu.addstr(h + index + 1, int(w / 2) - 7, f"- {key}")
            
        menu.refresh()
        return menu

    except:pass
def drawAgent(stdscr, screenHeight, screenWidth):
    try:
        word = f"Height is: {screenHeight}, Width is: {screenWidth}"
        stdscr.addstr(0, 0, word)
        ul_y1 = 2  
        ul_x1 = 2  
        lr_y1 = screenHeight - 2  
        lr_x1 = int(screenWidth / 2) - 2  
        recall_agent_area = stdscr.subwin(lr_y1 - ul_y1 + 1, lr_x1 - ul_x1 + 1, ul_y1, ul_x1)
        h = int(screenHeight / 2)
        recall_agent_area.addstr(1, 1, a.agent["happy"])  
        recall_agent_area.refresh()
    except:pass
def main(stdscr):
    curses.curs_set(0)  
    screenHeight, screenWidth = stdscr.getmaxyx()
    current_index = 0
    
    stdscr.addstr(screenHeight - 1, 3, "@Lindomash001")
    
    drawAgent(stdscr, screenHeight, screenWidth)
    menu = menuBox(stdscr, screenHeight, screenWidth, current_index)
    
    while True:
        current_option = stdscr.getch()
        
        if current_option == curses.KEY_UP and current_index > 0:
            current_index -= 1
        
        elif current_option == curses.KEY_DOWN and current_index < len(menu_options) - 1:
            current_index += 1
        
        elif current_option == curses.KEY_ENTER or current_option in [10, 13]:
            stdscr.refresh()
            stdscr.getch()  
            break
        
        menu.clear()
        menu = menuBox(stdscr, screenHeight, screenWidth, current_index)
        menu.refresh()
        
    
    if current_index ==0:
        stdscr.clear()
        stdscr.getch()
        print("sssssadasfRDGFDc")
    elif current_index ==1:
        install()
    elif current_index ==3:
        stdscr.clear()
        stdscr.getch()          




if __name__ =="__main__":
    
    
    curses.wrapper(main)