
![Image_1](https://github.com/user-attachments/assets/30eb2ef9-dc15-4ebc-8d34-b0c19a2a5339)

# Introduction
As a teacher, I have to engage in parent-teacher conferences a few times a year and every year I found myself rushing to make a quick intro card so people can know my name once they enter my room or are speaking with me. Of course, I can introduce myself or - as I have done here - I can have a programmable e-ink screen displaying my name and relevant information for parents. This is super simple to do and setup, but I wanted to dedicate a repository for my own posterity.
# Material(s)

Badger 2040 by Pimoroni - this can be purchased for $20 (about $30 after shipping costs) at the following link: https://shop.pimoroni.com/products/badger-2040?variant=39752959852627

DIYMAG 120Pcs Refrigerator Magnets 10x2mm Premium Brushed Nickel Small Round Cylinder Fridge Magnet, Perfect to use as Office Magnets, Dry Erase Board Magnetic pins, Whiteboard, Map Pins  - this can be purchased for $12.99 at the following link: https://www.amazon.com/DIYMAG-Refrigerator-Magnets-100-piece/dp/B0753ZPBLQ/ref=sr_1_15?crid=1LP6OMWHOW7J0&dib=eyJ2IjoiMSJ9.WlU1gPXNyLeoE60GeE-rIFVgLx09JrIzCqVNNmZI45Se5J-RxH5oeplSl2VZjbZazxosP3Ww3WEyXQRheL1tMhdbiS9NHFA3k4PDUAtjCQ_pDsDKOdLYM4CulMzqCWwsFtrzBy6IabptRBPHUnjV77nJ0TB0FTenl1IaVMa2_x4l9SJvljne80_YfM-Is8V8TxyEISlLSXDLJCjZRkrJcUHff_Wv2qCz67dz7HNRva4.WYhowoa9txxhU4kfoz_R9glKt7drWcm2iIcKx4Yotcc&dib_tag=se&keywords=10mm%2Bdiameter%2Bmagnets%2Bneodymium&qid=1737917543&sprefix=10mm%2Bdiameter%2Bmagnets%2Bneodynium%2Caps%2C114&sr=8-15&th=1

# Case
This next section covers the 3D-printed case so I can put the badger on my desk.

![Image_2](https://github.com/user-attachments/assets/ea6a25d9-8066-47b9-9bec-3978476ba82f)

The case I made has it as a slight angle and utilizes magnets to hold the cover in place. This makes it easy to take the Badger 2040 in and out of the case for changing what is displayed on the screen.

![Image_3](https://github.com/user-attachments/assets/37eb265c-3e5f-43ad-b76c-f45b45582363)

## Specifications & Material(s)
Below you can find the printer and material used.
### 3D Printer
 Original Prusa Mini+
### Material(s)
INLAND PLA 3D Printer Filament - 3D Printing PLA Filament 1.75mm, Dimensional Accuracy +/- 0.03mm - 1kg Cardboard Spool (2.2 lbs), Marble PLA
 – this can be purchased for $29.99 at the following link:
https://www.amazon.com/Inland-1-75mm-Marble-Printer-Filament/dp/B08M4733VV/ref=sr_1_3?crid=RY0788Z9D3XL&dib=eyJ2IjoiMSJ9.GvDUjGeacdaThMoKB2T31ewH9i3JmlLfhoDydChHBm-pD7cXPBEVjrKUewiIA1ZLE0_09V1n0PRn75b7hFqiDw4M0-lnl6NiRKwU4Bay_UQglrp8aVfnSITNRxxnTlk00zi7jk9JMRR5mzHilVguVNlu22jSBhxaIA2Mgu28qpM98QySMqZ0onKGj8rI2Ae99hyhSl7nTwlWuBccngRzfk5tlxoLLDb3Ck8adz-NTaQ.5vcyT03Wl1FkUx1DENvwhSOMvdqbl_TQCjXICAq7kSI&dib_tag=se&keywords=pla+filament+inland+marble&qid=1735843633&sprefix=pla+filament+inland+marble%2Caps%2C87&sr=8-3

### Software
 PrusaSlicer
 
![Image_4](https://github.com/user-attachments/assets/39432d94-ad40-4164-a282-88a7bdc576e2)


### Settings
  Layer Height: .2mm \
  Infill: 30% \
  Supports: Everywhere \
  Estimated Printing Time: 7 hours and 34 minutes

# Code
There is already a lot of available code, especially from Pimoroni themselves; I decided to take some of the available code and use ChatGPT to edit it.

## Software
I personally like to use Thonny for my editing/programming of microcontrollers, so that is what I have here.

![Image_5](https://github.com/user-attachments/assets/fa01b4ad-c60a-4ea4-b805-a1a3b18918f0)

## Code

If you do not want to download the .py file, you can just copy the following to your clipboard.

```bash
import badger2040

# Global Constants
WIDTH = badger2040.WIDTH
HEIGHT = badger2040.HEIGHT

COMPANY_HEIGHT = 30
DETAILS_HEIGHT = 20
NAME_HEIGHT = HEIGHT - COMPANY_HEIGHT - (DETAILS_HEIGHT * 2) - 2
TEXT_WIDTH = WIDTH - 1

COMPANY_TEXT_SIZE = 0.6
DETAILS_TEXT_SIZE = 0.5

LEFT_PADDING = 5
NAME_PADDING = 20
DETAIL_SPACING = 10

# ------------------------------
#      Utility functions
# ------------------------------

# Reduce the size of a string until it fits within a given width
def truncatestring(text, text_size, width):
    while display.measure_text(text, text_size) > width and len(text) > 0:
        text = text[:-1]
    return text

# ------------------------------
#      Drawing functions
# ------------------------------

# Draw the badge, including user text
def draw_badge(company, name, detail1_text, detail2_text):
    display.set_pen(0)
    display.clear()

    # Draw the company ("Teacher")
    display.set_pen(15)
    display.set_font("serif")
    company_length = display.measure_text(company, COMPANY_TEXT_SIZE)
    display.text(company, (WIDTH - company_length) // 2, (COMPANY_HEIGHT // 2) + 1, WIDTH, COMPANY_TEXT_SIZE)

    # Draw a white background behind the name
    display.set_pen(15)
    display.rectangle(1, COMPANY_HEIGHT + 1, TEXT_WIDTH, NAME_HEIGHT)

    # Draw the name, scaling it based on the available width
    display.set_pen(0)
    display.set_font("sans")
    name_size = 2.0  # A sensible starting scale
    while display.measure_text(name, name_size) >= (TEXT_WIDTH - NAME_PADDING) and name_size >= 0.1:
        name_size -= 0.01
    name_length = display.measure_text(name, name_size)
    display.text(name, (TEXT_WIDTH - name_length) // 2, (NAME_HEIGHT // 2) + COMPANY_HEIGHT + 1, WIDTH, name_size)

    # Draw a white background behind the details
    display.set_pen(15)
    display.rectangle(1, HEIGHT - DETAILS_HEIGHT * 2, TEXT_WIDTH, DETAILS_HEIGHT - 1)
    display.rectangle(1, HEIGHT - DETAILS_HEIGHT, TEXT_WIDTH, DETAILS_HEIGHT - 1)

    # Draw the first detail's text
    display.set_pen(0)
    display.set_font("sans")
    detail1_length = display.measure_text(detail1_text, DETAILS_TEXT_SIZE)
    display.text(detail1_text, (WIDTH - detail1_length) // 2, HEIGHT - ((DETAILS_HEIGHT * 3) // 2), WIDTH, DETAILS_TEXT_SIZE)

    # Draw the second detail's text
    detail2_length = display.measure_text(detail2_text, DETAILS_TEXT_SIZE)
    display.text(detail2_text, (WIDTH - detail2_length) // 2, HEIGHT - (DETAILS_HEIGHT // 2), WIDTH, DETAILS_TEXT_SIZE)

    display.update()

# ------------------------------
#        Program setup
# ------------------------------

# Create a new Badger and set it to update NORMAL
display = badger2040.Badger2040()
display.led(128)
display.set_update_speed(badger2040.UPDATE_NORMAL)
display.set_thickness(2)

# Open the badge file
company = "Profession"
name = "FIRST LAST"
detail1_text = "Subtext 1"
detail2_text = "Subtext 2"

# Truncate all of the text (except for the name as that is scaled)
company = truncatestring(company, COMPANY_TEXT_SIZE, TEXT_WIDTH)
detail1_text = truncatestring(detail1_text, DETAILS_TEXT_SIZE,
                              TEXT_WIDTH - DETAIL_SPACING - display.measure_text("", DETAILS_TEXT_SIZE))
detail2_text = truncatestring(detail2_text, DETAILS_TEXT_SIZE,
                              TEXT_WIDTH - DETAIL_SPACING - display.measure_text("", DETAILS_TEXT_SIZE))

# ------------------------------
#       Main program
# ------------------------------

draw_badge(company, name, detail1_text, detail2_text)

while True:
    # Keep the system alive to prevent power-off
    display.keepalive()

    # If on battery, halt the Badger to save power, it will wake up if any of the front buttons are pressed
    display.halt()
```

# Tips
I have been using the filament I have here because it's just available. I think this would look better in black (Prusa has a really nice galaxy black filament).

I used gorilla glue to hold the magnets in place.
