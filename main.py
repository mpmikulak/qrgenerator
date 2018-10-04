#!/usr/bin/python3

import qrcode

for n in range(2):
    data = ''
    for i in range(100):
        data = "{}{}".format(data, i)
        # print(data)
        img = qrcode.make(data)

        img.save("testqr{}".format(n))