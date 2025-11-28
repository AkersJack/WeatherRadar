import sys 
import time
from datetime import datetime
import pytz
import os
import json
import math
import requests
import logging
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import xmltodict
import geotiler
import numpy as np
import pygame



#KLWX radar station for sykesville MD

# Display resultion (that we are using): 1024 x 768

# Remove Adafruit libraries
from Rsecrets import secrets

#CURR_DIR = f"{home/james/Weather-Radar/Examples(weather_radarGAME.py)}"
CURR_DIR = f"{os.getcwd()}/"

global timezone 
global station 
global forecast_url
global forecast_grid_url


# Initialize Pygame
pygame.init()


# Set up the display
screen = pygame.display.set_mode((1024, 768), pygame.FULLSCREEN)  # Adjust size as needed
clock = pygame.time.Clock()

disp = screen

# Function to update display
def update_display(image):
    # Convert PIL Image to Pygame surface
    mode = image.mode
    size = image.size
    data = image.tobytes()
    py_image = pygame.image.fromstring(data, size, mode)
    
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Blit the new image to the screen
    screen.blit(py_image, (0, 0))
    
    # Update the display
    pygame.display.flip()

print("\n*******************************\n*  the initial WEATHER RADAR was by Thornhill! But then James changed it    *\n*******************************")

if __name__ == "__main__":
    running = True
    while running:
        for event in pygame.event.get():
         if event.type == pygame.QUIT:
             running = False
     # Your existing main loop logic here...
    while True:
        try:
            print("\n****************************************************")

            time_now = datetime.now(pytz.timezone(timeZone))

            print(f"\n----------------------\n     Local info:\n----------------------")
            local_warnings, local_alerts = get_all_alerts(coordinates=(lat_long[1],lat_long[0]))

            print(f"\n\n----------------------\n     Greater area:\n----------------------")
            warnings_list, hazard_list = get_all_alerts("Storm","Extreme Wind","High Wind","Gale Warning","Blizzard","Hurricane","Tropical","Winter Storm")

        except Exception as exception: 
        ### If there's an error, get the time, and display it.
            time_now = datetime.now(pytz.timezone('America/New_York'))
            message = f'{time_now.strftime("%H:%M")}\nException: {type(exception).__name__}'
            disp.image(status_images(message,loading,font=fnt_goth_medium))
            logging.exception('Caught an error')
            break
            
