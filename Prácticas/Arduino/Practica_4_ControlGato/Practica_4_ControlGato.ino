int pulsadorLe = 13;
int pulsadorUp = 12;
int pulsadorDo = 11;
int pulsadorRi = 10;
int pulsadorSELECT = 8;

void setup() {
  // put your setup code here, to run once:
  pinMode(pulsadorUp, INPUT_PULLUP);
  pinMode(pulsadorLe, INPUT_PULLUP);  
  pinMode(pulsadorRi, INPUT_PULLUP);
  pinMode(pulsadorDo, INPUT_PULLUP);
  pinMode(pulsadorSELECT, INPUT_PULLUP);

  Serial.begin(9600);

}

int coordX = 0;
int coordY = 0;
String coordenadas = "";
void loop() {
  // put your main code here, to run repeatedly:
  if (digitalRead(pulsadorUp) == 0) {
    //Serial.println("arriba");
    coordY++;
    if (coordY >= 3) {
      coordY = 2;
    }
    //Serial.print(coordY);
    }

  if (digitalRead(pulsadorLe) == 0) {
    //Serial.println("izquierda");
    coordX--;
    if (coordX <= -1) {
      coordX = 0;
    }
    //Serial.print(coordX);
  }

  if (digitalRead(pulsadorRi) == 0) {
    //Serial.println("derecha");
    coordX++;
    if (coordX >= 3) {
      coordX = 2;
    }
    //Serial.print(coordX);
  }

  if (digitalRead(pulsadorDo) == 0) {
    //Serial.println("abajo");
    coordY--;
    if (coordY <= -1) {
      coordY = 0;
    }
    //Serial.print(coordY);
  }

  if (digitalRead(pulsadorSELECT) == 0) {
    Serial.println("seleccionar");
  }

  coordenadas = String(coordX) + "," + String(coordY);
  Serial.println(coordenadas);

  delay(100);

}
