
"""
# ES32 TTGO v1.0 
device_config = {
    'miso':19,
    'mosi':27,
    'ss':18,
    'sck':5,
    'dio_0':26,
    'reset':14,
    'led':2, 
}
# M5Stack ATOM Matrix
device_config = {
    'miso':23,
    'mosi':19,
    'ss':22,
    'sck':33,
    'dio_0':25,
    'reset':21,
    'led':12, 
}

# M5Stack & LoRA868 Module
device_config = {
    'miso':19,
    'mosi':23,
    'ss':5,
    'sck':18,
    'dio_0':26,
    'reset':36,
    'led':12, 
}

"""

# WIFI Lora 32(V2) Module
device_config = {
    'miso':19,
    'mosi':27,
    'ss':18,
    'sck':5,
    'dio_0':26,
    'reset':14,
    'led':25, 
}



app_config = {
    'loop': 200,
    'sleep': 100,
}

lora_parameters = {
    'frequency': 868E6, 
    'tx_power_level': 2, 
    'signal_bandwidth': 125E3,    
    'spreading_factor': 8, 
    'coding_rate': 5, 
    'preamble_length': 8,
    'implicit_header': False, 
    'sync_word': 0x12, 
    'enable_CRC': False,
    'invert_IQ': False,
}

wifi_config = {
    'ssid':'',
    'password':''
}