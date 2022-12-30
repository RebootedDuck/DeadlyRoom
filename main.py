from math import trunc
from fractions import Fraction

print("Deadly Room V2.0 - Inspired by https://qr.ae/prvX6x")
print("---")

type = input("Litres or Dimensions? L/D ")

if type == "D":
    try:
        height = float(input("How high is the room in meters?: "))
        length = float(input("How long is the room in meters?: "))
        width = float(input("How wide is the room in meters?: "))
    except ValueError:
        exit("Not a Float")

    volume = height * width * length
    litres = volume * 1000
elif type == "L":
    try:
        litres = float(input("How many litres? "))
    except ValueError:
        exit("Not a Float")
else:
    exit("Invalid Type - L/D")

try:
    people = float(input("How many people in the room?: "))
except ValueError:
    exit("Not a Float")

otwo = trunc(litres / 5)
days = otwo / 550 / people
roundays = round(days, 2)
actualdays = roundays / Fraction(3, 2)
actualroundays = round(actualdays, 2)

if type == "D":
    # noinspection PyUnboundLocalVariable
    print('Room volume is ' + str(volume) + " metres cubed or " + str(litres) + " litres")
if type == "L":
    print('Room volume is ' + str(litres) + ' litres')

print('Available uncompressed oxygen is ' + str(otwo) + ' litres')
print('At maximum lung efficiency ' + str(people) + ' people could survive for ' + str(roundays) + ' days')
print('However due to oxygen deprivation the actual time is ' + str(actualroundays) + ' days')
