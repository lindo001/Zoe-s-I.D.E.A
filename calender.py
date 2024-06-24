import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/calendar"]


def main():
  creds = None
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

  try:
    service = build("calendar", "v3", credentials=creds)

    now = datetime.datetime.now().isoformat() + "Z"  
    print("Getting the upcoming 10 events")
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
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
      print(start, event["summary"])
    event = {
        "summary": "RedPlay",
        "location": "Cool",
        "description": "something cool",
        "colorId": "5",  # Importance
        "start": {
            "dateTime": "2024-06-23T09:00:00+02:00",
            "timeZone": "Africa/Johannesburg"
        },
        "end": {
            "dateTime": "2024-06-23T19:00:00+02:00",
            "timeZone": "Africa/Johannesburg"
        },
        "attendees": [
            {"email": "lintmash@gmail.com"}
        ]
    }
    
    event = service.events().insert(calendarId="primary", body=event).execute()
    print(event.get('htmlLink'))

    
 
 
 
  except HttpError as error:
    print(f"An error occurred: {error}")
    
    
    # event = {
    #     "summary": "RedPlay",
    #     "location": "Cool",
    #     "description": "something cool",
    #     "colorId": "5",  # Importance
    #     "start": {
    #         "dateTime": "2024-06-23T09:00:00+02:00",
    #         "timeZone": "Africa/Johannesburg"
    #     },
    #     "end": {
    #         "dateTime": "2024-06-23T19:00:00+02:00",
    #         "timeZone": "Africa/Johannesburg"
    #     },
    #     "attendees": [
    #         {"email": "lintmash@gmail.com"}
    #     ]
    # }    
    
    summary = input("Summary")
    location = input("Where is it held default is online")
    description = input("description")
    importance = input("Color code")
    startZ


if __name__ == "__main__":
  main()