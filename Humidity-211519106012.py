import random
Humidity= random.randint(70,85)
Temperature=random.randint(70,85)
if(Temperature<60 and Humidity<45):
  print("NO HARM")
elif (Temperature<60 or Humidity<45):
  if (Temperature<60 or Humidity>45):
    print("HUMIDITY ALERT")
  elif(Temperature>60 or Humidity<45):
    print("TEMPERATURE ALERT")
else:
  print("THE AREA SHOULD BE CLEARED IMMEDIATELY")
