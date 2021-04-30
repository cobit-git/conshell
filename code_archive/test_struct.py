import struct 

STX = 0x0203
projectID = 345
cageID = 2445
arr= struct.pack('hh', projectID, cageID)
print(arr)

unarr = struct.unpack('hh', arr)
print(unarr)