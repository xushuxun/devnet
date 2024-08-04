from web3 import Web3
import json

# 连接到您的以太坊节点（这里假设是本地节点）
w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))

# 合约地址（请替换为实际部署的地址）
contract_address = '0x3B92c21Ad01E7091513eAb0c26C28B8Ba1Ee21ab'  # 替换为您的合约地址

# 合约 ABI（从编译后的合约JSON文件中获取）
# load file from artifacts/contracts/Token.sol/Token.json
contract_abi = None
with open('artifacts/contracts/Token.sol/Token.json') as f:
    contract_abi = json.load(f)
    contract_abi = contract_abi['abi']

# 创建合约实例
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

# 获取账户（这里使用第一个账户）
account = w3.eth.accounts[0]

# 读取合约信息
print(f"Token Symbol: {contract.functions.symbol().call()}")
print(f"Total Supply: {contract.functions.totalSupply().call()}")
print(f"Owner: {contract.functions.owner().call()}")

# 查看账户余额
balance = contract.functions.balanceOf(account).call()
print(f"Balance of {account}: {balance}")

# 转账示例
recipient = '0x123c0ffee567beef890decade123fade456bed78'  # 替换为接收方地址
amount = 100  # 转账金额
checksum_address = Web3.to_checksum_address(recipient)

# 创建交易
tx = contract.functions.transfer(checksum_address, amount).build_transaction({
    'from': account,
    'nonce': w3.eth.get_transaction_count(account),
})

# 签名交易
private_key = '2e0834786285daccd064ca17f1654f67b4aef298acbb82cef9ec422fb4975622'  # 替换为发送方账户的私钥
signed_tx = w3.eth.account.sign_transaction(tx, private_key)

# 发送交易
tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

# 等待交易被挖矿
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"Transaction successful. Transaction hash: {tx_receipt.transactionHash.hex()}")

# 查看转账后的余额
new_balance = contract.functions.balanceOf(account).call()
recipient_balance = contract.functions.balanceOf(checksum_address).call()
print(f"New balance of {account}: {new_balance}")
print(f"Balance of recipient {recipient}: {recipient_balance}")