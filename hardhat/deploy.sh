#!/bin/bash

npx hardhat compile

rm ignition/deployments -rf

npx hardhat ignition deploy ./ignition/modules/Token.js --network devnet
