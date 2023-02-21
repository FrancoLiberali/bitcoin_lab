import bitcoin
import bitcoin.rpc

bitcoin.SelectParams("regtest")
conf="Chuck/BtcChuck.conf"
proxy=bitcoin.rpc.Proxy(btc_conf_file=conf)
nbblocks=proxy.getblockcount()
print(nbblocks)
