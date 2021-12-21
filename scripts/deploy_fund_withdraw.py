import os

from scripts.deploy import (
    deploy_fund_me,
)


from scripts.fund_and_withdraw import (
    fund,
    withdraw
)


def main():
    deploy_fund_me()
    fund()
    withdraw()
