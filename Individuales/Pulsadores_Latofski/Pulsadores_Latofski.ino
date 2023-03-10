int pul = 2;
int estado;
void setup() {
  // put your setup code here, to run once:
  pinMode(pul, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  estado = digitalRead(pul);
  delay(50);
  Serial.println(estado);
}
