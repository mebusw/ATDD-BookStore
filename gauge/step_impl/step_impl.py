#encoding=utf8
from getgauge.python import step, before_scenario, Messages
from src import *

vowels = ["a", "e", "i", "o", "u"]


def number_of_vowels(word):
    return len([elem for elem in list(word) if elem in vowels])


# --------------------------
# Gauge step implementations
# --------------------------

@step("The word <word> has <number> vowels.")
def assert_no_of_vowels_in(word, number):
    assert str(number) == str(number_of_vowels(word))


@step("Vowels in English language are <vowels>.")
def assert_default_vowels(given_vowels):
    Messages.write_message("Given vowels are {0}".format(given_vowels))
    assert given_vowels == "".join(vowels)


@step("Almost all words have vowels <table>")
def assert_words_vowel_count(table):
    actual = [str(number_of_vowels(word)) for word in table.get_column_values_with_name("Word")]
    expected = [str(count) for count in table.get_column_values_with_name("Vowel Count")]
    assert expected == actual

@step("fc <table>")
def assert_flight_combination(table):
    for case in table.get_column_values_with_name("case"):
        Messages.write_message(u"case={0}".format(case))
    assert 1 == 1


@step("<Case> for <Combination>  with <Booked Seat> results in <NREA> and <Extra Locked Seat> which is <status>")
def assert_flight_combination(case, combination, booked_seat, NREA, extra, status):
    Messages.write_message(u"case={0},{1},{2},{3},{4}".format(case, combination, booked_seat, NREA, extra))
    assert status == "OK"
    assert NREA == FlightScheduler(case, combination, booked_seat, extra).process()
    


# ---------------
# Execution Hooks
# ---------------

@before_scenario()
def before_scenario_hook():
    assert "".join(vowels) == "aeiou"
