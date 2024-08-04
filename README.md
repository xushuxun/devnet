# Eth local dev network

```bash

cd devnet

./clone_and_build.sh

./init.sh

./cleanup.sh

```


```bash
./geth attach http://localhost:8545

> web3.eth.sendTransaction({from: "0x123463a4b065722e99115d6c222f267d9cabb524",to: "0x123c0ffee567beef890decade123fade456bed78",value: web3.toWei(1, "ether")})

> web3.fromWei(eth.getBalance("0x123c0ffee567beef890decade123fade456bed78"), "ether")

```