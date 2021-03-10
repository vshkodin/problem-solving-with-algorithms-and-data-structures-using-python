def func(s1,s2):
	reversedString=""
	for i in s1:
		reversedString=i + reversedString
	if reversedString == s2:
		return True
	else:
		return False

print(func("coc","coc"))
print(func("coc","cox"))
