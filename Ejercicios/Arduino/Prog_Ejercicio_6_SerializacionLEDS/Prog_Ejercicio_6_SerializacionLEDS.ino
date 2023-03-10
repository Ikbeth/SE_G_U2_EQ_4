String texto,cadena,L[3];
int inicio,fin,i,led1=3,led2=4,led3=5;

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);//ms por defecto 1000
}

void loop() {
  i=0;
  inicio=0;
  
  if(Serial.available()>0){
    cadena = Serial.readString();//E001R056R255C 
    Serial.println(cadena);
      
    fin=cadena.indexOf("",inicio); 
     
    while (fin!=-1) {
    texto = cadena.substring(inicio, fin); 
    L[i]=texto;

    inicio = fin+1;
    fin = cadena.indexOf(',', inicio);
    i++;
  }
  
  texto=cadena.substring(inicio,cadena.length());
  L[3]=texto;
  
  analogWrite(led1,L[1].toInt());
  analogWrite(led2,L[2].toInt());
  analogWrite(led3,L[3].toInt());
  delay(1000);
  }
}
