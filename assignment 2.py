import random
Humidity= random.randint(40,90)
Temperature=random.randint(40,90)
if(Temperature<50 and Humidity<45):
  print("NO HARM")
elif (Temperature<50 or Humidity<45):
  if (Temperature<50 or Humidity>45):
    print("HUMIDITY ALERT")
  elif(Temperature>50 or Humidity<45):
    print("TEMPERATURE ALERT")
else:
  print("THE AREA SHOULD BE CLEARED IMMEDIATELY")