import time

KEY_MAP = {
    'a': 0x04, 'b': 0x05, 'c': 0x06, 'd': 0x07,
    'e': 0x08, 'f': 0x09, 'g': 0x0a, 'h': 0x0b,
    'i': 0x0c, 'j': 0x0d, 'k': 0x0e, 'l': 0x0f,
    'm': 0x10, 'n': 0x11, 'o': 0x12, 'p': 0x13,
    'q': 0x14, 'r': 0x15, 's': 0x16, 't': 0x17,
    'u': 0x18, 'v': 0x19, 'w': 0x1a, 'x': 0x1b,
    'y': 0x1c, 'z': 0x1d, ' ': 0x2c,
    '\n': 0x28
}

def send_key(code):
    with open('/dev/hidg0', 'wb') as f:
        f.write(bytes([0, 0, code, 0, 0, 0, 0, 0]))
        time.sleep(0.05)
        f.write(bytes([0]*8))

text = "hello from raspberry pi\n"

for char in text:
    if char in KEY_MAP:
        send_key(KEY_MAP[char])
