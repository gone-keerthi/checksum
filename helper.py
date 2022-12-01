# Steps to calculate Checksum

# 1 convert strings to 8 bits array
# 2 sum the b values allowing carry bit wrap around
# 3 take 1's compliment of the and attach it to data


# data_to_binarr = lambda data:[format(ord(ch),"08b") for ch in data]
import time


def data_to_binarr(data):
    result = []
    for ch in data:
        binary_value = format(ord(ch), "08b")
        time.sleep(1)
        print(f"{ch} -> {binary_value}")
        result.append(binary_value)
    return result


def binary_sum(a, b): return bin(int(a, 2)+int(b, 2))[2:]


def bin_arr_to_data(bin_data):
    ans = ""
    for data in bin_data:
        ans += chr(int(data, 2))
    return ans


def carry_bit_wrap_around_sum(a, b):
    ans = binary_sum(a, b)
    if len(ans) > 8:
        while(len(ans) > 8):
            a = ans[-8:]
            b = ans[:-8]
            ans = binary_sum(a, b)
    return ans.rjust(8, '0')


def ones_compliment(bin_val):
    compliment = ""
    for val in bin_val:
        compliment += '1' if val == '0' else '0'
    return compliment


def checksum(bin_data):

    data_checksum = "00000000"

    # calculating checksum by adding binnary with carry bit wrap around
    for data in bin_data:
        data_checksum = carry_bit_wrap_around_sum(data_checksum, data)

    # 1's compliment of the sum
    data_checksum = ones_compliment(data_checksum)

    print(f"The checksum of above that is {data_checksum}")

    return data_checksum


if __name__ == "__main__":
    data = "ABCDEFGH"

    bin_data = data_to_binarr(data)
    # append checksum to data
    bin_data.append(checksum(bin_data))

    data_with_checksum = bin_arr_to_data(bin_data)

    print(f"\nData after appending checksum -> {data_with_checksum}")
    print("\n")
    print(checksum(data_to_binarr(data_with_checksum)))
