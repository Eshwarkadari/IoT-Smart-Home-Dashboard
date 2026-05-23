// ============================================================
// Arduino Sensor Node — IoT Smart Home Dashboard
// Author: Kadari Eshwar | B.Tech ECE, JNTU Hyderabad
// Sensors: DHT22, PIR, LDR, MQ-2
// ============================================================

#include <DHT.h>
#include <SoftwareSerial.h>

#define DHT_PIN     2
#define PIR_PIN     3
#define LDR_PIN     A0
#define GAS_PIN     A1
#define DHT_TYPE    DHT22

DHT dht(DHT_PIN, DHT_TYPE);

void setup() {
  Serial.begin(9600);
  pinMode(PIR_PIN, INPUT);
  dht.begin();
  Serial.println("Smart Home Sensor Node Ready!");
}

void loop() {
  float temperature = dht.readTemperature();
  float humidity    = dht.readHumidity();
  int   motion      = digitalRead(PIR_PIN);
  int   light       = analogRead(LDR_PIN);
  int   gas         = analogRead(GAS_PIN);

  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("ERROR: DHT sensor read failed!");
    delay(2000);
    return;
  }

  // Send as JSON over Serial (to Raspberry Pi)
  Serial.print("{");
  Serial.print("\"temperature\":"); Serial.print(temperature);
  Serial.print(",\"humidity\":");  Serial.print(humidity);
  Serial.print(",\"motion\":");    Serial.print(motion);
  Serial.print(",\"light\":");     Serial.print(light);
  Serial.print(",\"gas\":");       Serial.print(gas);
  Serial.println("}");

  delay(5000);  // Read every 5 seconds
}
