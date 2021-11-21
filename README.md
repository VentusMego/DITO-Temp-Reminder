# DITO-Temp-Reminder
## DITO查询、转赠流量插件（Auto refer and share Data to another DITO User）

For specific function. For my own convenience. Remind owner to share data to another DITO user.
本插件是非官方第三方插件，仅限学习交流使用，不作为自己盈利项目，不保证维护。

## 功能
本插件针对Shared Data部分的余量与时间进行定制。
通过购买套餐（promo199、promo99、promo39）的手机号转赠流量给被监控DITO卡，保证被监控卡的Shared Data流量足够使用，时间不会过期。目前支持消息推送后手动操作，后期支持直接输入手机上的OTP进行流量转赠。

*目前（20211120）DITO最少赠送流量50M，一天可赠送5次。*
*没有转赠费用。*
*赠送流量48小时内有效，独立计算，转赠将更新Shared Data的时间。*

![image](https://user-images.githubusercontent.com/6715610/142747001-9c73438b-df7f-4391-ac9b-07fdc422169f.png)
基于Python、Selenium实现，电脑端需要配置环境。考虑后期迁移Github Actions/服务器端。
