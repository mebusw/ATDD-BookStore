# 航班预定

![](las-vegas-flight.jpg)
![](../../../specs/las-vegas-flight.jpg)

座位的大致规则：

- 6级：经济舱第一排
- 8级：安全出口座位
- 5级：经济舱第2-6排靠窗及靠过道
- 4级：经济舱第2-6排中间

背景：

- 使用的布局：787，330
- 原座位是锁的
- 除布局图上的X锁外，其他座位都可用
- 机型文件：海航机型.txt


## 相同价值，相同位置保护
（固定是向前保护的，如果后面有合适的座位不保护，但安全出口例外）

tags: flight


* fc
     |case      |航班组合    |订座|NREA|额外锁定座位 |
     |----------|-----------|---|----|-----------|
     |31到31靠窗 |*          |31A|31K |           |
     |过道       |*          |31C|31D |           |
     |中间       |767/300N-767/300N||||
     |1变2 中间  |767/300N-300/200||||
     |2-6排中间向前|||||
     |中间不向后|||||
     |2-6排窗口同排|||||
     |2-6排窗口向前|||||
     |2-6排过道向前|||||
     |安全出口同排|||||
     |安全出口前移|||||
     |其他|||||
     

## Vowel counts in single word

tags: single word

* The word "gauge" has "3" vowels.


## Vowel counts in multiple word

This is the second scenario in this specification

Here's a step that takes a table

* Almost all words have vowels
     |Word  |Vowel Count|
     |------|-----------|
     |Gauge |3          |
     |Mingle|2          |
     |Snap  |1          |
     |GoCD  |1          |
     |Rhythm|0          |
