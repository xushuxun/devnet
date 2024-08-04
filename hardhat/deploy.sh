#!/bin/bash

npx hardhat compile
npx hardhat ignition deploy ./ignition/modules/Token.js --network devnet
