class EBadSignature(Exception):
	pass

def isBestChoice(item):
	return (item["isNative"] == True) and \
	       (item["isOOP"] == True) and \
	       (item["isEasy"] == True)

def printJson(data):
	print(
		'Lang'.ljust(15) +
		'Is native'.ljust(15) +
		'Is OOP'.ljust(15) +
		'Is easy'.ljust(15) +
		'Is best choice!'.ljust(15)
	)
	print('-'*15*5)
	for i in data["items"]:
		print(
			str(i["lang"]).ljust(15) +
			str(i["isNative"]).ljust(15) +
			str(i["isOOP"]).ljust(15) +
			str(i["isEasy"]).ljust(15) +
			str(isBestChoice(i)).ljust(15)
		)
	pass

if __name__ == "__main__":
    from json import *
    import json

    data: dict

    with open("./data.json", "r") as file:
        try:
            data = json.load(file)
            if not (data['signature'] == 'com.github.anotherstudent.json-example-signateure'):
                raise EBadSignature('')
            printJson(data)
        except JSONDecodeError:
            print("Bad json")
        except EBadSignature:
        	print("Bad signature")
        except:
        	print("Internal error")  	
