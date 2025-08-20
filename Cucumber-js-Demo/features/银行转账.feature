Feature: 银行账户

    Scenario: 账户之间成功转账
        Given 阿宝的账户里有500元
        And 玛丽的账户里有200元
        When 阿宝试图转账200元给玛丽的账户
        Then 转账"成功"
        And 阿宝的账户应该有300元余额
        And 玛丽的账户应该有400元余额

    Scenario Outline: 账户之间成功或取消转账
        Given 阿宝的账户里有<balancePaul>元
        And 玛丽的账户里有<balanceMary>元
        When 阿宝试图转账<amount>元给玛丽的账户
        Then 转账"<status>"
        And 阿宝的账户应该有<finalBalancePaul>元余额
        And 玛丽的账户应该有<finalBalanceMary>元余额


        Examples:
            | balancePaul | balanceMary | amount | status | finalBalancePaul | finalBalanceMary |
            | 1000        | 300         | 100    | 成功   | 900              | 400              |
            | 200         | 0           | 300    | 取消   | 200              | 0                |