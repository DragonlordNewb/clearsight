from time import time
from random import getrandbits
from random import randint
from tqdm import tqdm
from hashlib import sha256

def _hexadecimalToBinary(n):
	return bin(int(n, 16))[2:]

def _binaryToHexadecimal(n):
	return hex(int(n, 2))[2:]

def _binaryToDecimal(n):
	return int(n, 2)

def _decimalToBinary(n):
	return bin(n)[2:]

def _decimalToHexadecimal(n):
	return _binaryToHexadecimal(_decimalToBinary(int(n)))

def _hexadecimalToDecimal(n):
	return _binaryToDecimal(_hexadecimalToBinary(n))

def _binaryToBoolean(n):
	return [x == "1" for x in list(n)]

def _stringToBinary(s):
		result = []
		for c in s:
				bits = bin(ord(c))[2:]
				bits = '00000000'[len(bits):] + bits
				result.extend([int(b) for b in bits])
		return "".join([str(x) for x in result])

def _stringToHexadecimal(s):
    return _binaryToHexadecimal(_stringToBinary(s))

def _hexadecimalToString(n):
    return _binaryToString(_hexadecimalToBinary(n))

def _binaryToString(n):
	return "".join(chr(int(''.join(x), 2)) for x in zip(*[iter(n)]*8))

def _decimalToString(n):
    return _hexadecimalToString(_decimalToHexadecimal(n))

def generateKey(keylength):
	return _binaryToHexadecimal("".join([str(getrandbits(1)) for x in range(keylength)]))

def operate(string, hexkey):
	# Operating on plaintext with the key gives ciphertext.
	# Operating on ciphertext with the key gives plaintext.
	st = time()

	binstring = [int(x) for x in _stringToBinary(string)]
	binkey = [int(x) for x in _hexadecimalToBinary(hexkey)]

	result = ""
	toggle = True

	for index in range(len(binstring)):
		keybit = binkey[(index ** int(hexkey[0], 16)) % len(binkey)]
		stringbit = binstring[index]

		if keybit == 1:
			toggle = not toggle

		if toggle:
			result = result + str(keybit ^ stringbit)

		else:
			result = result + str(stringbit)

	et = time()

	return _binaryToString(result)

def shuffleKey(hexkey):
    # "Shuffle" key
    binkey = _hexadecimalToBinary(hexkey)

    try:
        skip = _hexadecimalToDecimal(hexkey[1])
    except IndexError:
        skip = _hexadecimalToDecimal(hexkey[0])
    except Exception as e:
        raise e

    newbinkey = []
    for index in range(len(binkey)):
        if binkey[:index] == "":
            targetBitIndex = int(binkey[0])
        else:
            targetBitIndex = skip + _binaryToDecimal(binkey[:index])
        newbinkey.append(binkey[targetBitIndex % len(binkey)])

    newhexkey = _binaryToHexadecimal("".join(newbinkey))

    shuffled = []

    repetitions = 0
    lastNybble = ""
    for nybble in newhexkey:
        if nybble == lastNybble:
            repetitions += 1
            if repetitions == 3:
                return "".join(shuffled)
            shuffled.append(nybble)
        else:
            repetitions == 0
            lastNybble = nybble
            shuffled.append(nybble)

    return "".join(shuffled)

def generateSalt(hexkey):
    # Generate the salt

    salt = ""

    currenthexkey = hexkey

    for _ in range(_hexadecimalToDecimal(hexkey[:2])):
        currenthexkey = shuffleKey(currenthexkey)
        currentbinkey = _hexadecimalToBinary(currenthexkey)
        currenthash = sha256(hexkey.encode("utf-8")).hexdigest()

        addLength = 0
        toggle = True
        for strbit in currentbinkey:
            bit = int(strbit)
            if bit == 1:
                toggle = not toggle

            if toggle:
                addLength += 1

        salt = salt + currenthash[addLength % len(currenthash)]

    # Clip the salt

    shuffled = []

    repetitions = 0
    lastNybble = ""
    for nybble in salt:
        if nybble == lastNybble:
            repetitions += 1
            if repetitions == 3:
                return "".join(shuffled)
            shuffled.append(nybble)
        else:
            repetitions == 0
            lastNybble = nybble
            shuffled.append(nybble)

    return _binaryToString(_hexadecimalToBinary("".join(shuffled))[1:])

def salt(string, hexkey):
    hexstring = _stringToHexadecimal(string)
    if _hexadecimalToBinary(hexkey)[0] == "0":
        return _hexadecimalToString(hexstring + generateSalt(hexkey))
    else:
        return _hexadecimalToString(generateSalt(hexkey) + hexstring)

def encrypt(plaintext, hexkey):
    return generateSalt(hexkey) + operate(plaintext, hexkey)

def decrypt(ciphertext, hexkey):
    return operate(ciphertext[len(generateSalt(hexkey)):], hexkey)
