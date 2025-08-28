This repository contains a collection of small experiments I built during my spare time while learning **embedded development and IoT**.  
The projects cover different layers of the stack, from device-to-device communication to cloud data integration, using **Bluetooth, LoRa (duplex/half-duplex), and MQTT/TTN**.  

All experiments are based on the **WiFi LoRa 32 v2 (ESP32)** board, with additional modules such as the **NEO-6M GPS** and **SX127x LoRa**.

---

## Experiments

### 1. Bluetooth Connection for Two Development Boards
- Custom BLE libraries used for central (receiver) and peripheral (sender) roles.  
- The peripheral connects to a NEO-6M GPS module and transmits data.  
- The central receives the data using a simple demo function.  

### 2. Duplex LoRa Communication (MicroPython)
- LoRa P2P full-duplex communication.  
- `DuplexCallback`: send a message, then wait to receive.  
- `PingPong`: two boards exchange messages back and forth like a ping-pong game.  

### 3. Half-duplex LoRa Communication (MicroPython)
- LoRa P2P half-duplex communication using the `sx127x` library.  
- One board acts as sender, the other as receiver.  
- Includes the base library, configuration, and sender/receiver examples.  

### 4. MQTT Subscription from TTN
- Connects to WiFi and subscribes to **TTN (The Things Network)** via MQTT.  
- Extracts sensor payload (temperature, humidity, CO₂, etc.) from uplink messages.  
- Subscription topic and parsing logic can be customized.  

---

## Requirements
- **Board**: WiFi LoRa 32 v2 (ESP32)  
- **Modules**: NEO-6M GPS, SX127x LoRa  
- **Firmware/Language**: MicroPython  
- **Network services**: The Things Network (TTN), MQTT broker  

---

## Usage
- **Bluetooth**:  
  - Run the main function on the peripheral.  
  - On the central device, simply use:  
    ```python
    import BLE_Central
    
    if __name__ == "__main__":
        BLE_Central.demo()
    ```
- **LoRa Duplex/Half-duplex**: run the corresponding example (`DuplexCallback.py`, `PingPong.py`, `Sender.py`, or `Receiver.py`).  
- **MQTT**: update WiFi configuration and `MQTT_TOPIC`, then run `mqtt_sub.py`.  

---

## Repository Scope
This repository is intended as a personal learning project at the intersection of **embedded systems and IoT**:  
- Starting with **low-level communication protocols** (BLE, SPI, UART, LoRa)  
- Extending to **network and cloud integration** (MQTT, TTN)  
- Building a minimal end-to-end IoT learning loop from device to cloud  


