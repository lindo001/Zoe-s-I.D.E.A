import re
import datetime
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


#recall add even -t listen -s listenig to music -l who  -md 05 
SCOPES = ["https://www.googleapis.com/auth/calendar"]


title = ""
summary =""
location = ""
month = ""
date = ""
cool_map:dict ={}
def main(selected):
  
  creds = None
  service =None
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES[0])
    
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES[0])
      creds = flow.run_local_server(port=0)
    
    with open("token.json", "w") as token:
      token.write(creds.to_json())
      service = build("calendar", "v3", credentials=creds)

  try:
    if selected == 1:
      upload(service)
      
    elif selected ==2:
      retrive(service)
 
  except HttpError as error:
    print(f"An error occurred: {error}")

def retrive(service):
    now = datetime.datetime.now().isoformat() + "Z"  
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=7,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )
    events = events_result.get("items", [])

    if not events:
      print("No upcoming events found.")
      return

     
    for event in events:
      start = event["start"].get("dateTime", event["start"].get("date"))
      print(start.split("T")[0], event["summary"])    
   
def upload(service):

    
    event = {
        "summary": cool_map["title"],
        "location": cool_map["location"],
        "description": cool_map["summary"],
        "start": {
            "dateTime": "2024-"+cool_map["date"]+"T09:00:00+02:00",
            "timeZone": "Africa/Johannesburg"
        },
        "end": {
            "dateTime": "2024-"+cool_map["date"]+"T19:00:00+02:00",
            "timeZone": "Africa/Johannesburg"
        },
        "attendees": [
            {"email": "lintmash@gmail.com"}
        ]
    }
    
    event = service.events().insert(calendarId="primary", body=event).execute()
    print(event.get('htmlLink'))
    


def book(ititle,isummary,ilocation,idate):
  cool_map["title"] = ititle
  cool_map["summary"] = isummary
  cool_map["location"] = ilocation
  cool_map["date"] = idate
  main(1)

def check():
  main(2)
 
