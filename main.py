import os
import pillow
import rtoml
import random

def handle_config() -> dict:
    if os.path.exists("config.toml"):
        # load config file
        with open("config.toml", "r") as f:
            config = rtoml.load(f)
        if config["noun1"] == "Your word here":
            print("Please actually fill in config file and run the script again.")
            exit()
    else:
        # no config file, create one
        template = {
            "keybind": "space",  # keybind to use
            "adjective1": "Your word here",  
            "adjective2": "Your word here", 
            "adjective3": "Your word here",  
            "adjective4": "Your word here",  
            "noun1": "Your word here",  
            "noun2": "Your word here",  
            "noun3": "Your word here", 
            "noun4": "Your word here",  
            "verb1": "Your word here",  
            "verb2": "Your word here",  
            "verb3": "Your word here", 
            "verb4": "Your word here",  
            "word1": "Your word here",  
            "word2": "Your word here",  
        }
        with open("config.toml", "w") as f:
            rtoml.dump(template, f)
        print(
            "No config file found, created one. Please edit it and run the script again."
        )
        exit()
    return config

def main():
    config = handle_config()
    wvar = random.randint(0,1)
    print(wvar)
