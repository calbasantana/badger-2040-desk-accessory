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
