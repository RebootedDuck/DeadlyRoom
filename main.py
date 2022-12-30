import math
import fractions

print("Deadly Room V2.0 - Inspired by https://qr.ae/prvX6x")
print("---")

type = input("Litres or Dimensions? L/D ")

if type == "D":
    height = float(input("How high is the room in meters?: "))
    length = float(input("How long is the room in meters?: "))
    width = float(input("How wide is the room in meters?: "))
    volume = height * width * length
    litres = volume * 1000
else:
    litres = float(input("How many litres? "))

people = float(input("How many people in the room?: "))
otwo = math.trunc(litres / 5)
days = otwo / 550 / people
roundays = round(days, 2)
actualdays = roundays / fractions.Fraction(3, 2)
actualroundays = round(actualdays, 2)

if type == "D":
    print('Room volume is ' + str(volume) + " metres cubed or " + str(litres) + " litres")
if type == "L":
    print('Room volume is ' + str(litres) + ' litres')

print('Available uncompressed oxygen is ' + str(otwo) + ' litres')
print('At maximum lung efficiency ' + str(people) + ' people could survive for ' + str(roundays) + ' days')
print('However due to oxygen deprivation the actual time is ' + str(actualroundays) + ' days')

