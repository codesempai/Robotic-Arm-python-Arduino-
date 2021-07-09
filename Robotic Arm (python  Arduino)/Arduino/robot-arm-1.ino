#include <Servo.h>

//defining the servos
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;

//servo position in degree!
int pos = 0;
int pos1 = 90;

void setup() {
  servo1.attach(8);     //middle   //yellow
  servo2.attach(9);    //up-down  //orange
  servo3.attach(10);  //rotation //black
  servo4.attach(11); //hand     //red
}



void loop() {
//default
//rotation/hand/up-down
for(pos = 0;pos<=0;pos+=1){
servo4.write(pos);
servo3.write(pos);
servo2.write(pos);
delay(25);}

//middle
for(pos = 40;pos<=40;pos+=1){
servo1.write(pos);
delay(25);}

delay(2000);















//rotation1
for(pos = 0;pos<=160;pos+=1){
servo3.write(pos);
delay(25);}

//middle
for(pos = 0;pos<=0;pos+=1){
servo1.write(pos);
delay(25);}

//open hand
for(pos = 0;pos<=90;pos+=1){
servo4.write(pos);
delay(25);}

//up
for(pos = 0;pos<=180;pos+=1){
servo2.write(pos);
delay(25);}

//middle
for(pos = 0;pos<=90;pos+=1){
servo1.write(pos);
delay(25);}

//close hand
for(pos = 90;pos>=0;pos-=1){
servo4.write(pos);
delay(25);}


//middle
for(pos = 90;pos>=30;pos-=1){
servo1.write(pos);
delay(25);}

//down
for(pos = 180;pos>=0;pos-=1){
servo2.write(pos);
delay(25);}

//rotation
for(pos = 160;pos>=0;pos-=1){
servo3.write(pos);
delay(25);}


//middle
for(pos = 0;pos<=0;pos+=1){
servo1.write(pos);
delay(25);}

//up
for(pos = 0;pos<=180;pos+=1){
servo2.write(pos);
delay(25);}


//middle
for(pos = 0;pos<=180;pos+=1){
servo1.write(pos);
delay(25);}

//open hand
for(pos = 0;pos<=90;pos+=1){
servo4.write(pos);
delay(25);}

//close hand
for(pos = 90;pos>=0;pos-=1){
servo4.write(pos);
delay(25);}


//middle
for(pos = 180;pos>=30;pos-=1){
servo1.write(pos);
delay(25);}
//down
for(pos = 180;pos>=0;pos-=1){
servo2.write(pos);
delay(25);}

delay(9000);


}
