from brownie import OurToken, network, accounts, config
from scripts.helpful_scripts import get_account
from web3 import Web3

INITIAL_SUPPLY = Web3.toWei(69000, "ether")


def deploy_token():
    account = get_account()
    token = OurToken.deploy(
        INITIAL_SUPPLY,
        {"from": account}
    )
    print(token.name())


def main():
    deploy_token()
