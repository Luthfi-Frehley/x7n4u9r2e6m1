# Changelog Sistem Telemetri IoT PLN x Unsri

Semua perubahan dan riwayat rilis protokol sistem telemetri dicatat dalam dokumen ini.

## [2.8.4-rel] - 2026-09-18
### Ditambahkan
- Modul peta geospasial interaktif Leaflet.js dengan basemap CartoDB DarkMatter.
- Indikator peringatan visual *pulsing red beacon* pada node gangguan Kuta Beach (`ESP32-KTA-03`).
- Terminal telemetri live streamer pada dashboard utama NOC.
- Endpoint asinkron `/api-simulation/metrics.json` dengan dukungan anti-cache header.
- Otomasi deployment CI/CD GitHub Pages via GitHub Actions.

### Diperbaiki
- Optimasi latensi handshake MQTT TLS 1.3 antara Gateway Udayana dan Lab Unsri Palembang.
- Penanganan auto-failover rute transmisi telemetri melalui Substation Jimbaran.

## [2.0.1] - 2026-08-10
### Ditambahkan
- Portal autentikasi Gatekeeper berstandar enkripsi SHA-256 untuk akses operator.
- Dukungan sensor suhu digital DS18B20 pada trafo distribusi 20kV.

## [1.0.0] - 2026-06-01
### Rilis Perdana
- Inisialisasi arsitektur telemetri node ESP32 cluster Denpasar.
- Protokol pertukaran paket MQTT broker port 8883.

