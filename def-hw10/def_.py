def calculate(a=52, b=67):
    return a + b











def change_case(text: str, upper: bool = True) -> str:
    return text.upper() if upper else text.lower()











def sum_numbers(numbers: str = "1,2,3", separator: str = ",") -> int:
    return sum(int(x) for x in numbers.split(separator))

