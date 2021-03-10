import os
from random import randint
from string import ascii_letters, digits, punctuation
from datetime import date
from typing import List
from numbers import Real


def is_even_number(number: int) -> bool:
    """Returns True or False if number is even.

    :param number: Input number
    :returns:
        number is even: True
        number is not even: False
        number is not an integer: False
    """

    if not isinstance(number, int):
        return False
    return number % 2 == 0


def low_or_highpass_filter(values: List[Real], treshhold: Real,
                           type_: str = "lowpass") -> List[Real]:
    """Lowpass or Highpass Filter for list values.
        Depends on filter type maximum or minimum value of treshhold
        will be returned.

    :param values: List of values. A single value can be int or float
    :param treshhold: Value which is the max/min allowed limit
    :param type_: filter type. Should be `lowpass` or `highpass`
    :returns: Filtered list of numbers
    :raises: TypeError if type_ is not `lowpass` or `highpass`
    :raises: ValueError if a single type of values is not a Real Number
    :raises: ValueError if treshhold is not a real number

    :examples:
        >> values = [1, 2, 3, 4, 5, 6, 7]
        >> value_filter(values=values, treshhold=4)
        [1, 2, 3, 4]

        >> value_filter(values=values, treshhold=4, type_: "highpass")
        [4, 5, 6, 7]
    """
    if type_ not in ['lowpass', 'highpass']:
        raise TypeError(
            f"Type must be lowpass or highpass but {type_} is used."
        )

    if not isinstance(treshhold, Real):
        raise ValueError(
            f"treshhold must be a Real number but {type(treshhold)} is used."
        )

    # Note the following method for geting not valid values from list is not
    # optimized since the loop `value in values` is used twice.
    # You can take a look into the additional solution
    if False in [isinstance(value, Real) for value in values]:
        raise ValueError("values must contain only Real numbers.")

    if type_ == "lowpass":
        return [value for value in values if value <= treshhold]

    if type_ == "highpass":
        return [value for value in values if value >= treshhold]

    return []


def low_or_highpass_filter_alternative(values: List[Real], treshhold: Real,
                                       type_: str = "lowpass") -> List[Real]:
    """Lowpass or Highpass Filter for list values.
        Depends on filter type maximum or minimum value of treshhold
        will be returned.

    :param values: List of values. A single value can be int or float
    :param treshhold: Value which is the max/min allowed limit
    :param type_: filter type. Should be `lowpass` or `highpass`
    :returns: Filtered list of numbers
    :raises: TypeError if type_ is not `lowpass` or `highpass`
    :raises: ValueError if a single type of values is not a Real Number
    :raises: ValueError if treshhold is not a real number

    :examples:
        >> values = [1, 2, 3, 4, 5, 6, 7]
        >> value_filter(values=values, treshhold=4)
        [1, 2, 3, 4]

        >> value_filter(values=values, treshhold=4, type_: "highpass")
        [4, 5, 6, 7]
    """
    if type_ not in ["lowpass", "highpass"]:
        raise TypeError(
            f"Type must be lowpass or highpass but {type_} is used."
        )

    if not isinstance(treshhold, Real):
        raise ValueError(
            f"treshhold must be a Real number but {type(treshhold)} is used."
        )

    filtered_values = []
    for value in values:
        if not isinstance(value, Real):
            raise ValueError("values must contain only Real numbers.")
        if type_ == "lowpass" and value <= treshhold:
            filtered_values.append(value)
        if type_ == "highpass" and value >= treshhold:
            filtered_values.append(value)

    return filtered_values


def get_files_from_directory(suffix: str = ".py",
                             directory_path: str = "./") -> List[str]:
    """Returns lists of files with given suffix from directory.

    :param suffix: File suffix (which can be also the file type)
    :param directory: path to directory where files should be excluded from
    :returns: list of filesnames incl. suffix
        returns an empty list if directory_path does not exists
    """
    if not os.path.exists(directory_path):
        return []
    return [f for f in os.listdir(directory_path) if f.endswith(suffix)]


def generate_random_string(string_length: int) -> str:
    """Generates a random string with any given length

    :param string_length: Wanted length of generated string
    :returns: random string with mixed numbers, letters and punctuation with
        length string_length
    """
    chars = ascii_letters + digits + punctuation
    return "".join(
        [chars[randint(0, len(chars)-1)] for _ in range(string_length)]
    )


def get_number_of_days_in_month(month: int, year: int) -> int:
    """Get numbers of days in a given month in a year.

    :param month: Index of month. Indexes starts with 1 for January.
        Number must be between 1 and 12.
    :param year: Year where month is alocated
    :returns: Numbers of days in month.
        returns -1 If Monthindex is out of range
    """
    if month < 1 or month > 12:
        return -1

    input_date = date(year, month, 1)
    if month == 12:
        output_date = date(year+1, 1, 1)
    else:
        output_date = date(year, month+1, 1)

    return (output_date - input_date).days


def next_time_calculator(hour: int, duration: int) -> int:
    """Calculates end time hour based on start hour and duration
        in a 24h time system

    :param hour: start time in range [0, 23]
    :param duration: duration in hours from start to endtime
    :returns: end time in range [0, 23]
    :raises: ValueError if hour is out of range
    :raises: TypeError if hour or duration have wrong type

    :examples:
        >> next_time_calculator(hour=8, duration=8)
        16

        >> next_time_calculator(hour=20, duration=8)
        4

        >> next_time_calculator(hour=22, duration=2)
        0

        >> next_time_calculator(hour=20, duration=140)
        16
    """
    if not isinstance(hour, int):
        raise TypeError(f"`hour` must be type int but it's {type(hour)}")

    if not isinstance(duration, int):
        raise TypeError(
            f"`duration` must be type int but it's {type(duration)}"
        )

    if hour not in range(24):
        raise ValueError(f"`hour` must be in range [0, 24] but it's {hour}")

    return (hour + duration) % 24


def get_fibonacci_numbers(counts: int) -> List[int]:
    """Returns list of fibonacci numbers with length of counts

    :param counts: Count of Fibonacci numbers
        **NOT maximum fibonacci number**
    :returns: List of Fibonacci numbers

    :examples:
        >> get_fibonacci_numbers(1)
        [1]

        >> get_fibonacci_numbers(7)
        [1, 1, 2, 3, 5, 8, 13]
    """
    if counts == 1:
        return [1]
    if counts == 2:
        return [1, 1]

    fibonacci = [1, 1]
    for i in range(counts - 2):
        # I do personally do not like to manipulate a list based on it's own
        # values. A lot of side effects can happen while you are modyfying an
        # operating list. An additional approach is mentioned in another
        # function.
        fibonacci.append(fibonacci[i] + fibonacci[i+1])
    return fibonacci


def get_fibonacci_numbers_alternative(counts: int) -> List[int]:
    """Returns list of fibonacci numbers with length of counts

    :param counts: Count of Fibonacci numbers
        **NOT maximum fibonacci number**
    :returns: List of Fibonacci numbers

    :examples:
        >> get_fibonacci_numbers(1)
        [1]

        >> get_fibonacci_numbers(7)
        [1, 1, 2, 3, 5, 8, 13]
    """
    if counts == 1:
        return [1]
    if counts == 2:
        return [1, 1]

    fibonacci = [1, 1]
    current_value, past_value = 1, 1
    for i in range(counts - 2):
        new_value = current_value + past_value

        # Just initialized same styled like few lines before
        past_value, current_value = current_value, new_value
        fibonacci.append(new_value)
    return fibonacci
