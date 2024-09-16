#include <Servo.h>

Servo myServo;  // Create a Servo object
int servoPin = 9;  // Define the pin connected to the servo signal

void setup() {
  myServo.attach(servoPin);  // Attach the servo to the pin
  Serial.begin(9600);  // Start the serial communication
}

void loop() {
  if (Serial.available() > 0) {
    int angle = Serial.parseInt();  // Read the angle from the serial input
    if (angle >= 0 && angle <= 180) {
      myServo.write(angle);  // Set the servo position
      Serial.print("Servo moved to angle: ");
      Serial.println(angle);
    } else {
      Serial.println("Please enter a valid angle between 0 and 180.");
    }
  }
}
