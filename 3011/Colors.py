"""Colors"""

Colors1 = input()
Colors2 = input()
if (Colors1 == "Red" and Colors2 == "Yellow")or(Colors1 == "Yellow" and Colors2 == "Red"):
    print("Orange")
elif (Colors1 == "Red" and Colors2 == "Blue")or(Colors1 == "Blue" and Colors2 == "Red"):
    print("Violet")
elif (Colors1 == "Yellow" and Colors2 == "Blue")or(Colors1 == "Blue" and Colors2 == "Yellow"):
    print("Green")
elif (Colors1 == "Red" and Colors2 == "Red"):
    print("Red")
elif (Colors1 == "Yellow" and Colors2 == "Yellow"):
    print("Yellow")
elif (Colors1 == "Blue" and Colors2 == "Blue"):
    print("Blue")
else:
    print("Error")
