import pytest
import os
import uuid

from tasks._01_basics.functions import (
  is_even_number, low_or_highpass_filter, get_files_from_directory,
  generate_random_string, get_number_of_days_in_month, next_time_calculator,
  get_fibonacci_numbers
)
# from solutions._01_basics.functions import (
#     is_even_number, low_or_highpass_filter, get_files_from_directory,
#     generate_random_string, get_number_of_days_in_month,
#     next_time_calculator, get_fibonacci_numbers,
# )


class TestIsEvenNumber:
    def test_number_is_even(self):
        assert is_even_number(202)

    def test_number_is_not_even(self):
        assert not is_even_number(1001)

    def test_wrong_number_type(self):
        assert not is_even_number(42.1)
        assert not is_even_number("string")


class TestLowOrHighpassFilter:
    def setup_class(self):
        self.values = [1, 2.3, 0.8, 3.3, 4, 99, 3.14, 42]
        self.treshhold = 3.14

    def test_lowpass_filter(self):
        expected_filtered_values = [1, 2.3, 0.8, 3.14]
        filtered_values = low_or_highpass_filter(
            values=self.values, treshhold=self.treshhold
        )
        assert expected_filtered_values == filtered_values

    def test_highpass_filter(self):
        expected_filtered_values = [3.3, 4, 99, 3.14, 42]
        filtered_values = low_or_highpass_filter(
            values=self.values, treshhold=self.treshhold, type_="highpass"
        )
        assert expected_filtered_values == filtered_values

    def test_type_error_if_type_is_not_highpass_or_lowpass(self):
        with pytest.raises(TypeError):
            low_or_highpass_filter(
                values=self.values, treshhold=self.treshhold, type_="any"
            )

    def test_value_error_if_treshhold_has_wrong_type(self):
        with pytest.raises(ValueError):
            low_or_highpass_filter(values=self.values, treshhold="string")

    def test_value_error_if_single_value_has_wrong_type(self):
        value_list_1 = [1, 2.3, None, 3.3, 4, 99, 3.14, 42]
        with pytest.raises(ValueError):
            low_or_highpass_filter(
                values=value_list_1, treshhold=self.treshhold
            )

        value_list_2 = [1, 2.3, 0.8, 3.3, 4, 99, "3.14", 42]
        with pytest.raises(ValueError):
            low_or_highpass_filter(
                values=value_list_2, treshhold=self.treshhold
            )


class TestGetPythonFilesFromDirectory:
    def test_get_python_files_from_directory(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        expected_files = [
            f for f in os.listdir(current_path) if f.endswith(".py")
        ]
        files_in_directory = get_files_from_directory(
            suffix=".py", directory_path=current_path
        )
        assert files_in_directory == expected_files

    def test_get_empty_list_of_files_from_directory(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        suffix = uuid.uuid4().hex
        files_in_directory = get_files_from_directory(
            suffix=suffix, directory_path=current_path
        )
        assert files_in_directory == []

    def test_return_empty_list_on_not_existing_directory(self):
        not_existing_directory = "PathWhichDoesHopefullyNotExists"
        files_in_directory = get_files_from_directory(
            directory_path=not_existing_directory
        )
        assert files_in_directory == []


def test_generate_random_string():
    assert len(generate_random_string(string_length=43)) == 43


class TestGetNumbersOfDaysInMonth:
    def test_returns_negative_value_for_invalid_month(self):
        invalid_months = [-1, 0, 13, 99]
        for month in invalid_months:
            assert get_number_of_days_in_month(month=month, year=2020) == -1

    def test_get_number_of_days_in_month(self):
        assert get_number_of_days_in_month(month=2, year=2021) == 28
        assert get_number_of_days_in_month(month=1, year=2021) == 31
        assert get_number_of_days_in_month(month=12, year=2020) == 31


class TestNextTimeCalculator:
    def test_next_time_calculator_within_same_day(self):
        assert next_time_calculator(hour=8, duration=8) == 16

    def test_next_time_calculator_with_overlap_day_less_than_24_hours(self):
        assert next_time_calculator(hour=20, duration=8) == 4

    def test_next_time_calculator_with_overlap_day_more_than_24_hours(self):
        assert next_time_calculator(hour=20, duration=140) == 16

    def test_raise_value_error_if_hour_is_out_of_range_positive_number(self):
        with pytest.raises(ValueError):
            next_time_calculator(hour=28, duration=10)

    def test_raise_value_error_if_hour_is_out_of_range_negative_number(self):
        with pytest.raises(ValueError):
            next_time_calculator(hour=-1, duration=10)

    def test_raise_type_error_if_hour_is_wrong_type(self):
        with pytest.raises(TypeError):
            next_time_calculator(hour="string", duration=10)

    def test_raise_type_error_if_duration_is_wrong_type(self):
        with pytest.raises(TypeError):
            next_time_calculator(hour=8, duration="string")


class TestFibonacciNumbers:
    def test_fibonacci_numbers_count_1(self):
        assert get_fibonacci_numbers(counts=1) == [1]

    def test_fibonacci_numbers_count_2(self):
        assert get_fibonacci_numbers(counts=2) == [1, 1]

    def test_fibonacci_numbers_count_3(self):
        assert get_fibonacci_numbers(counts=3) == [1, 1, 2]

    def test_fibonacci_numbers_count_10(self):
        expected_numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        assert get_fibonacci_numbers(counts=10) == expected_numbers
