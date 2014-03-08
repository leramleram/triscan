#include <AFMotoralt.h>
#include <stdlib.h>
#include <EEPROM.h>
#include <MsTimer2.h>

AF_Stepper oki(200, 2);      // 200 steps/rotation on port 2
const int leftLaserPin = 9; // Left Laser Pin
const int rightLaserPin = 10; // Right Laser Pin
const int testpin = 3;		//the button for testing
int data;      // data from the host

long laststep = 0;
long ontime = 200;

void setup() {
  Serial.begin(9600);
  pinMode(leftLaserPin, OUTPUT);
  pinMode(rightLaserPin, OUTPUT);
  pinMode(testpin, INPUT);
  digitalWrite(testpin, HIGH);
  oki.setSpeed(10);
}

void loop() {
  if (Serial.available() > 0) {
    data = Serial.read();
    if (data == 'F') {
      oki.step(1, FORWARD, INTERLEAVE);
      laststep = millis();
    }
    if (data == 'B') {
      oki.step(1, BACKWARD, INTERLEAVE);
      laststep = millis();
    }
    if (data == 'T') {
      oki.step(400, FORWARD, INTERLEAVE);
      laststep = millis();
    }
    if (data == 'O') {
      oki.step(400, BACKWARD, INTERLEAVE);
      laststep = millis();
    }
    if (data == 'L') {
      digitalWrite(leftLaserPin, HIGH);
    }
    if (data == 'R') {
      digitalWrite(rightLaserPin, HIGH);
    }
    if (data == 'l') {
      digitalWrite(leftLaserPin, LOW);
    }
    if (data == 'r') {
      digitalWrite(rightLaserPin, LOW);
    }
  }
  if (digitalRead(testpin) == LOW) {
    oki.step(800, FORWARD, INTERLEAVE);
    laststep = millis();
  }
  
  if (millis() - laststep >= ontime)
    oki.release();
 
}
