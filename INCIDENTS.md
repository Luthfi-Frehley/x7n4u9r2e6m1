# Laporan Insiden & Investigasi Gangguan (Post-Mortem)

## Tiket: #INC-2026-0918-KTA
- **Tanggal:** 18 September 2026, 08:12:02 WIB
- **Tingkat Keparahan:** SEV-1 (Critical / Down)
- **Komponen Terdampak:** Node Sensor ESP32-KTA-03 (Gardu Trafo Distribusi Kuta Beach)
- **Penyelidik:** Luthfi (Lab IoT Unsri) & Ir. Nyoman Arya (PLN UID Bali)

---

### Kronologi Kejadian
1. **08:10:02 WIB**: Gateway Udayana mendeteksi hilangnya 1 heartbeat frame dari ESP32-KTA-03.
2. **08:11:02 WIB**: Percobaan retry TCP syn kedua gagal. Latensi melonjak ke >900ms.
3. **08:12:02 WIB**: Sistem otomatis menyatakan status `TIMEOUT > 300s`, packet loss 100%.
4. **08:12:05 WIB**: Daemon otomatis mengalihkan (failover) transmisi radio data area Kuta melalui Substation Repeater Jimbaran (ESP32-JBR-02).
5. **08:12:10 WIB**: Tiket `#INC-2026-0918-KTA` diterbitkan ke sistem pemantauan NOC dan peta spasial menampilkan kedap-kedip merah.

---

### Akar Masalah (Root Cause)
Terjadi anomali pemutusan daya pada feeder sekunder 220V akibat cuaca pesisir pantai Kuta dan pemicuan MCB proteksi beban lebih. Unit cadangan baterai LiFePO4 internal node mempertahankan logging lokal, namun transmisi RF terputus.

---

### Rencana Mitigasi
1. Dispatch teknisi PLN Unit Pelaksana Pelayanan Pelanggan (UP3) Bali Selatan ke titik koordinat node `[-8.7214, 115.1695]`.
2. Penggantian modul isolator tegangan dan pemulihan catu daya gardu trafo.

