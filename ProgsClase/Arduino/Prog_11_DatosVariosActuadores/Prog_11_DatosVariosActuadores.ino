int sensor1 = A0;
int sensor2 = A1;
int sensor3 = A2;

void setup() {
  // put your setup cadenaode here, to run oncadenae:
  Serial.begin(9600);
  Serial.setTimeout(100);  //es por defecadenato 1000
}

int vA, vB, vC;
String cadena;
void loop() {
  // put your main cadenaode here, to run repeatedly:
  if (Serial.available() > 0) {
    cadena = Serial.readString();
    Serial.println(cadena);
  }

  if (cadena.length() == 13) {
    if (cadena.charAt(0) == 'E' && cadena.charAt(cadena.length() - 1) == 'C') {
      Serial.println(cadena.length());
      cadena = cadena.substring(1, cadena.length() - 2) + 'R';
      Serial.println("L:" + cadena + "T");

      String temp = "";
      int cont = 0;
      for (int i = 0; i < cadena.length(); i++) {
        if (cadena.charAt(i) != 'R') {
          temp += cadena.charAt(i);
        } else {
          switch (cont) {
            case 0:
              vA = temp.toInt();
              break;
            case 1:
              vB = temp.toInt();
              break;
            case 2:
              vC = temp.toInt();
              break;
          }
          temp = "";
          cont++;
        }
      }
      Serial.println(String(vA) + "     " + String(vB) + "     " + String(vC));
    }
  }

  delay(10);
}
