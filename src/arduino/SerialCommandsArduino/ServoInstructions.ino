#include "Servo.h"
Servo servo1;
Servo servo2;
Servo servo3;

String instruction = "";

int incomingByte = 0; // for incoming serial data

void setup() {
  Serial.begin(9600); // opens serial port, sets data rate to 9600 bps
  digitalWrite(13, HIGH);

  servo1.attach(9);
  servo2.attach(10);
  servo3.attach(11);
  
  servo1.write(180);
}

void loop() {
  if (Serial.available() > 0) {
    instruction = Serial.readStringUntil('\n');

    if(instruction.charAt(0) == 'Q') 
    {
      int servoNumber = instruction.charAt(1) - '0';

      float angle = instruction.substring(3).toFloat();

      Serial.print("Servo: ");
      Serial.print(servoNumber);
      Serial.print(" Angle: ");
      Serial.println(angle);

      switch(servoNumber)
      {
        case 1:
          servo1.write(angle);
          break;
        case 2:
          servo2.write(angle);
          break;
        case 3: 
          servo3.write(angle);
          break;
      }


    }
  }
}