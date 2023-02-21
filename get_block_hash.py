import bitcoin
import bitcoin.rpc
import binascii

bitcoin.SelectParams("regtest")
conf="Chuck/BtcChuck.conf"
proxy=bitcoin.rpc.Proxy(btc_conf_file=conf)

# call the node's getblockcount JSON-RPC method
count = proxy.getblockcount()

for i in range(0, min(10, count)):
    print(binascii.hexlify(
        proxy.getblockhash(count - i)
    ))