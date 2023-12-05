"""?"""


def calc_mean(numbers: list[int]) -> float:
    """
    Calculate the mean of a list of integers.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        float: The mean of the input list, rounded to three decimal places.

    Example:
    ```python
    >>> calc_mean([1, 2, 3, 4, 5])
    3.0
    ```
    """
    mean = sum(numbers) / len(numbers)
    return round(mean, 3)


def calc_median(numbers: list[int]) -> float:
    """
    Calculate the median of a list of integers.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        float: The median of the input list, rounded to two decimal places.

    Example:
    ```python
    >>> calc_median([1, 2, 3, 4, 5])
    3.0
    ```

    Note:
    - For an odd-length list, the median is the middle element.
    - For an even-length list,
     the median is the average of the two middle elements.
    """
    ordered_numbers: list[int] = sorted(numbers)
    length: int = len(ordered_numbers)
    if length % 2 == 1:
        # odd
        mid_point_index = length // 2

        median_value = float(ordered_numbers[mid_point_index])
    else:
        # even
        upper_middle_index = length // 2
        lower_middle_index = upper_middle_index - 1

        upper_middle_value = ordered_numbers[upper_middle_index]
        lower_middle_value = ordered_numbers[lower_middle_index]

        median_value = (upper_middle_value + lower_middle_value) / 2

    return round(median_value, 2)


def calc_mode(numbers: list[int]) -> list[int]:
    """
    Calculate the mode(s) of a list of integers.

    Args:
        numbers (List[int]): A list of integers.

    Returns:
        List[int]: A list containing the mode(s) of the input list.
        If there is a tie, multiple modes may be returned.

    Example:
    ```python
    >>> calc_mode([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    [4]
    ```

    Note:
    - If all values in the input list are unique,
     an empty list is returned.
    - In case of a tie for the mode,
     multiple modes may be present in the result.
    """
    unique_numbers = set(numbers)

    frequency_map = {}
    for unique_number in unique_numbers:
        frequency = numbers.count(unique_number)
        frequency_map[unique_number] = frequency

    max_frequency = max(frequency_map.values())

    modes = []
    for key, value in frequency_map.items():
        if value == max_frequency:
            modes.append(key)

    if len(unique_numbers) == len(modes):
        modes.clear()

    return modes


def solve_data_set(data: list[int]) -> tuple[float, float, list[int]]:
    """
    Solve a data set by calculating its mean, median, and mode.

    Args:
        data (List[int]): A list of integers representing the data set.

    Returns:
        Tuple[float, float, List[int]]: 
        A tuple containing the mean, median, and mode of the input data set.

    Example:
    ```python
    >>> solve_data_set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
    (3.0, 3.0, [4])
    ```

    Note:
    - The mean is the average value of the data set.
    - The median is the middle value or the average of the 
    middle values in the sorted data set.
    - The mode is the value(s) that occur most frequently in the data set.
    If there is a tie, multiple modes may be returned.
    """
    mean = calc_mean(data)
    median = calc_median(data)
    mode = calc_mode(data)

    return (mean, median, mode)


def main() -> None:
    """
    Main function demonstrating the usage of statistical 
    calculation functions on predefined data sets.

    Returns:
        None

    Example:
    ```python
    >>> main()
    (4.286, 4.0, [6, 1])
    (4.375, 4.5, [6])
    (4.0, 3.0, [6])
    (4.0, 4.0, [6])
    ```

    Note:
    - The function prints the results of solving each data set,
    including mean, median, and mode.
    - The `solve_data_set` function is used for calculating 
    the statistical measures.
    - Data sets are predefined for illustration purposes.
    """
    data_set_one = [6, 9, 1, 2, 6, 3, 7]
    data_set_two = [6, 9, 1, 2, 6, 3, 7, 4]
    data_set_three = [6, 9, 1, 2, 6, 3, 7, 4, 1]
    data_set_four = [6, 9, 1, 2, 3, 7, 4, 8]

    data_sets = [data_set_one, data_set_two, data_set_three, data_set_four]
    for data_set in data_sets:
        print(solve_data_set(data_set))


if __name__ == "__main__":
    main()
