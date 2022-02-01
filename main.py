"""
Given a string as input. Print the total number of uppercase characters, lowercase characters and digits in input string.
Input-> NEWS360
Output-> Uppers#4 Lower#0 Digit#3
"""

st = "NEWS360"
ln = len(st)
u_count = 0
l_count = 0
d_count = 0
for i in range(0,ln):
  ch = st[i]
  if(ch>="A" and ch<="Z"):
    u_count += 1
  elif(ch>="a" and ch<="z"):
    l_count += 1
  elif(ch>="0" and ch<="9"):
    d_count += 1
print(f"Upper#{u_count}")
print(f"Digit#{d_count}")
print(f"Lower#{l_count}")
