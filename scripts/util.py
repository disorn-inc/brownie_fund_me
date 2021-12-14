from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMAL = 8
STARTING_PRICE = 390000000000

def get_account():
    if (network.show_active() in LOCAL_BLOCHAIN_ENVIRONMENTS 
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    
def deploy_mock():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mock...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            DECIMAL, STARTING_PRICE, {"from": get_account()}
        )
    print("Mock Deployed!")