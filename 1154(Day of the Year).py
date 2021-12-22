class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = date.split("-")

        year = int(year)
        is_leap = (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)
        day_of_month = [31, 29+is_leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        day_of_year = 0
        for m in range(int(month) - 1):
            day_of_year += day_of_month[m]

        return day_of_year + int(day)