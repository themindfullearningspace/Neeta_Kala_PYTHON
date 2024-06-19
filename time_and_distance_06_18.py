#Taking input for time and distance
distance = float(input("Enter the distance covered(in kilometers): "))
time = float(input("Enter the time taken to cover the distance(in hours): "))

if time != 0:
  speed = distance / time
  print(f"The speed is {speed} in kilometers per hour.")
else:
  print("Time can not be zero.")