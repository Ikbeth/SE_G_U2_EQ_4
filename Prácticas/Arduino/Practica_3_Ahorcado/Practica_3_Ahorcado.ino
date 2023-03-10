int p1 = 2, p2 = 3, p3 = 4;
int correcto = 8, incorrecto = 9;
void setup() {
  // put your setup code here, to run once:
  pinMode(correcto, OUTPUT);
  pinMode(incorrecto, OUTPUT);

  pinMode(p1, INPUT_PULLUP);
  pinMode(p2, INPUT_PULLUP);
  pinMode(p3, INPUT_PULLUP);
  Serial.begin(9600);
}
int estado;
void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available() > 0){
    estado = Serial.readString().toInt();
    Serial.println(estado);

    if(estado == 0){
      digitalWrite(correcto, 0);
      digitalWrite(incorrecto, 1);
    } 
    if(estado == 1){
      digitalWrite(correcto, 1);
      digitalWrite(incorrecto, 0);
    }
  }

  if (digitalRead(p1) == 0){
    Serial.println("Anterior");
  }
  else if (digitalRead(p2) == 0){
    Serial.println("Siguiente");
  }
  else if (digitalRead(p3) == 0){
    Serial.println("Seleccionar");
  }
  delay(150);
}
