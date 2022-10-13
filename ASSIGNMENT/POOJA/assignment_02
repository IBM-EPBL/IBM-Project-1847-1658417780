int pirsensor = 0;

void setup()
{
  pinMode(2, INPUT);
  pinMode(13, OUTPUT);
  Serial.begin(9600);

}

void loop()
{
  pirsensor = digitalRead(2);
  if (pirsensor == 1) {
    digitalWrite(13, HIGH);
    Serial.println("Motion detected , presence of human or animals");
  } else {
    digitalWrite(13, LOW);
    Serial.println("Motion not detected");
  }
  delay(1000); // Wait for 1000 millisecond(s)
}
