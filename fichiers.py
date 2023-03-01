with open("file.txt", "a+") as file:
	file.write("h4cK3rM4n04\n")
	file.write("31i3\n")
	file.write("r4m4m1h4r150n\n")
	file.write("h4ck\n")
	file.close()


'''Grande différence entre "a+" et "w+"	'''

students_list = ["Mirai", "Kakehashi", "Saki", "Yusuke", "Alice", "Max", "Paul", "Bernard"]

with open("students.txt", "w+") as exe:
	for x in students_list:
		exe.write(x + '\n')
	exe.close()

t = ['bonjour']
with open('txt.txt', 'w+') as r:
	r.write(str(t))
	r.close()