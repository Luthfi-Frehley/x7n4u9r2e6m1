# Simulasi API Telemetri Gateway

Folder ini menyediakan data mock dan jembatan simulasi telemetri untuk demonstrasi web dashboard NOC tanpa memerlukan koneksi hardware fisik secara langsung.

- `metrics.json`: Snapshot data metrik realtime grid (tegangan, frekuensi, CPU, status node).
- `endpoints.json`: Daftar rute dan spesifikasi API gateway.
- `mqtt-bridge.js`: Skrip bridge untuk update timestamp berkala.
- `data-generator.js`: Generator payload telemetri acak.
