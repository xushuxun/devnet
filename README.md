# Eth local dev network

启动本地网络

```bash
cd devnet

# 编译过程被注释掉了
./clone_and_build.sh

# 初始化，geth要求输入密码，填1
./init.sh

# 启动网络
# 使用 Procfile文件，或者 run_*.sh 脚本挨个启动

# 清理数据
./cleanup.sh
```


测试本地网络

```bash
./geth attach http://localhost:8545

> web3.eth.sendTransaction({from: "0x123463a4b065722e99115d6c222f267d9cabb524",to: "0x123c0ffee567beef890decade123fade456bed78",value: web3.toWei(1, "ether")})

> web3.fromWei(eth.getBalance("0x123c0ffee567beef890decade123fade456bed78"), "ether")
```

部署合约

```bash
cd hardhat

./deploy.sh
```

测试执行合约和订阅

```bash
python3 subscribe.py

# 注意修改合约部署地址
python3 call_token.py
```