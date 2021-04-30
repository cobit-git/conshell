import struct 
import numpy as np

class ConshellUtils:
    def float16_to_hex(self, f):
        return hex(struct.unpack('<H', np.float16('117.0').tobytes())[0])

    def float_to_hex(self, f):
        return hex(struct.unpack('<I', struct.pack('<f', f))[0])

    def double_to_hex(self, f):
        return hex(struct.unpack('<Q', struct.pack('<d', f))[0])

    def hex_to_float(self, f):
        return struct.unpack('!f', bytes.fromhex(f))[0]

    
if __name__ == '__main__':
    utils = ConshellUtils()
    print(utils.float16_to_hex(17.5))
    hex_value = utils.float_to_hex(17.5)
    print(hex_value[:6]) 
    print(utils.double_to_hex(17.5))
    print(utils.hex_to_float(utils.float_to_hex(17.5)[2:]))