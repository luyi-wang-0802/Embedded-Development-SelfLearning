# Duplex Lora communication MicroPython

This part of the code implements full-duplex communication in Lora P2P mode, i.e., it can send and receive messages at the same time.

The DuplexCallback file is simple to send a message and then wait to receive a message, while the PingPong file allows the two boards to reciprocate messages as if they were playing ping pong.

The SPI bus used for Lora communication is itself a bus that can achieve full-duplex communication, just like the UART bus used for NUS in Bluetooth communication, which has two channels for sending and receiving at the same time.

