int led1 = 2, led2 = 3, led3 = 4, led4 = 5, led5 = 6, led6 = 7, led7 = 8, led8 = 9;

void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
  pinMode(led7, OUTPUT);
  pinMode(led8, OUTPUT);
  Serial.setTimeout(10);
}
int v;
void loop() {
  if(Serial.available() > 0){
    //Leer el valor que viene de python
    int leds[] = { 0, 0, 0, 0, 0, 0, 0, 0};
    v = Serial.readString().toInt();
    Serial.println(v);
    //Pasar a binario
    int x = 7;
    for (int i = 0; i < 8; i++){
      
      if (v > 0) {
        Serial.println(v);
        int aux = v / 2;
        int res = v % 2;
        leds[x] = res;
        v = v - (res + aux);
        x--;
      }else{
        i = 8;
      }
  }
  digitalWrite(led1, leds[0]);
  digitalWrite(led2, leds[1]);
  digitalWrite(led3, leds[2]);
  digitalWrite(led4, leds[3]);
  digitalWrite(led5, leds[4]);
  digitalWrite(led6, leds[5]);
  digitalWrite(led7, leds[6]);
  digitalWrite(led8, leds[7]);

}

  delay(4000);
}
