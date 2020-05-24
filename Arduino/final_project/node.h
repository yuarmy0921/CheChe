/***************************************************************************/
// File			  [node.h]
// Author		  [Erik Kuo, Joshua Lin]
// Synopsis		[Code for managing car movement when encounter a node]
// Functions  [/* add on yout own! */]
// Modify		  [2020/03/027 Erik Kuo]
/***************************************************************************/

#include <SoftwareSerial.h>
#include <Wire.h>

/*===========================import variable===========================*/
int extern r1, l1, r2, l2, r3, l3;
int extern _Tp;
/*===========================import variable===========================*/

// TODO: add some function to control your car when encounter a node
// here are something you can try: left_turn, right_turn... etc.

void right_turn(){
   MotorWriting(150,150);
   delay(280);//860isok
   MotorWriting(0,0);
   delay(1000);
   MotorWriting(100,-100);
   delay(250);//860isok
   MotorWriting(0,0);
   delay(1000);
  l3 = analogRead(L3);
  l2 = analogRead(L2);
  l1 = analogRead(L1);
  r1 = analogRead(R1);
  r2 = analogRead(R2);
  r3 = analogRead(R3);
   while(l1+l2+l3+r1+r2<900){
     l3 = analogRead(L3);
  l2 = analogRead(L2);
  l1 = analogRead(L1);
  r1 = analogRead(R1);
  r2 = analogRead(R2);
  r3 = analogRead(R3);
     MotorWriting(70,-70);
     delay(100);
     MotorWriting(0,0);
     delay(10);
   }
   MotorWriting(0,0);
     delay(500);
   Serial.println("trun over");
   
 
}
void left_turn(){
 MotorWriting(-80,80);
   delay(400);//860isok
   MotorWriting(0,0);
   delay(2000);
    l3 = analogRead(L3);
  l2 = analogRead(L2);
  l1 = analogRead(L1);
  r1 = analogRead(R1);
  r2 = analogRead(R2);
  r3 = analogRead(R3);
   while(l1+l2+l3+r1+r2+r3<1000){
     l3 = analogRead(L3);
  l2 = analogRead(L2);
  l1 = analogRead(L1);
  r1 = analogRead(R1);
  r2 = analogRead(R2);
  r3 = analogRead(R3);
     MotorWriting(0,80);
     delay(200);
     MotorWriting(0,0);
     delay(100);
   }
   Serial.println("trun over");
}
void U_turn(){
   //MotorWriting(70,76);
   //delay(500);
   MotorWriting(100,-100);
   delay(700);//860isok
   MotorWriting(0,0);
   delay(2000);
    l3 = analogRead(L3);
  l2 = analogRead(L2);
  l1 = analogRead(L1);
  r1 = analogRead(R1);
  r2 = analogRead(R2);
  r3 = analogRead(R3);
   while(l1+l2+l3+r1+r2<900){
     l3 = analogRead(L3);
  l2 = analogRead(L2);
  l1 = analogRead(L1);
  r1 = analogRead(R1);
  r2 = analogRead(R2);
  r3 = analogRead(R3);
     MotorWriting(70,0);
     delay(100);
     MotorWriting(0,0);
     delay(10);
   }
   Serial.println("trun over");
}
