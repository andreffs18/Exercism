def commands(binary_str):
    message = []
    for operation, bit in enumerate(reversed(binary_str), start=1):
        if bool(int(bit)):
            if operation == 1:
                # 00001 = wink
                message.append("wink")
            if operation == 2:
                # 00010 = double blink
                message.append("double blink")
            if operation == 3:
                # 00100 = close your eyes
                message.append("close your eyes")
            if operation == 4:
                # 01000 = jump
                message.append("jump")
            if operation == 5:
                # 10000 = Reverse the order of the operations in the secret handshake.
                message = list(reversed(message))
    return message
