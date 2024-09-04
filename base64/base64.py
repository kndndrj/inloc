_LOOKUP = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def encode(body: bytes) -> str:
    # convert input to bits
    bits = str()
    for b in body:
        bits += f"{b:08b}"

    # calculate ammount of padding characters ("=")
    length = len(bits)
    while length % 6:
        length += 8
    padding = int((length - len(bits)) / 6)

    # assemble base64 string from bits
    encoded = str()
    for i in range(0, len(bits), 6):
        chunk = bits[i : i + 6]

        # at the end, if the chunk is incomplete, add zeroes to it's tail
        if len(chunk) < 6:
            chunk += "0" * (6 - len(chunk))

        # take the appropriate character from the lookup
        encoded += _LOOKUP[int(chunk, 2)]

    # finally, add padding characters ("=")
    return encoded + "=" * padding


def decode(body: str) -> bytes:
    # assemble bits from input characters with lookup
    # ignore padding and any possible whitespace
    bits = str()
    for c in body:
        if c not in ("=", " ", "\t", "\n"):
            bits += f"{_LOOKUP.index(c):06b}"

    # assemble an array of bytes from produced bits
    decoded = bytearray()
    for i in range(0, len(bits), 8):
        byte = bits[i : i + 8]

        # at the end, if the byte is incomplete, it's leftover padding (ignore it)
        if len(byte) < 8:
            continue
        decoded.append(int(byte, 2))

    return bytes(decoded)


if __name__ == "__main__":
    import sys
    import textwrap

    if "-d" in sys.argv:
        # strip trailing newline from input
        dec = decode("\n".join(sys.stdin.readlines()))
        # print without a newline
        sys.stdout.buffer.write(dec)
    else:
        enc = encode(b"".join(sys.stdin.buffer.readlines()))
        # print with 76 character line wrap
        print(textwrap.fill(enc, 76))
