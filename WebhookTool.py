import requests
import threading
import time
import os
from pystyle import Colorate, Colors

ascii_art = """
                                  ╔╦╗╦  ╦╔═╗  ╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═  ╔═╗╦ ╦╔═╗╦╔═╔═╗╦═╗
                                   ║ ╚╗╔╝║    ║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗  ╠╣ ║ ║║  ╠╩╗║╣ ╠╦╝
                                   ╩  ╚╝ ╚═╝  ╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩  ╚  ╚═╝╚═╝╩ ╩╚═╝╩╚═                                                                                                          
"""

choices = """
                                                    [1] Spam messages
                                                    [2] Delete webhook
                                                    [3] Rename webhook
                                                    [4] Change webhook avatar
    """

os.system('cls')
print(Colorate.Vertical(Colors.red_to_blue, ascii_art))
print(Colorate.Vertical(Colors.red_to_blue, choices))

def sendfagmsg(webhook_url, data):
    try:
        response = requests.post(webhook_url, json=data)
        response.raise_for_status()
        print(f"[>] Sent Message")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

def delete_fag(webhook_url):
    try:
        response = requests.delete(webhook_url)
        response.raise_for_status()
        print(f"[>] Deleted Webhook")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

def fag_renamer(webhook_url, new_name):
    data = {
        "name": new_name
    }
    try:
        response = requests.patch(webhook_url, json=data)
        response.raise_for_status()
        print(f"[>] Renamed Webhook to {new_name}")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

def fagatar(webhook_url, new_avatar_url):
    data = {
        "avatar_url": new_avatar_url
    }
    try:
        response = requests.patch(webhook_url, json=data)
        response.raise_for_status()
        print(f"[>] Changed Webhook Avatar")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")

def msg_spammer(webhook_urls, webhook_name, message):
    while True:
        threads = []
        for url in webhook_urls:
            data = {
            "content": message,
            "username": webhook_name
        }
        thread = threading.Thread(target=sendfagmsg, args=(url.strip(), data))
        threads.append(thread)
        thread.start()

        for thread in threads:
            thread.join()

def main():
    while True:
        choice = input("Choice >> ")

        if choice == "1":
            try:
                webhook_urls = input("[>] Enter the webhook URL(s) separated by space: ").split()
                webhook_name = input("[>] Enter the new name for the webhook: ")
                message = input("[>] Enter the message to send: ")
                msg_spammer(webhook_urls, webhook_name, message)
            except KeyboardInterrupt:
                print("[>] Keyboard Interrupt. Goodbye! :D")
        
        elif choice == "2":
            webhook_urls = input("[>] Enter the webhook URL(s) separated by space: ").split()
            for url in webhook_urls:
                delete_fag(url.strip())
                os.system('cls')
                print(Colorate.Vertical(Colors.red_to_blue, ascii_art))
                print(Colorate.Vertical(Colors.red_to_blue, choices))
            
        elif choice == "3":
            new_name = input("[>] Enter the new name for the webhook: ")
            webhook_urls = input("[>] Enter the webhook URL(s) separated by space: ").split()
            for url in webhook_urls:
                fag_renamer(url.strip(), new_name)
                os.system('cls')
                print(Colorate.Vertical(Colors.red_to_blue, ascii_art))
                print(Colorate.Vertical(Colors.red_to_blue, choices))
        
        elif choice == "4":
            new_avatar_url = input("[>] Enter the new avatar URL for the webhook: ")
            webhook_urls = input("[>] Enter the webhook URL(s) separated by space: ").split()
            for url in webhook_urls:
                fagatar(url.strip(), new_avatar_url)
                os.system('cls')
                print(Colorate.Vertical(Colors.red_to_blue, ascii_art))
                print(Colorate.Vertical(Colors.red_to_blue, choices))
        
        else:
            print("[>] what the fuck are you saying!")
            break

if __name__ == "__main__":
    main()
