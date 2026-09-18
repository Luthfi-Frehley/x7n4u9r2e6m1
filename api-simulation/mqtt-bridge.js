/**
 * @file mqtt-bridge.js
 * @description Jembatan simulasi protokol MQTT ke HTTP REST WebSocket untuk telemetry gateway
 * @author Luthfi - Lab Komputasi & IoT Teknik Elektro Unsri
 */

const fs = require('fs');
const path = require('path');

const METRICS_FILE = path.join(__dirname, 'metrics.json');

console.log('[MQTT-BRIDGE] Memulai bridge simulasi telemetry PLN x Unsri...');
console.log('[MQTT-BRIDGE] Mendengarkan topic: pln/bali/+/telemetry');

// Fungsi regenerasi snapshot metrics berkala (simulasi daemon)
function cycleTelemetrySnapshot() {
    try {
        if (!fs.existsSync(METRICS_FILE)) return;
        const raw = fs.readFileSync(METRICS_FILE, 'utf-8');
        const data = JSON.parse(raw);

        // Update server timestamp
        data.system.server_time = new Date().toISOString();
        data.system.uptime_seconds += 5;

        // Simulasi fluktuasi beban listrik grid
        const freqOffset = (Math.random() * 0.04 - 0.02);
        data.grid_metrics.frequency_hz = +(50.0 + freqOffset).toFixed(2);
        data.grid_metrics.voltage_rms_v = +(220.0 + (Math.random() * 1.2 - 0.6)).toFixed(1);

        fs.writeFileSync(METRICS_FILE, JSON.stringify(data, null, 2), 'utf-8');
        console.log(`[SNAPSHOT] Telemetri grid disinkronkan: ${data.grid_metrics.voltage_rms_v}V @ ${data.grid_metrics.frequency_hz}Hz`);
    } catch (err) {
        console.error('[ERROR] Gagal sinkronisasi data telemetri:', err.message);
    }
}

// Simulasi loop bridge jika dijalankan langsung via node
if (require.main === module) {
    setInterval(cycleTelemetrySnapshot, 5000);
    cycleTelemetrySnapshot();
}

module.exports = { cycleTelemetrySnapshot };

