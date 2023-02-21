import bitcoin
import bitcoin.rpc
import base64

bitcoin.SelectParams("regtest")
conf="Bob/BtcBob.conf"
proxy=bitcoin.rpc.Proxy(btc_conf_file=conf)

lasthash=proxy.getbestblockhash()
lastblock = proxy.getblock(lasthash)
tx = lastblock.vtx[1]
txo2=tx.vout[1]
script = txo2.scriptPubKey
data=script[2:]

fh = open("CA_Banfield-rebuild.png", "wb")
fh.write(base64.b64decode(data))
fh.close()