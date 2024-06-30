"""
Created by Angelo John Benedict Laus of SF231
Created on April 11, 2024
"""

again = 'Y'

def money_conversion():
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print("       Money Conversion\n    1. Peso to Dollar\n    2. Peso to Yen\n    3. Peso to Riyals\n")

    moncInput = float(input("  Choose a number: "))
    peso = float(input("Enter a value in Peso: "))

    match moncInput:
        case 1:
            print("The equivalent in Dollar is: %.3f" % float(peso * 0.018))
        case 2:
            print("The equivalent in Yen is: %.3f" % float(peso * 2.71))
        case 3:
            print("The equivalent in Riyals is: %.3f" % float(peso * 0.066))
        case _:
            print("Error.")

    print("\n&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")


def area_computation():
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("       Area Computation\n    1. Area of a Circle\n    2. Area of a Square\n    3. Area of a Rectangle\n")

    arcInput = float(input("  Choose a number: "))

    match arcInput:
        case 1:
            radius = float(input("Enter the value of the radius: "))
            print("The area is: %.3f" % float(3.14 * (radius ** 2)))
        case 2:
            side = float(input("Enther the value of the square's side: "))
            print("The area is: %.3f" % float(side ** 2))
        case 3:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print("The area is: %.3f" % float(length * width))
        case _:
            print("Error.")

    print("\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")



def metric_conversion():
    print("#############################")
    print("       Metric Conversion\n    1. Kilogram to Pound\n    2. Square Meter to Hectare\n    3. Gallon to Barrel\n")

    metcInput = float(input("  Choose a number: "))

    match metcInput:
        case 1:
            kilogram = float(input("Enter the value in kilograms: "))
            print("The equivalent in pounds is: %3.f" % float(kilogram * 2.205))
        case 2:
            sqm = float(input("Enter the value in square meters: "))
            print("The equivalent in hectares is: %3.f" % float(sqm * 0.0001))
        case 3:
            gallon = float(input("Enter the value in gallons: "))
            print("The equivalent in barrels is: %3.f" % float(gallon * 0.0238095))
        case _:
            print("Error.")

    print("\n#############################")


while again == 'Y':
    print("*****************************")
    print("         Main Menu\n    1. Money Conversion\n    2. Area Computation\n    3. Metric Conversion\n")

    mmInput = float(input("  Choose from the menu: "))
    print("\n*****************************\n")

    match mmInput:
        case 1:
            money_conversion()
        case 2:
            area_computation()
        case 3:
            metric_conversion()
        case _:
            print("Error.")

    again = (input("Try again? Y/N: "))