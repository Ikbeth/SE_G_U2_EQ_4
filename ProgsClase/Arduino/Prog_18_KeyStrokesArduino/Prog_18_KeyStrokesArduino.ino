//Sensores analógicos. ->

int pulsador1 = 4;
int pulsador2 = 5;

void setup() {
  // put your setup cadenaode here, to run oncadenae:
  pinMode(pulsador1, INPUT_PULLUP);
  pinMode(pulsador2, INPUT_PULLUP);

  Serial.begin(9600);
  Serial.setTimeout(100);  //es por defecadenato 1000
}

int sA, sB;
void loop() {
  // put your main cadenaode here, to run repeatedly:
  sA = digitalRead(pulsador1) == 1?0:1;
  sB = digitalRead(pulsador2) == 1?0:1;

  //llenar la cadena que se enviara
  String cadena = String(sA) + " " + String(sB);

  Serial.println(cadena);

  delay(100);
}
