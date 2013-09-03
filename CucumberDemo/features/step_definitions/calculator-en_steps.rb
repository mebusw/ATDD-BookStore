# encoding: utf-8
begin require 'rspec/expectations'; rescue LoadError; require 'spec/expectations'; end
require 'cucumber/formatter/unicode'
$:.unshift(File.dirname(__FILE__) + '/../../lib')
require 'calculator'

Before do
  @calc = Calculator.new
end

After do
end

Given /I have entered (\d+) into the calculator/ do |n|
  @calc.push n.to_i
end

When /I press (\w+)/ do |op|
  if op == 'add'
    @result = @calc.send op
  end
end

Then /the result should be (.*) on the screen/ do |result|
  @result.should == result.to_f
end

When(/^I touch "(.*?)"$/) do |arg1|
  i = 1
end

Given(/^I fill in text fields as follows:$/) do |table|
  #puts table.raw
  #fail(msg="Error. Check log for details.")
end

And /^It should (pass|fail) with (.*)$/ do |pass_fail, json|
	puts pass_fail, json
end
