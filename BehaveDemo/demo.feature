Feature: 作为亚马逊用户，我想要登录系统，以便能够购买商品。

Scenario: 作为亚马逊用户，我想要成功地登录系统，以便能够购买商品。
	Given 我已具有亚马逊账号
	 When 我使用用户名JackyShen@UPerform.CN和密码Abc12345进行登录
	 Then 系统跳转到首页


Scenario Outline: 用户名格式有误
  Given 我已具有亚马逊账号
   When 我使用用户名<username>和密码<password>进行登录
   Then 提示用户名格式有误

  Examples: 错误的用户名格式
   | username         | password |
   | abc              | Abc12345 |
   | abc@             | Abc12345 |
   | abc@b            | Abc12345 |



Scenario Outline: 密码格式有误
  Given 我已具有亚马逊账号
   When 我使用用户名<username>和密码<password>进行登录
   Then 提示密码格式有误

  Examples: 错误的密码格式
   | username                | password |
   | JackyShen@UPerform.CN   | 0        |
   | JackyShen@UPerform.CN   | &^#      |
   | JackyShen@UPerform.CN   | aaabbb12 |

