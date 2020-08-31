import sys

def convertIntToBin8(n):
	return f'{n:08b}'

def inputIpAdress():
	return input("Ip adresss to convert:");

# Convert Ip adress to bin
def convertIpAdressToBin(ipAddress: str):
	# Split the address in a tab.
	tabIp = inputIpAdress.split('.')

	r = "";

	for index in range(len(tabIp)):
		r = r + str(convertIntToBin8(int(tabIp[index])))

		if(index < len(tabIp) - 1):
			r = r + '.'

	return r


def diplayResult(ipAdress: str, ipAdressConverted: str):
	print("---------------------------------------------------\n Ip address : \t" + ipAdress + "\n Result: \t" + ipAdressConverted)
	print("---------------------------------------------------")


argv = sys.argv

if(len(argv) > 1):
	inputIpAdress = argv[1]
else:
	inputIpAdress = inputIpAdress()


diplayResult(inputIpAdress, convertIpAdressToBin(inputIpAdress))
