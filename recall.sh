#!/bin/bash

case "$1" in
    "rss")
        python3 /path/to/rss_feed_mode.py
        ;;
    "get")
        case "$2" in
            "videos")
                if [ "$3" = "playlist" ]; then
                    python3 /path/to/videoplaylist_mode.py
                else
                    python3 /path/to/video_mode.py
                fi
                ;;
            *)
                echo "Invalid command. Usage: recall get [videos | videos playlist]"
                ;;
        esac
        ;;
    "calendar")
        python3 /path/to/calendar_mode.py
        ;;
    "")
        python3 /path/to/recall_mode.py
        ;;
    *)
        echo "Invalid command. Usage: recall [rss | get | calendar]"
        ;;
esac
