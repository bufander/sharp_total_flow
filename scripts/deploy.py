from brownie import L1Action

from brownie import accounts, network, config
from typing import Union

LOCAL_BLOCKCHAIN = ["development", "goerli-fork"]

def deploy_contract():
    account = get_account()
    print(f"Using account {account.address}")

    # Only publish source in tesnets
    publish_source = True if network.show_active()=="goerli" else False
    contract = L1Action.deploy({"from":account}, publish_source=publish_source)
    print(f"Deployed contract in {contract}")
    return account, contract


def get_account(index: Union[int, None] = None) -> str:
    if index:
        return accounts[index]
    elif network.show_active() in LOCAL_BLOCKCHAIN:
        return accounts[0]
    elif network.show_active() in config["networks"]:
        return accounts.add(config["wallets"]["from_key"])
    else:   
        print("Unknow network")
        assert 0


def main():
    deploy_contract()