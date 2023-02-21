import sys
import bitcoin
import bitcoin.rpc
from bitcoin.core import COIN, b2x, b2lx
import binascii
from bitcoin.core import CTxOut, CTxIn, CTransaction
from bitcoin.core import CMutableTransaction, CMutableTxOut
from bitcoin.core.script import CScript
from bitcoin.core.script import OP_CHECKSIG, OP_RETURN
import base64

fd = open("download/CA_Banfield.png", "rb")
b = fd.read()
print(binascii.hexlify(b))
photo_str=base64.b64encode(b)

bitcoin.SelectParams("regtest")
conf="Chuck/BtcChuck.conf"
proxy=bitcoin.rpc.Proxy(btc_conf_file=conf)

unspent = sorted(proxy.listunspent(0), key=lambda x: hash(x["amount"]))
txins = [CTxIn(unspent[-1]["outpoint"])]
value_in = unspent[-1]["amount"]

change_addr = proxy.getnewaddress()
change_pubkey = proxy.validateaddress(change_addr)["pubkey"]
change_out = CMutableTxOut(bitcoin.params.MAX_MONEY, CScript([change_pubkey, OP_CHECKSIG]))

digest_outs = [CMutableTxOut(0, CScript([OP_RETURN, photo_str]))]
txouts = [change_out] + digest_outs

tx = CMutableTransaction(txins, txouts)

FEE_PER_BYTE = 0.00011*COIN/1000
tx.vout[0].nValue = int(value_in - len(tx.serialize()) * FEE_PER_BYTE)
r = proxy.signrawtransaction(tx)
tx = r["tx"]
print(b2x(tx.serialize()))
print(len(tx.serialize()), "bytes")
print(b2lx(proxy.sendrawtransaction(tx)))