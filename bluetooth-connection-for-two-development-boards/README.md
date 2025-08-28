# Bluetooth Connection for Two Development Boards

It's Raymond, This part of the code implements the Bluetooth connection between the two development boards (using Wifi Lora 32 v2 boards).

The project contains three BLE libraries, the Advertising library is needed for both development boards, the Central library is for the central device (the device that receives data) and the Peripheral library is for the peripheral device (the device that sends data). In addition, I use the NEO-6M GPS module, so I also put the getGPS library here. 

Only the main function for the peripheral device is there because, the main function for the central device does not need to call anything more than the demo function at the bottom of the Central library, so please use:

import BLE_Central

if __name__ == "__main__".
    BLE_Central.demo()

to get the central device started.

Note the modification of various connection ports, except that there are no other notes, have a good time!

Ruiming Wu, 28.03.2023