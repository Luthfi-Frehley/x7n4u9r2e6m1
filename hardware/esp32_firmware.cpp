/**
 * @file esp32_firmware.cpp
 * @brief Firmware ESP32 Node Sensor Telemetri Trafo Grid PLN UID Bali
 * @author Luthfi Hibatullah - Lab Komputasi & IoT Teknik Elektro Universitas Sriwijaya
 * @date 2026-09-18
 */

#include <Arduino.h>
#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>
#include <ArduinoJson.h>

#define NODE_ID "ESP32-KTA-03"
#define PIN_ADC_VOLTAGE 34
#define PIN_TEMP_ONEWIRE 4
#define STATUS_LED 2

const char* ssid = "PLN_SECURE_GRID_IOT";
const char* password = "REDACTED_WPA3_PSK";
const char* mqtt_server = "broker.unsri-pln.ac.id";
const int mqtt_port = 8883;

WiFiClientSecure espClient;
PubSubClient client(espClient);

void connectWiFi() {
    Serial.printf("[WIFI] Connecting to SSID: %s\n", ssid);
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\n[WIFI] Connected! IP: " + WiFi.localIP().toString());
}

void connectMQTT() {
    while (!client.connected()) {
        Serial.printf("[MQTT] Attempting connection as %s...\n", NODE_ID);
        if (client.connect(NODE_ID, "pln_operator", "auth_token_hash")) {
            Serial.println("[MQTT] Connected to Secure Broker.");
            client.subscribe("pln/command/" NODE_ID);
        } else {
            Serial.printf("[MQTT] Failed, rc=%d. Retrying in 5s...\n", client.state());
            delay(5000);
        }
    }
}

void setup() {
    Serial.begin(115200);
    pinMode(STATUS_LED, OUTPUT);
    pinMode(PIN_ADC_VOLTAGE, INPUT);

    Serial.println("=========================================");
    Serial.println("UNSRI x PLN BALI - IOT TELEMETRY NODE");
    Serial.println("Firmware Rev: v2.8.4-rel | Node: " NODE_ID);
    Serial.println("=========================================");

    connectWiFi();
    client.setServer(mqtt_server, mqtt_port);
}

void loop() {
    if (!client.connected()) {
        connectMQTT();
    }
    client.loop();

    // Baca sensor dan kirim telemetri setiap 3 detik
    static unsigned long lastMsg = 0;
    if (millis() - lastMsg > 3000) {
        lastMsg = millis();

        float rawAdc = analogRead(PIN_ADC_VOLTAGE);
        float busVoltage = (rawAdc / 4095.0) * 3.3 * (220.0 / 3.3); // Kalibrasi trafo
        float chipTemp = temperatureRead();

        StaticJsonDocument<256> doc;
        doc["node_id"] = NODE_ID;
        doc["voltage_rms"] = busVoltage;
        doc["chip_temp"] = chipTemp;
        doc["rssi"] = WiFi.RSSI();
        doc["uptime"] = millis() / 1000;

        char buffer[256];
        serializeJson(doc, buffer);
        client.publish("pln/bali/telemetry/" NODE_ID, buffer);

        Serial.printf("[TELEMETRY SENT] %s\n", buffer);
    }
}

