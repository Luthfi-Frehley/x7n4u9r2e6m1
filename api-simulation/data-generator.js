/**
 * @file data-generator.js
 * @description Generator data uji telemetri node sensor ESP32
 */

function generateTelemetryFrame(nodeId, lat, lng) {
    return {
        node_id: nodeId,
        location: { lat, lng },
        timestamp: Date.now(),
        voltage_rms: +(219 + Math.random() * 3).toFixed(1),
        current_amp: +(12 + Math.random() * 4).toFixed(2),
        temperature_c: +(32 + Math.random() * 5).toFixed(1),
        status: "NORMAL"
    };
}

module.exports = { generateTelemetryFrame };
