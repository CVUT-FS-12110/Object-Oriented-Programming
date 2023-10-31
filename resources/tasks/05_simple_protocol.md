# 05 - Simple Protocol Parser

Objective: The objective of this assignment is to design an object-oriented solution for parsing a binary protocol with nested structures. You are required extract meaningful information from binary data provided. See the following instructions


### Binary Protocol Description
- The binary protocol consists of frames, each containing a header and a payload.
- The header contains information about the payload length and other metadata.
- The payload contains multiple frames of different layers, with each frame having a specific structure.

Protocol specification:

    SimpleFrame:
        Header (7 bytes):
            Frame ID (1 byte): Unique identifier for the frame (0-255).
            Payload Length (2 bytes): Number of bytes in the payload (0-65535).
            Secret Flag (1 byte): 0 for not secret, 1 for secret.
            Number of SubFrames (1 byte): Number of SubFrames in the payload (0-255).
        Payload:
            SubFrame (variable length):
                Frame Type (1 byte): Type identifier for the SubFrame.
                Frame Length (2 bytes): Number of bytes in the SubFrame data.
                Frame Data (variable length = Frame Length): Actual data of the SubFrame.
            SubFrame (variable length):
                (again SubFrame body) ...
    SimpleFrame: 
        (again SimpleFrame body) ...

In scope of this task you are encouraged to use Python `struct` module for handling binary data. Struct Formats:

    SimpleFrame Header Format: '>BHBB' (Big-endian, 1 byte for Frame ID, 2 bytes for Payload Length, 1 byte for Secret Flag, 1 byte for Number of SubFrames)
    SubFrame Header Format: '>BH' (Big-endian, 1 byte for Frame Type, 2 bytes for Frame Length)

### Task Requirements:
- In the provided template there is one predefined function `parse_data` which takes as an input parameter binary encoded messages. 
- During the test runs `parse_data` function will be called, and it has to return decoded message in correct format. 
- You are supposed to fill in the implementation of the function `parse_data`, so it works as described.
- You are allowed (encouraged) to create additional classes and functions for your implementation. Provided `parse_data` should be just staging point for your solution.

Required output format
    
    {FrameHeader[Frame ID,Payload Length,Secret Flag,Number of SubFrames]:FramePayload[<SubFrameHeader[Frame Type,Frame Length]:SubFrameData[Frame Data]>,<SubFrameHeader[Frame Type,Frame Length]:SubFrameData[Frame Data]>]}->Space separated Frame Data of each SubFrame

Meaning that for following decoded message:
    
    SimpleFrame:
        Header:
            Frame ID: 1
            Payload Length: 10
            Secret Flag: 0
            Number of SubFrames: 2
        Payload:
            SubFrame:
                Frame Type: 1
                Frame Length: 5
                Frame Data: Hello
            SubFrame:
                Frame Type: 1
                Frame Length: 6
                Frame Data: World!

The output will be as follows:

    {FrameHeader[1,10,0,2]:FramePayload[<SubFrameHeader[1,5]:SubFrameData[Hello]>,<SubFrameHeader[1,6]:SubFrameData[World!]>]}->Hello World!

### Aditional information

The basic interface is prepared in provided [template](05_simple_protocol.py).

Put genuine effort into considering object-oriented programming (OOP) design, as investing time in it will significantly simplify your solution.

All necessary modules (io, struct) are already imported. It is not allowed to use any other import. **Assignment with additional imports will fail automatically.**
