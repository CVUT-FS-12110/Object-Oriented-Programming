import struct
import io

"""
    vvvv      YOUR SOLUTION      vvvv
"""


def parse_data(input_binary_data):  # dont change the signature of the function

    # use this function to run your solution

    return "decoded message"  # here return decoded message in correct format


"""
    ^^^^      YOUR SOLUTION      ^^^^
#################################################################
    vvvv TESTS FOR YOUR SOLUTION vvvv
"""

assert parse_data(b'\x01\x00\x0A\x00\x02\x01\x00\x05\x48\x65\x6C\x6C\x6F\x01\x00\x06\x57\x6F\x72\x6C\x64\x21') == "{FrameHeader[1,10,0,2]:FramePayload[<SubFrameHeader[1,5]:SubFrameData[Hello]>,<SubFrameHeader[1,6]:SubFrameData[World!]>]}->Hello World!"
assert parse_data(b'\x01\x00\x00\x00\x00') == '{FrameHeader[1,0,0,0]:FramePayload[]}->'
assert parse_data(b'\x01\x00\x0A\x00\x02\x01\x00\x05\x48\x65\x6C\x6C\x6F\x01\x00\x05\x57\x6F\x72\x6C\x64\x01\x00\x0A\x00\x02\x01\x00\x05\x48\x65\x6C\x6C\x6F\x01\x00\x05\x57\x6F\x72\x6C\x64') == "{FrameHeader[1,10,0,2]:FramePayload[<SubFrameHeader[1,5]:SubFrameData[Hello]>,<SubFrameHeader[1,5]:SubFrameData[World]>]}->Hello World\n{FrameHeader[1,10,0,2]:FramePayload[<SubFrameHeader[1,5]:SubFrameData[Hello]>,<SubFrameHeader[1,5]:SubFrameData[World]>]}->Hello World"
assert parse_data(b'\x01\x00\x32\x00\x04\x01\x00\x0D\x48\x75\x73\x74\x6f\x64\x65\x6d\x6f\x6e\x73\x6b\x79\x01\x00\x0B\x6b\x72\x75\x74\x6f\x70\x72\x69\x73\x6e\x61\x01\x00\x11\x6d\x6f\x6e\x73\x74\x72\x6e\x65\x2d\x76\x74\x69\x70\x6f\x7a\x6e\x69\x01\x00\x09\x61\x6c\x69\x6f\x66\x6f\x62\x69\x65') == "{FrameHeader[1,50,0,4]:FramePayload[<SubFrameHeader[1,13]:SubFrameData[Hustodemonsky]>,<SubFrameHeader[1,11]:SubFrameData[krutoprisna]>,<SubFrameHeader[1,17]:SubFrameData[monstrne-vtipozni]>,<SubFrameHeader[1,9]:SubFrameData[aliofobie]>]}->Hustodemonsky krutoprisna monstrne-vtipozni aliofobie"
