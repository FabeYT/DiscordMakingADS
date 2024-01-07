import requests
import json
import time
import glob
from datetime import datetime

channel_ids = ["1189181365615329350"] # Replace the following line with your desired channel IDs
discord_token = "N_puyDfOa4_ZoZwXvD1UCN4Y.ZY39bA.dFM1Vs4WPq4JA6Lg-eJksDmUrVc" # Discord Token

print("\033[34m███╗░░░███╗███████╗░██████╗░██████╗░█████╗░░██████╗░███████╗  ░██████╗███████╗███╗░░██╗██████╗░███████╗██████╗░")
print("\033[34m████╗░████║██╔════╝██╔════╝██╔════╝██╔══██╗██╔════╝░██╔════╝  ██╔════╝██╔════╝████╗░██║██╔══██╗██╔════╝██╔══██╗")
print("\033[34m██╔████╔██║█████╗░░╚█████╗░╚█████╗░███████║██║░░██╗░█████╗░░  ╚█████╗░█████╗░░██╔██╗██║██║░░██║█████╗░░██████╔╝")
print("\033[34m██║╚██╔╝██║██╔══╝░░░╚═══██╗░╚═══██╗██╔══██║██║░░╚██╗██╔══╝░░  ░╚═══██╗██╔══╝░░██║╚████║██║░░██║██╔══╝░░██╔══██╗")
print("\033[34m██║░╚═╝░██║███████╗██████╔╝██████╔╝██║░░██║╚██████╔╝███████╗  ██████╔╝███████╗██║░╚███║██████╔╝███████╗██║░░██║")
print("\033[34m╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═════╝░╚═╝░░╚═╝░╚═════╝░╚══════╝  ╚═════╝░╚══════╝╚═╝░░╚══╝╚═════╝░╚══════╝╚═╝░░╚═╝ Made by DasoFabe")
print()
print("\033[97m")

def read_message_content(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def send_messages(auth, channel_id, msg, files):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    response = requests.post(url, headers=auth, data=msg, files=files)

    if response.status_code == 200:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Message and images successfully sent to channel {channel_id} | {current_time}")

def main():

    auth = {
        'authorization': discord_token
    }

    # Read message content from the file
    message_content_path = 'YourMessageContent.txt'
    msg = {
        'content': read_message_content(message_content_path)
    }

    bild_dateien = glob.glob('YourVouchImage/*.jpg') + glob.glob('YourVouchImage/*.png')

    counter = 60  

    if len(bild_dateien) < 1:
        print("Add an image to the Vouche folder.")
    else:
        while True:
            for channel_id in channel_ids:
                # Send messages with images
                files = [('file', (f'file{i}.png', open(bild, 'rb'))) for i, bild in enumerate(bild_dateien[:6])]
                send_messages(auth, channel_id, msg, files)
                time.sleep(counter)

if __name__ == "__main__":
    main()
