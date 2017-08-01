Feature: 作为网站用户，我想要登录系统，以便能够购买商品。

Scenario: 作为网站用户，我想要成功地登录系统，以便能够购买商品。
	Given 我已具有网站账号
	 When 我使用用户名JackyShen@UPerform.CN和密码Abc12345登录网站
	 Then 网站跳转到首页

