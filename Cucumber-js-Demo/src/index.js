class Greeter {
  sayHello() {
    return 'hello'
  }
}

class Bank {
  transfer(from, to, amount) {
    if(from.balance < amount) {
      return "取消";
    }
    from.balance -= amount;
    to.balance += amount;
    return "成功";
  }
}

class Account {
  constructor(name, balance) {
    this.name = name;
    this.balance = balance;
  }

  debit(amount) {
    this.balance += amount;
  }

  withdraw(amount) {
    this.balance -= amount;
  }

}

class LoyaltyProgram {
  registerCustomer(customer) {
    // register the customer in the loyalty program
  }

  awardPoints(customer, points) {
    // award loyalty points to the customer
  }
}

module.exports = {
  Greeter,
  Bank,
  Account,
  LoyaltyProgram
}


