import sys


def convert_int_to_bin_8(n):
    return f'{n:08b}'


def func_input_ip_address():
    return input("Ip address to convert:")


def reverse_bin(address_bin: str):
    return address_bin.replace('0', 'b').replace('1', 'a').replace('a', '0').replace('b', '1')


# Convert Ip address to bin
def convert_ip_address_to_bin(ip_address: str):
    # Split the address in a tab.
    tab_ip = ip_address.split('.')

    r = ""

    for index in range(len(tab_ip)):
        r = r + str(convert_int_to_bin_8(int(tab_ip[index])))

        if index < len(tab_ip) - 1:
            r = r + '.'

    return r


# Return the number of possible addresses (without network and broadcast)
def get_number_possible_address(ip_address_converted: str):
    return 2 ** ip_address_converted.count('0') - 2


def display_result(ip_address: str, ip_address_converted: str, number_possible_address: int):
    print("-----------------------------------------------------------")
    print("Subnet mask : \t\t" + ip_address)
    print("Subnet mask bin: \t" + ip_address_converted)
    print()
    print("Number of available addresses: " + str(number_possible_address))
    print("-----------------------------------------------------------")


argv = sys.argv

argc = len(argv)

if argc == 2:
    input_ip_address = argv[1]
elif argc == 3:
    input_ip_address = argv[1]
else:
    input_ip_address = func_input_ip_address()

# if(len(argv) > 1):
# 	func_input_ip_address = argv[1]
# else:
# 	func_input_ip_address = func_input_ip_address()

# Convert the subnet mask to binary
ip_address_converted = convert_ip_address_to_bin(input_ip_address)

# Get the number of available addresses
numberPossibleAddress = get_number_possible_address(ip_address_converted)

display_result(input_ip_address, ip_address_converted, numberPossibleAddress)
