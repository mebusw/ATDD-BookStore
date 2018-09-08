# Flight Booking

To run this spec

     gauge run specs/


![](las-vegas-flight.jpg)
![](../../../specs/las-vegas-flight.jpg)

Rules of seats：

- Lv6：First seat of economic class
- Lv8：Safe exit
- Lv5：Row 2-6, aisle or window
- Lv4：Row 2-6, middle

Background：

- Layout：787，330
- Booked seat is locked
- All seats except X lock on layout are availiable
- Layout file：HainanAirline.txt

     |Case      |Combination|Booked Seat|NREA|Extra Locked Seat|
     |----------|-----------|-----------|----|-----------------|
     |31-31 Window |*          |31A        |31K |                 |
     |Aisle       |*          |31C        |31D |                |
     |Middle       |767/300N-767/300N||||
     |1 to 2, middle  |767/300N-300/200||||
     |row 2-6, middle, forward|||||
     |middle, not forward|||||
     |row 2-6, same row, window|||||
     |row 2-6, window, forward|||||
     |row 2-6, aisle, forward|||||
     |safe exit, same row|||||
     |safe exit, forward|||||
     |others|||||

## Same value, Same seat protection

tags: flight

* <Case> for <Combination>  with <Booked Seat> results in <NREA> and <Extra Locked Seat> which is "OK"


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
