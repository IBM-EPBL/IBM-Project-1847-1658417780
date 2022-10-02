import random
Humidity= random.randint(60,70)
Temperature=random.randint(60,70)
if(Temperature<65 and Humidity<35):
  print("NO HARM")
elif (Temperature<65 or Humidity<35):
  if (Temperature<65 or Humidity>35):
    print("HUMIDITY ALERT")
  elif(Temperature>65 or Humidity<35):
    print("TEMPERATURE ALERT")
else:
  print("THE AREA SHOULD BE CLEARED IMMEDIATELY")
