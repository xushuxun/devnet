#!/bin/bash


# jwt.hex:
#  beacon-chain 和 geth 通信的 jwt token

# config.yml: 
#   beacon chain 配置

# genesis.json:
#  geth 创世区块配置

# 创世配置
# 注意 genesis-time-deploy 参数，多问chatgpt
./prysmctl testnet generate-genesis --fork capella --num-validators 64 --genesis-time-delay 10 --chain-config-file config.yml --geth-genesis-json-in genesis.json  --geth-genesis-json-out genesis.json --output-ssz genesis.ssz


# geth 初始化
./geth --datadir=gethdata account import secret.txt
./geth --datadir=gethdata init genesis.json



