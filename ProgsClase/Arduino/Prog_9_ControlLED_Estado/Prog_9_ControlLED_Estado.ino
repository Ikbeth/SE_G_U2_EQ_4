int led = 13;

void setup() {
  // put your setup code here, to run once:
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(100);  //es por defecto 1000
}

int estado = 0;
void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0) {
    int estado = Serial.readString().toInt();
    digitalWrite(led, estado);
  }
  Serial.println(estado);
  delay(10);
}
