#include <LiquidCrystal.h>

LiquidCrystal lcd(4, 6, 10, 11, 12, 13);
const int pulsePin = 8;    // Signal In
const int dataPin = 2;     // Data out to Pi GPIO 23
const int clockPin = 3;    // Clock out to Pi GPIO 24

float frequency;

void setup() {
  pinMode(pulsePin, INPUT);
  pinMode(dataPin, OUTPUT);   // Data pin to Raspberry Pi
  pinMode(clockPin, OUTPUT);  // Clock pin to Raspberry Pi
  
  lcd.begin(16, 2);
  lcd.print("Arduino Powered");
  lcd.setCursor(0,1);
  lcd.print(" Freq Counter ");
  delay(2000);
}

void sendFrequency(float freq) {
  // Convert frequency to integer (multiply by 10 to keep 1 decimal place)
  long freqInt = (long)(freq * 10);
  
  // Send 32 bits of data
  digitalWrite(clockPin, LOW);
  delayMicroseconds(100);
  
  for(int i = 31; i >= 0; i--) {
    // Set data bit
    digitalWrite(dataPin, (freqInt >> i) & 1);
    delayMicroseconds(100);
    
    // Clock pulse
    digitalWrite(clockPin, HIGH);
    delayMicroseconds(100);
    digitalWrite(clockPin, LOW);
    delayMicroseconds(100);
  }
}

void loop() {
  int pulseHigh = pulseIn(pulsePin, HIGH);
  int pulseLow = pulseIn(pulsePin, LOW);
  float pulseTotal = pulseHigh + pulseLow;
  frequency = 1000000/pulseTotal;
  
  // Update LCD
  lcd.setCursor(0,0);
  lcd.print("Frequency is ");
  lcd.setCursor(0,1);
  lcd.print(" ");
  lcd.setCursor(0,1);
  lcd.print(frequency);
  lcd.print(" Hz");
  
  // Send to Raspberry Pi
  sendFrequency(frequency);
  
  delay(100);  // Reduced delay for faster updates
}
