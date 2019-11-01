#include <Servo.h>
//Pines utilizados
int verde2 = 8;
int amarillo2 = 9;
int rojo2 = 10;
int rojo = 11;
int amarillo = 12;
int verde = 13;
int tiempoEspera = 5000;
int tiempoCambio = 1000;
long valor;
Servo servo1;

void setup() {
  // put your setup code here, to run once:
  pinMode(verde, OUTPUT);
  pinMode(amarillo, OUTPUT);
  pinMode(rojo, OUTPUT);
  pinMode(verde2, OUTPUT);
  pinMode(amarillo2, OUTPUT);
  pinMode(rojo2, OUTPUT);
  Serial.begin(9600);
  // APAGAR TODOS LOS LEDS
  digitalWrite(verde, LOW);
  digitalWrite(amarillo, LOW);
  digitalWrite(rojo, LOW);
  digitalWrite(verde2, LOW);
  digitalWrite(amarillo2, LOW);
  digitalWrite(rojo2, LOW);
  //ESTADO INICIAL
  digitalWrite(rojo2, HIGH);
  servo1.attach(6);
}

void loop() {
  valor = analogRead(A0);
  //Serial.println(valor); Si desea conocer el valor
  // put your main code here, to run repeatedly:
  servo1.write(0);
  delay(5000);
  servo1.write(180);
  delay(5000);
  Serial.println(valor);
 
if(valor > 800){
  tiempoEspera = tiempoEspera - valor*4;
  tiempoCambio = tiempoCambio - valor;
  encenderS1();
  encenderS2();
}else if(valor > 400){
  tiempoEspera = tiempoEspera - valor*2;
  tiempoCambio = tiempoCambio - valor;
  encenderS1();
  encenderS2();
}else{
  encenderS1();
  encenderS2();
}

tiempoEspera = 5000;
tiempoCambio = 1000;

}

void encenderS1(){
  digitalWrite(rojo, HIGH);
  digitalWrite(amarillo, LOW);
  digitalWrite(verde, LOW);
  delay(tiempoEspera);
  digitalWrite(rojo, LOW);
  digitalWrite(amarillo, HIGH);
  digitalWrite(verde, LOW);
  delay(tiempoCambio);
  digitalWrite(rojo, LOW);
  digitalWrite(amarillo, LOW);
  digitalWrite(verde, HIGH);
  delay(tiempoEspera);
  digitalWrite(rojo, LOW);
  digitalWrite(amarillo, HIGH);
  digitalWrite(verde, LOW);
  delay(tiempoCambio);
  digitalWrite(rojo, HIGH);
  digitalWrite(amarillo, LOW);
  digitalWrite(verde, LOW);
  delay(tiempoCambio);
}

void encenderS2(){
  digitalWrite(rojo2, HIGH);
  digitalWrite(amarillo2, LOW);
  digitalWrite(verde2, LOW);
  delay(tiempoEspera);
  digitalWrite(rojo2, LOW);
  digitalWrite(amarillo2, HIGH);
  digitalWrite(verde2, LOW);
  delay(tiempoCambio);
  digitalWrite(rojo2, LOW);
  digitalWrite(amarillo2, LOW);
  digitalWrite(verde2, HIGH);
  delay(tiempoEspera);
  digitalWrite(rojo2, LOW);
  digitalWrite(amarillo2, HIGH);
  digitalWrite(verde2, LOW);
  delay(tiempoCambio);
  digitalWrite(rojo2, HIGH);
  digitalWrite(amarillo2, LOW);
  digitalWrite(verde2, LOW);
  delay(tiempoCambio);
}
