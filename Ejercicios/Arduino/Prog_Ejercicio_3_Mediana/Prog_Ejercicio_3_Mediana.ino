int pot = A0;
int tamMuestra = 29;

void setup() {
  Serial.begin(9600);
}

int mediana, i, j, aux;
void loop() {

  int datos[tamMuestra];

  for (i = 0; i < tamMuestra; i++) {
    datos[i] = analogRead(pot);
  }
  // ordenamiendo de datos para obtener mediana usando met: Burbuja

  for (i = 0; i < tamMuestra; i++) {
    for (j = 0; j < tamMuestra; j++) {
      if (datos[j + 1] < datos[i]) {
        aux = datos[j + 1];
        datos[j + 1] = datos[i];
        datos[i] = aux;
      }
    }
  }

  mediana = datos[tamMuestra / 2];

  Serial.println(mediana);
  delay(100);
}
