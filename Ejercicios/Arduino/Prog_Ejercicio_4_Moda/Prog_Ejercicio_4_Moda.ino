int pot = A0;
int tamMuestra = 30;

void setup() {
  Serial.begin(9600);
}

int moda, i, j, aux;
void loop() {

  int datos[tamMuestra];

  for (i = 0; i < tamMuestra; i++) {
    datos[i] = analogRead(pot);
  }

  //Obtener la moda
  int contRepeticiones = 0; //Es el valor de el numero que mas se va a repetir
  for(i = 0; i < tamMuestra; i++){
    int numValIguales = 0; //El numero de repeticiones de cada numero 
    for(j = 0; j < tamMuestra; j++){
      if(datos[i] == datos[j]){ 
        numValIguales++; // comparamos valores y contamos si son iguales
      }
      if(contRepeticiones < numValIguales){
        contRepeticiones = numValIguales;
        moda = datos[i];
      }
    }
  } 

  Serial.println(moda);
  delay(1000);
}
