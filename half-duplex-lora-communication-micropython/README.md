# Half-duplex Lora communication MicroPython

This is the code used to implement half-duplex P2P Lora communication between two boards, with one as receiver and one as sender.

This library contains 5 files, where sx127x is the basic library for Lora communication, just like the BLE library for Bluetooth communication; the config library should be changed according to the board (or according to the pinout of the external Lora module); the Sender and Receiver files are functions written according to the sx127x library for both roles (it is possible to consider them as main functions directly).


