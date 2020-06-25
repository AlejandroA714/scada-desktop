from datetime import date, timedelta, datetime
from openpyxl import Workbook
from openpyxl.styles import Color, Fill, PatternFill

format = "%Y-%m-%d"
value = date.today()
value2 = '2020-06-24 00:00:00'
print(date.strftime(value, '%Y-%m-%d'))