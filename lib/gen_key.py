#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:刘海超
# 该类已被修改

from binascii import hexlify, unhexlify

import pyelliptic


def createPrivateKeyAndPublicKey():
    CURVE = 'secp256k1'

    svr = pyelliptic.ECC(curve=CURVE)

    svr_pubkey = svr.get_pubkey()
    svr_privkey = svr.get_privkey()
    privateKey = hexlify(svr_privkey)
    # print("save private key")
    # print(privateKey)

    publicKey = "%s%s" % (hexlify(svr.pubkey_x), hexlify(svr.pubkey_y))
    # print("\nappender_open's parameter:")
    # print(publicKey)
    return privateKey, publicKey
