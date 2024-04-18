print("an air condition bus charge")
distance=int(input(" enter ur  distance km:"))
if distance<=10:
    charge = distance * 80
elif distance>=11 and distance<=20:
    charge = distance * 6 + 80
elif distance >= 21 and distance <= 30:
    charge = distance * 5 + 80
elif distance >= 31:
    charge = distance * 4 + 80
print(charge)
