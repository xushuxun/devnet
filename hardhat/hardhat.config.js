require("@nomicfoundation/hardhat-toolbox");



/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.24",
  networks: {
    devnet: {
      url: "http://localhost:8545", // 替换为您的 devnet RPC 地址
      chainId: 32382, // 替换为您的 devnet 链 ID
      accounts: ["2e0834786285daccd064ca17f1654f67b4aef298acbb82cef9ec422fb4975622"] // 替换为您的私钥
    }
  }
};
