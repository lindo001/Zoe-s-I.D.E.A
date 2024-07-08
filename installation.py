import os



drive_file_path = "/home/thinkpad/.Projects/Python/Zoe-s-I.D.E.A/rss_feed_mode.py"
calendar_file_path = "/home/thinkpad/.Projects/Python/Zoe-s-I.D.E.A/rss_feed_mode.py"
download_file_path = "/home/thinkpad/.Projects/Python/Zoe-s-I.D.E.A/rss_feed_mode.py"
recall_file_path = "/home/thinkpad/.Projects/Python/Zoe-s-I.D.E.A/rss_feed_mode.py"
rss_file_path = "/home/thinkpad/.Projects/Python/Zoe-s-I.D.E.A/rss_feed_mode.py"

def step_two_install():
    available_attempts = 10
    current_dir = working_dir = os.getcwd()
    while available_attempts > 0:
        if current_dir == "/":
            os.chdir("bin")
            install_script(working_dir)
            break
        current_dir = os.path.dirname(current_dir)
        os.chdir(current_dir)
        available_attempts -= 1
    else:
        print("Failed to locate bin folder")

def install_script(working_dir):
    script_path = os.path.join(working_dir, "main.py")
    delete_file = os.path.join(working_dir, "installation.py")
    with open("recall", "w") as f:
        f.write(f"""#!/bin/bash

case "$1" in
    "rss")
        python3 {rss_file_path}
        ;;
    "get")
        case "$2" in
            "videos")
                if [ "$3" = "playlist" ]; then
                    python3 {download_file_path}
                else
                    python3 {download_file_path}
                fi
                ;;
            *)
                echo "Invalid command. Usage: recall get [videos | videos playlist]"
                ;;
        esac
        ;;
    "calendar")
        python3 {calendar_file_path}
        ;;
    "")
        python3 {recall_file_path}
        ;;
    *)
        echo "Invalid command. Usage: recall [rss | get | calendar]"
        ;;
esac
""")
    os.chmod("recall", 0o755) 
    
    os.system("clear")  
    print("Done installing.")
    # os.remove(delete_file)  

def install():
    current_dir = working_dir = os.getcwd()
    for _ in range(3):
        current_dir = os.path.dirname(current_dir)
        os.chdir(current_dir)
        print(os.getcwd())
        if os.path.exists("Desktop"):
            global drive_file_path, calendar_file_path, download_file_path, recall_file_path, rss_file_path
            # drive_file_path = os.path.join(os.getcwd(), "Recall_python_files/gdrive_mode.py")
            # calendar_file_path = os.path.join(os.getcwd(), "Recall_python_files/gcalender_mode.py")
            # download_file_path = os.path.join(os.getcwd(), "Recall_python_files/download_mode.py")
            # recall_file_path = os.path.join(os.getcwd(), "Recall_python_files/recall_mode.py")
            # rss_file_path = os.path.join(os.getcwd(), "Recall_python_files/rss_feed_mode.py")
            os.makedirs("Recall_python_files", exist_ok=True)
            # os.replace("/home/thinkpad/.Projects/Python/Zoe-s-I.D.E.A/rss_feed_mode.py", rss_file_path)

            # Write the 'recall' Bash script with updated paths
            write_recall_script()

def write_recall_script():
    script_path = os.path.join(os.getcwd(), "recall")
    with open(script_path, "w") as f:
        f.write(f"""#!/bin/bash

case "$1" in
    "rss")
        python3 {rss_file_path}
        ;;
    "get")
        case "$2" in
            "videos")
                if [ "$3" = "playlist" ]; then
                    python3 {download_file_path}
                else
                    python3 {download_file_path}
                fi
                ;;
            *)
                echo "Invalid command. Usage: recall get [videos | videos playlist]"
                ;;
        esac
        ;;
    "calendar")
        python3 {calendar_file_path}
        ;;
    "")
        python3 {recall_file_path}
        ;;
    *)
        echo "Invalid command. Usage: recall [rss | get | calendar]"
        ;;
esac
""")
    os.chmod(script_path, 0o755)
if __name__ == "__main__":
    install()
    # install_script()