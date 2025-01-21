IMAGE

# Introduction
As a teacher, I have to engage in parent-teacher conferences a few times a year and every year I found myself rushing to make a quick intro card so people can know my name once they enter my room or are speaking with me. Of course, I can introduce myself or - as I have done here - I can have a programmable e-ink screen displaying my name and relevant information for parents. This is super simple to do and setup, but I wanted to dedicate a repository for my own posterity.
# Material(s)

Badger 2040 by Pimoroni - this can be purchased for $20 (about $30 after shipping costs) at the following link: https://shop.pimoroni.com/products/badger-2040?variant=39752959852627

# Case
This next section covers the 3D-printed case so I can put the badger on my desk.

The case I made has it as a slight angle and utilizes magnets to hold the cover in place. This makes it easy to take the Badger 2040 in and out of the case for changing what is displayed on the screen.

## Specifications & Material(s)
Below you can find the printer and material used.
### 3D Printer
 Original Prusa Mini+
### Material(s)
INLAND PLA 3D Printer Filament - 3D Printing PLA Filament 1.75mm, Dimensional Accuracy +/- 0.03mm - 1kg Cardboard Spool (2.2 lbs), Marble PLA
 – this can be purchased for $29.99 at the following link:
https://www.amazon.com/Inland-1-75mm-Marble-Printer-Filament/dp/B08M4733VV/ref=sr_1_3?crid=RY0788Z9D3XL&dib=eyJ2IjoiMSJ9.GvDUjGeacdaThMoKB2T31ewH9i3JmlLfhoDydChHBm-pD7cXPBEVjrKUewiIA1ZLE0_09V1n0PRn75b7hFqiDw4M0-lnl6NiRKwU4Bay_UQglrp8aVfnSITNRxxnTlk00zi7jk9JMRR5mzHilVguVNlu22jSBhxaIA2Mgu28qpM98QySMqZ0onKGj8rI2Ae99hyhSl7nTwlWuBccngRzfk5tlxoLLDb3Ck8adz-NTaQ.5vcyT03Wl1FkUx1DENvwhSOMvdqbl_TQCjXICAq7kSI&dib_tag=se&keywords=pla+filament+inland+marble&qid=1735843633&sprefix=pla+filament+inland+marble%2Caps%2C87&sr=8-3

DIYMAG 120Pcs Refrigerator Magnets 10x2mm Premium Brushed Nickel Small Round Cylinder Fridge Magnet, Perfect to use as Office Magnets, Dry Erase Board Magnetic pins, Whiteboard, Map Pins - this can be purchased for $12.99 at the following link: https://www.amazon.com/DIYMAG-Refrigerator-Magnets-100-piece/dp/B0753ZPBLQ/ref=sr_1_19?crid=4S38QACW5AEP&dib=eyJ2IjoiMSJ9.EYtZ7hOWoiRCrhWwwsVJrzaAfrfRynJzx0wpiY7EsDZ_R-bKmqQ46Kr_FJ605BzEmuvGgxXUmGzYITG6lXI-Y-QS1oPBC3tEEx4AuWbXIllhps4bsrN73sPxXvwDwjxnnNoBRcNRsZD0FSY8oCu01ctJIgLgNL79HUSnNnuCjsskJ3paOzRH5ifOJrdhgmuFKdXm3msnuZGOTHAOwH48ZJCPbHj7LhqKhDLUPQbLvsc.g_VQ_G2BEWRtxm6rLwTTMmpZn3GpH8QrYflAKJWOVWI&dib_tag=se&keywords=10%2Bmm%2Bmagnets&qid=1736535291&sprefix=10%2Bmm%2Bmagnet%2Caps%2C88&sr=8-19&th=1
### Software
 PrusaSlicer
 
IMAGE

### Settings
  Layer Height: .2mm \
  Infill: 50% \
  Supports: Everywhere \
  Estimated Printing Time: TBD

# Code
There is already a lot of available code, especially from Pimoroni themselves; here's how I edited it for my own use.

## Software
I personally like to use Thonny for my editing/programming of microcontrollers, so that is what I have here.

IMAGE

## QR Code
The first thing I wanted to incorporate was a QR code for a survey for families when they come through my classroom for parent-teacher conferences.

IMAGE

## Code

If you do not want to download the .py file, you can just copy the following to your clipboard.

```bash
import badger2040
import jpegdec
import pngdec


# Global Constants
WIDTH = badger2040.WIDTH
HEIGHT = badger2040.HEIGHT

IMAGE_WIDTH = 104

COMPANY_HEIGHT = 30
DETAILS_HEIGHT = 20
NAME_HEIGHT = HEIGHT - COMPANY_HEIGHT - (DETAILS_HEIGHT * 2) - 2
TEXT_WIDTH = WIDTH - IMAGE_WIDTH - 1

COMPANY_TEXT_SIZE = 0.6
DETAILS_TEXT_SIZE = 0.5

LEFT_PADDING = 5
NAME_PADDING = 20
DETAIL_SPACING = 10

BADGE_PATH = "/badges/badge.txt"

DEFAULT_TEXT = """mustelid inc
H. Badger
RP2040
2MB Flash
E ink
296x128px
/badges/badge.jpg
"""

# ------------------------------
#      Utility functions
# ------------------------------


# Reduce the size of a string until it fits within a given width
def truncatestring(text, text_size, width):
    while True:
        length = display.measure_text(text, text_size)
        if length > 0 and length > width:
            text = text[:-1]
        else:
            text += ""
            return text


# ------------------------------
#      Drawing functions
# ------------------------------

# Draw the badge, including user text
def draw_badge():
    display.set_pen(0)
    display.clear()

    try:
        # Draw badge image
        png.open_file(badge_image)
        png.decode(WIDTH - IMAGE_WIDTH, 0)
    except (OSError, RuntimeError):
        # Draw badge image
        jpeg.open_file(badge_image)
        jpeg.decode(WIDTH - IMAGE_WIDTH, 0)

    # Draw a border around the image
    display.set_pen(0)
    display.line(WIDTH - IMAGE_WIDTH, 0, WIDTH - 1, 0)
    display.line(WIDTH - IMAGE_WIDTH, 0, WIDTH - IMAGE_WIDTH, HEIGHT - 1)
    display.line(WIDTH - IMAGE_WIDTH, HEIGHT - 1, WIDTH - 1, HEIGHT - 1)
    display.line(WIDTH - 1, 0, WIDTH - 1, HEIGHT - 1)

    # Uncomment this if a white background is wanted behind the company
    # display.set_pen(15)
    # display.rectangle(1, 1, TEXT_WIDTH, COMPANY_HEIGHT - 1)

    # Draw the company
    display.set_pen(15)  # Change this to 0 if a white background is used
    display.set_font("serif")
    display.text(company, LEFT_PADDING, (COMPANY_HEIGHT // 2) + 1, WIDTH, COMPANY_TEXT_SIZE)

    # Draw a white background behind the name
    display.set_pen(15)
    display.rectangle(1, COMPANY_HEIGHT + 1, TEXT_WIDTH, NAME_HEIGHT)

    # Draw the name, scaling it based on the available width
    display.set_pen(0)
    display.set_font("sans")
    name_size = 2.0  # A sensible starting scale
    while True:
        name_length = display.measure_text(name, name_size)
        if name_length >= (TEXT_WIDTH - NAME_PADDING) and name_size >= 0.1:
            name_size -= 0.01
        else:
            display.text(name, (TEXT_WIDTH - name_length) // 2, (NAME_HEIGHT // 2) + COMPANY_HEIGHT + 1, WIDTH, name_size)
            break

    # Draw a white backgrounds behind the details
    display.set_pen(15)
    display.rectangle(1, HEIGHT - DETAILS_HEIGHT * 2, TEXT_WIDTH, DETAILS_HEIGHT - 1)
    display.rectangle(1, HEIGHT - DETAILS_HEIGHT, TEXT_WIDTH, DETAILS_HEIGHT - 1)

    # Draw the first detail's title and text
    display.set_pen(0)
    display.set_font("sans")
    name_length = display.measure_text(detail1_title, DETAILS_TEXT_SIZE)
    display.text(detail1_title, LEFT_PADDING, HEIGHT - ((DETAILS_HEIGHT * 3) // 2), WIDTH, DETAILS_TEXT_SIZE)
    display.text(detail1_text, 5 + name_length + DETAIL_SPACING, HEIGHT - ((DETAILS_HEIGHT * 3) // 2), WIDTH, DETAILS_TEXT_SIZE)

    # Draw the second detail's title and text
    name_length = display.measure_text(detail2_title, DETAILS_TEXT_SIZE)
    display.text(detail2_title, LEFT_PADDING, HEIGHT - (DETAILS_HEIGHT // 2), WIDTH, DETAILS_TEXT_SIZE)
    display.text(detail2_text, LEFT_PADDING + name_length + DETAIL_SPACING, HEIGHT - (DETAILS_HEIGHT // 2), WIDTH, DETAILS_TEXT_SIZE)

    display.update()


# ------------------------------
#        Program setup
# ------------------------------

# Create a new Badger and set it to update NORMAL
display = badger2040.Badger2040()
display.led(128)
display.set_update_speed(badger2040.UPDATE_NORMAL)
display.set_thickness(2)

jpeg = jpegdec.JPEG(display.display)
png = pngdec.PNG(display.display)

# Open the badge file
try:
    badge = open(BADGE_PATH, "r")
except OSError:
    with open(BADGE_PATH, "w") as f:
        f.write(DEFAULT_TEXT)
        f.flush()
    badge = open(BADGE_PATH, "r")

# Read in the next 6 lines
company = badge.readline()        # "mustelid inc"
name = badge.readline()           # "H. Badger"
detail1_title = badge.readline()  # "RP2040"
detail1_text = badge.readline()   # "2MB Flash"
detail2_title = badge.readline()  # "E ink"
detail2_text = badge.readline()   # "296x128px"
badge_image = badge.readline()    # /badges/badge.jpg

# Truncate all of the text (except for the name as that is scaled)
company = truncatestring(company, COMPANY_TEXT_SIZE, TEXT_WIDTH)

detail1_title = truncatestring(detail1_title, DETAILS_TEXT_SIZE, TEXT_WIDTH)
detail1_text = truncatestring(detail1_text, DETAILS_TEXT_SIZE,
                              TEXT_WIDTH - DETAIL_SPACING - display.measure_text(detail1_title, DETAILS_TEXT_SIZE))

detail2_title = truncatestring(detail2_title, DETAILS_TEXT_SIZE, TEXT_WIDTH)
detail2_text = truncatestring(detail2_text, DETAILS_TEXT_SIZE,
                              TEXT_WIDTH - DETAIL_SPACING - display.measure_text(detail2_title, DETAILS_TEXT_SIZE))


# ------------------------------
#       Main program
# ------------------------------

draw_badge()

while True:
    # Sometimes a button press or hold will keep the system
    # powered *through* HALT, so latch the power back on.
    display.keepalive()

    # If on battery, halt the Badger to save power, it will wake up if any of the front buttons are pressed
    display.halt()
```

# Tips
I have been using the filament I have here because it's just available. I think this would look better in black (Prusa has a really nice galaxy black filament).
