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
    pass


def low_or_highpass_filter(values: List[Real], treshhold: Real,
                           type_: str = "lowpass") -> List[Real]:
    """Lowpass or Highpass Filter for list values.
        Depends on filter type maximum or minimum value of treshhold
        will be returned.

    :param values: List of values. A single value can be int or float
    :param treshhold: Value which is the max/min allowed limit
    :param type_: filter type. Should be `lowpass` or `highpass`
    :returns: Filtered list of numbers
    :raises: TypeError if type is not `lowpass` or `highpass`
    :raises: ValueError if a single type of values is not a Real Number
    :raises: ValueError if treshhold is not a real number

    :examples:
        >> values = [1, 2, 3, 4, 5, 6, 7]
        >> value_filter(values=values, treshhold=4)
        [1, 2, 3, 4]

        >> value_filter(values=values, treshhold=4, type_: "highpass")
        [4, 5, 6, 7]
    """
    pass


def get_files_from_directory(suffix: str = ".py",
                             directory_path: str = "./") -> List[str]:
    """Returns lists of files with given suffix from directory.

    :param suffix: File suffix (which can be also the file type)
    :param directory: path to directory where files should be excluded from
    :returns: list of filesnames incl. suffix
        returns an empty list if directory_path does not exists
    """
    pass


def generate_random_string(string_length: int) -> str:
    """Generates a random string with any given length

    :param string_length: Wanted length of generated string
    :returns: random string with mixed numbers, letters and punctuation with
        length string_length
    """
    pass


def get_number_of_days_in_month(month: int, year: int) -> int:
    """Get numbers of days in a given month in a year.

    :param month: Index of month. Indexes starts with 1 for January.
        Number must be between 1 and 12.
    :param year: Year where month is alocated
    :returns: Numbers of days in month.
        returns -1 If Monthindex is out of range
    """
    pass


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
    pass


def get_fibonacci_numbers(counts: int) -> List[int]:
    """Returns list of fibonacci numbers with length of counts

    :param counts: Count of Fibonacci numbers
        **NOT maximum fibonacci number**
    :returns: List of Fibonacci numbers

    :examples:
        >> get_fibonacci_numbers(6)
        [1, 2, 3, 5, 8, 13]
    """
    pass
