const assert = require('assert')
const { Given, When, Then } = require('@cucumber/cucumber')
const { Greeter, Bank, Account, LoyaltyProgram } = require('../../src')

When('the greeter says hello', function () {
  this.whatIHeard = new Greeter().sayHello()
});

Then('I should have heard {string}', function (expectedResponse) {
  assert.equal(this.whatIHeard, expectedResponse)
});


function isItFriday(today) {
  if (today === "Friday") {
    return "TGIF";
  } else {
    return "Nope";
  }
}

Given('today is {string}', function (givenDay) {
  this.today = givenDay;
});

When('I ask whether it\'s Friday yet', function () {
  this.actualAnswer = isItFriday(this.today);
});

Then('I should be told {string}', function (expectedAnswer) {
  assert.strictEqual(this.actualAnswer, expectedAnswer);
});

///////////////////// LoyaltyProgram ////////////////////////////////

// '阿宝的账户里有<balance-paul>元'
Given('阿宝的账户里有{float}元', function (balancePaul) {
  this.accountOfPaul = new Account('阿宝', balancePaul);
});

// '玛丽的账户里有<balance-mary>元'
Given('玛丽的账户里有{float}元', function (balanceMary) {
  this.accountOfMary = new Account('玛丽', balanceMary);
});

// '阿宝试图转账<amount>元给玛丽的账户'
When('阿宝试图转账{float}元给玛丽的账户', function (amount) {
  this.transferResult = new Bank().transfer(this.accountOfPaul, this.accountOfMary, amount);
});

// '转账<status>'
Then('转账{string}', function (status) {
  // 根据实际的转账结果和期望的状态进行断言
  assert.equal(this.transferResult, status)
});

// '阿宝的账户应该有<final-balance-paul>元余额'
Then('阿宝的账户应该有{float}元余额', function (finalBalancePaul) {
  assert.equal(this.accountOfPaul.balance, finalBalancePaul);
});

// '玛丽的账户应该有<final-balance-mary>元余额'
Then('玛丽的账户应该有{float}元余额', function (finalBalanceMary) {
  assert.equal(this.accountOfMary.balance, finalBalanceMary);
});