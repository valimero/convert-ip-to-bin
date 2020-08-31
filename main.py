import sys

def convertIntToBin8(n):
	return f'{n:08b}'

def inputIpAdress():
	return input("Ip adresss to convert:")

def reverseBin(adressBin: str):
	return adressBin.replace('0', 'b').replace('1', 'a').replace('a', '0').replace('b', '1')

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

# Return the number of possible adresses (without network and broadcast)
def getNumberPossibleAddress(ipAdressConverted : str):
	return 2 ** ipAdressConverted.count('0') - 2


def diplayResult(ipAdress: str, ipAdressConverted: str, numberPossibleAddress: int):
	print("-----------------------------------------------------------")
	print("Subnet mask : \t\t" + ipAdress)
	print("Subnet mask bin: \t" + ipAdressConverted)
	print()
	print("Number of available addresses: " + str(numberPossibleAddress))
	print("-----------------------------------------------------------")


argv = sys.argv

argc = len(argv)

if(argc == 2):
	inputIpAdress = argv[1]
elif(argc == 3):
	inputIpAdress = argv[1]



else:
	inputIpAdress = inputIpAdress()

# if(len(argv) > 1):
# 	inputIpAdress = argv[1]
# else:
# 	inputIpAdress = inputIpAdress()

# Convert the subnet mask to binary
ipAdressConverted = convertIpAdressToBin(inputIpAdress)

# Get the number of available addresses
numberPossibleAddress = getNumberPossibleAddress(ipAdressConverted)

diplayResult(inputIpAdress, ipAdressConverted, numberPossibleAddress)
