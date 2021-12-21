from brownie import FundMe, MockV3Aggregator, network, config

from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)


def verify_fund_me():
    fund_me = FundMe[-1]
    account = get_account()
    FundMe.publish_source(fund_me)



def main():
    verify_fund_me()