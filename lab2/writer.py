def writeJson(data):
	import json
	with open('data.json', 'w') as f:
		s = '{ "items":['
		for i in data:
			s = s + '{'
			it = ''
			k = 1
			for j in i:
				it = '"key' + str(k) + '" : "' + j + '",'
				k = k + 1
			s = s + it + '},'
		s = s + "]}"
		json.dump(data, f)

def writeCsv(data):
	import csv
	with open('data.csv', 'w', newline='') as f:
		w = csv.writer(f, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for i in data:
			w.writerow(i)

print("Choice file type:")
print("1: json")
print("2: csv")
choice = int(input("Enter the number: "))
if (choice < 1) or (choice > 2):
	print("Fail choice!")
	exit()

print("Enter lines (ex: '123, test, true')")
print("For stop enter blank line")
data = []
while True:
	line = input(":")
	if(line == ""):
		break
	data.append(line.split(","))

if choice == 1:
	writeJson(data)
else:
	writeCsv(data)
