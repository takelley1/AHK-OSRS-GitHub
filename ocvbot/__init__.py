
from ocvbot.ocvbot import vision as vis

import pyautogui as pag

# These are constants.
# See ./tests/haystacks/client_anatomy.png for more info.
# Width and height of the entire game client.
CLIENT_WIDTH = 765
CLIENT_HEIGHT = 503

# Width and height of the inventory screen, in pixels.
INV_WIDTH = 186
INV_HEIGHT = 262

# Width and height of just the game screen in the game client.
GAME_SCREEN_WIDTH = 512
GAME_SCREEN_HEIGHT = 334

CHAT_MENU_WIDTH = 506
CHAT_MENU_HEIGHT = 129

# Dimensions of the most recent "line" in the chat menu.
CHAT_MENU_RECENT_WIDTH = 489
CHAT_MENU_RECENT_HEIGHT = 14

"""
Creates objects containing useful game coordinates for other
functions to serach through.
"""

# TODO: Find a better way to do this.
# Clean up left over screenshots from failed runs.
#sub.Popen(["rm", "./.screenshot2*"])

# Get the display size in pixels.
display_width = pag.size().width
display_height = pag.size().height


(client_left, client_top) = anchor

# The left corner of the game client is 709 pixels to the left of
#   the prayers icon
client_left -= 748
client_top -= 21

# Now we can create an object with the game client's X and Y
#   coordinates. This will allow other functions to search for
#   needles within the "client" object's coordinates, rather than
#   within the entire display's coordinates, which is much faster.
client = vis.Vision(left=client_left, width=CLIENT_WIDTH,
                top=client_top, height=CLIENT_HEIGHT)

# Create another object for the player's inventory.
inv_left = client_left + 548
inv_top = client_top + 205
inv = vis.Vision(left=inv_left, top=inv_top,
             width=INV_WIDTH, height=INV_HEIGHT)
# And another object for the bottom half of the player's inventory
inv_bottom_left = inv_left
inv_bottom_top = inv_top + (round(INV_HEIGHT / 2))
inv_bottom = vis.Vision(left=inv_bottom_left, top=inv_bottom_top,
                    width=INV_WIDTH, height=(round(INV_HEIGHT / 2)))

# Same thing for the gameplay screen.
game_screen_left = client_left + 4
game_screen_top = client_top + 4
game_screen = vis.Vision(left=game_screen_left, top=game_screen_top,
                     width=GAME_SCREEN_WIDTH, height=GAME_SCREEN_HEIGHT)

# And the chat menu.
chat_menu_left = client_left + 7
chat_menu_top = client_top + 345
chat_menu = vis.Vision(left=chat_menu_left, top=chat_menu_top,
                   width=CHAT_MENU_WIDTH, height=CHAT_MENU_HEIGHT)

# Another object for checking the most recent chat message.
chat_menu_recent_left = chat_menu_left + 2
chat_menu_recent_top = chat_menu_top + 100
chat_menu_recent = vis.Vision(left=chat_menu_recent_left,
                          top=chat_menu_recent_top,
                          width=CHAT_MENU_RECENT_WIDTH,
                          height=CHAT_MENU_RECENT_HEIGHT)

# Another object for searching the entire display.
display = vis.Vision(left=0, width=display_width,
                 top=0, height=display_height)
