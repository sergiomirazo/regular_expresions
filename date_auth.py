import re
date = input("Enter a date in the format dd/mm/yyyy:")
pattern1 = r"([0-2][0-9]|[3][0-1])\/([0][0-9]|[1][0-2])\/[0-9]{4}"
match1 = re.match(pattern1, date)
pattern2 = r"([0-2][0-9]|[3][0-1])\-(0[0-9]|1[0-2])\-[0-9]{4}"
match2 = re.match(pattern2, date)
pattern3 = r"([0-2][0-9]|[3][0-1])\.(0[0-9]|1[0-2])\.[0-9]{4}"
match3 = re.match(pattern3, date)
pattern4 = r"([0-2][0-9]|[3][0-1])\s(0[0-9]|1[0-2])\s[0-9]{4}"
match4 = re.match(pattern4, date)
if match1 or match2 or match3 or match4:
  print(f"{date} matches the pattern")
else:
  print("Date does not match the pattern")
