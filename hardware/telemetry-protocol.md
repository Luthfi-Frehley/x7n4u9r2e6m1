# Protokol Telemetri Biner & JSON IoT Grid PLN

Dokumen ini mendefinisikan struktur paket data transmisi serial dan nirkabel untuk node telemetri lapangan.

## 1. Frame Struktur JSON over MQTT
- **Topic**: `pln/bali/telemetry/{NODE_ID}`
- **QoS**: Level 1 (At least once)
- **Format**:
```json
{
  "node_id": "ESP32-KTA-03",
  "voltage_rms": 220.4,
  "chip_temp": 34.2,
  "rssi": -62,
  "uptime": 18492
}
```

## 2. Status Kode Kesalahan
- `0x00`: Normal Operation
- `0xE1`: AC Voltage Out of Bounds (< 198V / > 242V)
- `0xE2`: Over-Temperature Protection Tripped (> 65°C)
- `0xEF`: Loss of Primary AC Feeder (Running on LiFePO4 Reserve)

