#include <Adafruit_MotorShield.h>
#include <Wire.h> 
#include <Process.h>

// Setup MotorShield and Motors
Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *m2 = AFMS.getMotor(2);
Adafruit_DCMotor *m3 = AFMS.getMotor(3);
Adafruit_DCMotor *m4 = AFMS.getMotor(4);

// Number of tics received from rotary encoders per rotation (adjust for tuning)
int ticsprotation = 50;
int mspeed = 50;

void setup() {
  Serial.begin(9600);
  // A and B pins for motor 2,4, and 3, respectively
  pinMode(28, INPUT);
  pinMode(29, INPUT);
  pinMode(24, INPUT);
  pinMode(25, INPUT);
  pinMode(26, INPUT);
  pinMode(27, INPUT);
  // pin for initialize button
  pinMode(53, INPUT);

  // Initialize shield and motors
  AFMS.begin();
  m2->setSpeed(mspeed);
  m2->run(FORWARD);
  m2->run(RELEASE);
  m3->setSpeed(mspeed);
  m3->run(FORWARD);
  m3->run(RELEASE);
  m4->setSpeed(mspeed);
  m4->run(FORWARD);
  m4->run(RELEASE);

  // Initialize bridge to python file
  Bridge.begin();
}

void track_tics(int a, int b, int duration) {
  int A = 1;
  int B = 0;
  
  while (A < duration) {
    while (B < A) {
    if (digitalRead(a) && !digitalRead(b)) {
      ++B;
    }
  }
  delay(100);
  while (A == B) {
    if (digitalRead(a) && !digitalRead(b)) {
      ++A;
    }
  }
  }
  return NULL;
}

void forward(int distance) {
  int tics = 0;
  tics = (distance / 6) * ticsprotation;
  m2->run(BACKWARD);
  m4->run(FORWARD);
  m2->setSpeed(mspeed);
  m4->setSpeed(mspeed);
  track_tics(tics, 28, 29);
  m2->setSpeed(0);
  m4->setSpeed(0);
  m2->run(RELEASE);
  m4->run(RELEASE);
}
void back(int distance) {
  int tics = 0;
  tics = (distance / 6) * ticsprotation;
  m2->run(FORWARD);
  m4->run(BACKWARD);
  m2->setSpeed(mspeed);
  m4->setSpeed(mspeed);
  track_tics(tics, 28, 29);
  m2->setSpeed(0);
  m4->setSpeed(0);
  m2->run(RELEASE);
  m4->run(RELEASE);
}
void right(int distance) {
  rotate(5,0);
  int tics = 0;
  tics = (distance / 6) * ticsprotation;
  m2->run(BACKWARD);
  m4->run(FORWARD);
  m2->setSpeed(mspeed);
  m4->setSpeed(mspeed);
  track_tics(tics, 28, 29);
  m2->setSpeed(0);
  m4->setSpeed(0);
  m2->run(RELEASE);
  m4->run(RELEASE);
  rotate(5,1);
  

  
  //int tics = 0;
  //tics = (distance / 6) * ticsprotation;
  //m3->run(FORWARD);
  //m4->run(BACKWARD);
  //m3->setSpeed(mspeed);
  //m4->setSpeed(mspeed);
  //track_tics(tics, 24, 25);
  //m3->setSpeed(0);
  //m4->setSpeed(0);
  //m3->run(RELEASE);
  //m4->run(RELEASE);
}
void left(int distance) {
  rotate(5,1);
  int tics = 0;
  tics = (distance / 6) * ticsprotation;
  m2->run(BACKWARD);
  m4->run(FORWARD);
  m2->setSpeed(mspeed);
  m4->setSpeed(mspeed);
  track_tics(tics, 28, 29);
  m2->setSpeed(0);
  m4->setSpeed(0);
  m2->run(RELEASE);
  m4->run(RELEASE);
  rotate(5,0);

  
  //int tics = 0;
  //tics = (distance / 6) * ticsprotation;
  //m3->run(BACKWARD);
  //m2->run(FORWARD);
  //m3->setSpeed(mspeed);
  //m2->setSpeed(mspeed);
  //track_tics(tics, 28, 29);
  //m3->setSpeed(0);
  //m2->setSpeed(0);
  //m3->run(RELEASE);
  //m2->run(RELEASE);
}
void rotate(int distance, int backorforw) {
  int tics = 0;
  int mspeed = 93;
  tics = distance/6 * ticsprotation; //(distance / 6) * ticsprotation;
  if (backorforw == 1) {
  m3->run(FORWARD);
  m2->run(FORWARD);
  m4->run(FORWARD);
  m4->setSpeed(mspeed);
  m3->setSpeed(mspeed);
  m2->setSpeed(mspeed);
  track_tics(tics, 28, 29);
  m3->setSpeed(0);
  m4->setSpeed(0);
  m2->setSpeed(0);
  m3->run(RELEASE);
  m2->run(RELEASE);
  m4->run(RELEASE);
  } 
  else {
  m3->run(BACKWARD);
  m2->run(BACKWARD);
  m4->run(BACKWARD);
  m4->setSpeed(mspeed);
  m3->setSpeed(mspeed);
  m2->setSpeed(mspeed);
  track_tics(tics, 28, 29);
  m3->setSpeed(0);
  m4->setSpeed(0);
  m2->setSpeed(0);
  m3->run(RELEASE);
  m2->run(RELEASE);
  m4->run(RELEASE);
  }

}

char pyin = ' ';
void loop() {
  Process p;
  p.begin("/Documents/CodeBase/HackMIT/convertlettertocommand.py");

  if (Serial.available()) {
      pyin = Serial.read();
      Serial.print("I received: ");
      Serial.println(pyin);
    }
  delay(1000);
}
