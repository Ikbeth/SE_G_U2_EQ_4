int potenciometro = A0;
int tamMuestra = 10;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}
int valMenor = 9999;
int i, valor;
void loop() {
  // precesar datos
  for (i = 0; i < tamMuestra; i++) {
    valor = analogRead(potenciometro);
    if (valor < valMenor) {
      valMenor = valor;
    }
  }


  //Serial.println("valor= " + String(valor))
  Serial.println(valMenor);
  delay(1000);
}
