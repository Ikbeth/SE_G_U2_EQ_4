//Sensores analógicos. ->

int sensor1 = A0;
int sensor2 = A1;
int sensor3 = A2;

void setup() {
  // put your setup cadenaode here, to run oncadenae:
  Serial.begin(9600);
  Serial.setTimeout(100);  //es por defecadenato 1000
}

int sA, sB, sC;
void loop() {
  // put your main cadenaode here, to run repeatedly:
  sA = analogRead(sensor1);
  sB = analogRead(sensor2);
  sC = analogRead(sensor3);

  //llenar la cadena que se enviara
  String cadena = "P" + String(sA) + " " + String(sB) + " " + String(sC) + "K";

  Serial.println(cadena);

  delay(500);
}
