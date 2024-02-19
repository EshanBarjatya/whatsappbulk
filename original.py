from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import requests
import tkinter as tk
from tkinter import simpledialog

# Setup the Google Sheets API
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = 'google sheets api.json'

credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# Call the Sheets API
service = build('sheets', 'v4', credentials=credentials)
sheet = service.spreadsheets()

# Read the sheet data
SPREADSHEET_ID = '1uggiNaxeDE-KY3vr8ATidkV2jdeaIZGGTpzVezajDgM'
RANGE_NAME = 'Sheet1!A:E'  # Adjusted to include all columns you need
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE_NAME).execute()
values = result.get('values', [])

access_token = "EAALulZBaUFEoBO4IZBbZCfKQZA5HC24kHUkjRMMRqtFZAIeLdbu2O8nGiaVR3jc85ilhhhoXtsrORO8eaAmdBIVH93ILEkScKjWe5YVsZABB2qNH73B2fuUf0xwzfhnHG8aaFWdZAKZAjBVg6gz2F5vlrYt3isVEgQ71YFPxYCLNLde9Y1W3J56Q7TL1mMTMGiR8"
url = "https://graph.facebook.com/v18.0/238565786002156/messages"

headers = {
    'Authorization': f'Bearer EAALulZBaUFEoBO4IZBbZCfKQZA5HC24kHUkjRMMRqtFZAIeLdbu2O8nGiaVR3jc85ilhhhoXtsrORO8eaAmdBIVH93ILEkScKjWe5YVsZABB2qNH73B2fuUf0xwzfhnHG8aaFWdZAKZAjBVg6gz2F5vlrYt3isVEgQ71YFPxYCLNLde9Y1W3J56Q7TL1mMTMGiR8',
    'Content-Type': 'application/json'
}
print(headers)
header_media_id = "media_id"  # Uncomment this if you're using a media ID
button_text = "this is a btn ifyyk"
# button_url = "https://anitajainfashions.com/" 


# Assuming phone numbers are in the second column (index 1)
phonenumbers = [row[1] for row in values if len(row) >= 5]
print(phonenumbers)


def send_mark1_template(customer_info):

    for row in values:
        
        if len(row) >= 5:  # Ensure there are at least five columns with data
            customer_name = row[0]  # Customer's name from column A
            phone_number = row[1]   # Phone number from column B
            company_name = row[2]   # Company name from column C
            tracking_number = row[3]  # Tracking number from column D
            website = row[4]  # Website from column E
        
            print(phone_number)   # Phone number from column B
            print(phonenumbers)   # Phone number from column B

            # Construct the data payload for the API request
            data = {
                "messaging_product": "whatsapp",
                "to": phone_number,
                "type": "template",
                "template": {
                    "name": "placeholder",  # Use the actual template name you set on WhatsApp Manager
                    "language": {
                        "code": "en_US"
                    },
                    "components": [{
                        "type": "body",
                        "parameters": [
                            {"type": "text", "text": customer_name},
                            {"type": "text", "text": company_name},
                            {"type": "text", "text": tracking_number},
                            {"type": "text", "text": website}
                        ]
                    }]
                }
            }

            # Send the message
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                print(f"Message sent to {customer_name} ({phone_number}) successfully.")
            else:
                print(f"Failed to send message to {customer_name} ({phone_number}). Response: {response.text}")
        else:
            print(f"Skipping row with insufficient data: {row}")
        
        # return phone_number


def send_mark2_template(customer_info):
    # Gather inputs once before the loop
    template_name = "imagesender"
    header_image_url = input("Enter the URL of the image: ")  # Or use header_media_id if you have one
    temptext = input("Enter The Text Message You Want To Send: ")
    websiteurl = input(str("enter the url of the website something like: /products/chocolate-plain-crep : "))

    for row in values:
        if len(row) >= 2:  # Check if there are at least two columns
            phone_number1 = row[0]  # First phone number
            phone_number2 = row[1]  # Second phone number


            # The data payload for the request
            data = {
  "messaging_product": "whatsapp",
  "to": phone_number2,
  "type": "template",
  "template": {
    "name": "imagesender",
    "language": {
      "code": "en_US"
    },
   "components": [
    {
        "type": "header",
        "parameters": [
            {
                "type": "image",
                "image": {
                    "link": header_image_url
                }
            }
        ]
    },
    {
        "type": "body",
        "parameters": [
            {
                "type": "text",
                "text": temptext
            }
        ]
    },
    {
        "type": "button",
        "sub_type": "url",
        "index": 0,
        "parameters": [
            {
                "type": "text",
                "text": websiteurl  
            }
        ]
    }
]
  }
}
            # Send the POST request
            response = requests.post(url, headers=headers, json=data)

            # Check the response from WhatsApp
            if response.status_code == 200:
                print(f"Message sent to {phone_number1} ({phone_number2}) successfully with {template_name}.")
            else:
                print(f"Failed to send message to {phone_number1} ({phone_number2}). Status code: {response.status_code}, Response: {response.text}")
        else:
            print(f"Skipping row with insufficient data: {row}")


def send_mark3_template(customer_info):
    # Gather inputs once before the loop
    template_name = "mark4"
    # header_video_url = input("Enter the URL of the video: ")  # Or use header_media_id if you have one
    # websiteurl = input(str("enter the url of the website something like: /products/chocolate-plain-crep : "))
    # temptext = input("Enter The Text Message You Want To Send: ")
    temptext = "temp text"
                                        # "link": header_video_url  # Ensure this is a direct link to an image file
    

    for row in values:
        if len(row) >= 2:  # Check if there are at least two columns
            phone_number1 = row[0]  # First phone number
            phone_number2 = row[1]  # Second phone number

            # The data payload for the request
            data = {
                "messaging_product": "whatsapp",
                "to": phone_number2,
                "type": "template",
                "template": {
                    "name": "mark4",
                    "language": {
                        "code": "en_US"
                    },
                    "components": [
                        {
                            "type": "header",
                            "parameters": [
                                {
                                    "type": "video",
                                    "video": {
                                        "link": "https://drive.google.com/uc?export=download&id=1sV7G2i1mLEnVYJJnh9KJiocIYtcccyAP"  # Ensure this is a direct link to an video file
                                    }
                                }
                            ]
                        },
                        {
                            "type": "body",
                            "parameters": [
                                {
                                    "type": "text",
                                    "text": "/products/chocolate-plain-crep"   # The first placeholder value
                                },
                            ]
                        },
                        {
                            "type": "button",
                            "sub_type": "url",
                            "index": 0,
                            "parameters": [
                                {
                                    "type": "text",
                                    "text": "/products/chocolate-plain-crep"  
                                }
                            ]
                                    }
                        # Include any other components that your template might have, like buttons
                    ]
                }
            }

            # Send the POST request
            try:
                response = requests.post(url, headers=headers, json=data)
                response.raise_for_status()  # This will raise an exception for HTTP errors
                print(f"Message sent to {phone_number1} ({phone_number2}) successfully with video sender.")
            except requests.exceptions.HTTPError as err:
                print(f"HTTP error occurred: {err}")  # Python 3.6
                print(f"Response text: {response.text}")
            except Exception as err:
                print(f"An error occurred: {err}")

        else:
            print(f"Skipping row with insufficient data: {row}")




# Map template names to their respective functions for easier access
templates = {
    "Tracking Message Sender": send_mark1_template,
    "Image Sender": send_mark2_template,
    "video Sender": send_mark3_template,
}

# Function to display menu and get user selection
def get_user_template_choice():
    print("Please select a message template number:")
    for idx, template in enumerate(templates, start=1):
        print(f"{idx}. {template}")
    choice = input("Enter the number of your choice: ")
    return choice

# Main logic
def main():
    choice = get_user_template_choice()
    # Convert choice to index
    try:
        choice_index = int(choice) - 1
        if choice_index < 0 or choice_index >= len(templates):
            raise ValueError
        selected_template = list(templates)[choice_index]
        # Assume you have customer_info from somewhere
        customer_info = {}  # Placeholder for customer information
        # Call the selected template function
        templates[selected_template](customer_info)
    except ValueError:
        print("Invalid selection. Please enter a valid number.")

if __name__ == "__main__":
    main()