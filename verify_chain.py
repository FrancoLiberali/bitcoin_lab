import bitcoin
import bitcoin.rpc

bitcoin.SelectParams("regtest")
conf="Chuck/BtcChuck.conf"
proxy=bitcoin.rpc.Proxy(btc_conf_file=conf)

# call the node's getblockcount JSON-RPC method
count = proxy.getblockcount()

last_block_hash = proxy.getblockhash(count)
last_block = proxy.getblock(last_block_hash)
prev_block_hash = last_block.hashPrevBlock

for i in range(1, min(100, count)):
    block_hash = proxy.getblockhash(count - i)
    if block_hash != prev_block_hash:
        print("Error")
        exit(1)
    
    block = proxy.getblock(block_hash)
    prev_block_hash = block.hashPrevBlock

print("Chain verified")