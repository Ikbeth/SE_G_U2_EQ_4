int valor;

void setup() {
  // put your setup code here, to run once:
  valor = 0;
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  valor++;
  Serial.println(valor);
  delay(100);
}
