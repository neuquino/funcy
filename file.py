def xor(a, b):     # xor two strings of different lengths
 if len(a) > len(b):
    return "".join(["%s" % (ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
 else:
    return "".join(["%s" % (ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
print hex(0x30167b0eb4eef511ec82272b4b47a2d71471^0x1319057cb23c1dcbf616876372617fff8b48)

