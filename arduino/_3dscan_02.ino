#include <AFMotoralt.h>
#include <stdlib.h>
#include <EEPROM.h>
#include <MsTimer2.h>

AF_Stepper oki(200, 2);              // 200 steps/rotation on port 2
const int ledPin = 13; // the pin that the LED is attached to
const int leftLaserPin = 9; // the pin that the LED is attached to
const int rightLaserPin = 10; // the pin that the LED is attached to
const int testpin = 3;
int incomingByte;      // a variable to read incoming serial data into

long laststep = 0;
long ontime = 200;

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(ledPin, OUTPUT);
  pinMode(leftLaserPin, OUTPUT);
  pinMode(rightLaserPin, OUTPUT);
  pinMode(testpin, INPUT);
  digitalWrite(testpin, HIGH);
  oki.setSpeed(10);
}

void loop() {
  // see if there's incoming serial data:
  if (Serial.available() > 0) {
    // read the oldest byte in the serial buffer:
    incomingByte = Serial.read();
    // if it's a capital H (ASCII 72), turn on the LED:
    if (incomingByte == 'F') {
      digitalWrite(ledPin, HIGH);
      oki.step(1, FORWARD, INTERLEAVE);
      laststep = millis();
    }
    if (incomingByte == 'B') {
      digitalWrite(ledPin, HIGH);
      oki.step(1, BACKWARD, INTERLEAVE);
      laststep = millis();
    }
    // if it's an L (ASCII 76) turn off the LED:
    if (incomingByte == 'K') {
      digitalWrite(ledPin, LOW);
    }
    if (incomingByte == 'T') {
      digitalWrite(ledPin, HIGH);
      oki.step(400, FORWARD, INTERLEAVE);
      laststep = millis();
    }
    if (incomingByte == 'O') {
      digitalWrite(ledPin, HIGH);
      oki.step(400, BACKWARD, INTERLEAVE);
      laststep = millis();
    }
    if (incomingByte == 'L') {
      digitalWrite(leftLaserPin, HIGH);
    }
    if (incomingByte == 'R') {
      digitalWrite(rightLaserPin, HIGH);
    }
    if (incomingByte == 'l') {
      digitalWrite(leftLaserPin, LOW);
    }
    if (incomingByte == 'r') {
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
