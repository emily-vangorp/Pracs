COLOUR_NAMES = {"AliceBlue": "#f0f8ff", "Black": "#000000", "Beige": "#f5fdc", "BlueViolet": "#8a2be2",
                "CadetBlue": "#5f9ea0", "Chocolate": "#d2691e", "Coral": "#ff7f50", "DarkGreen": "#006400",
                "LawnGreen": "7cfc00", "Linen": "#faf0e6"}

colour = input("Colour: ")
while colour != "":
    if colour in COLOUR_NAMES:
        print(colour, "is", COLOUR_NAMES[colour])
    else:
        print("Invalid colour name.")
    colour = input("Colour: ")
