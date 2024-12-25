def encoder():
    print("This program converts a textual messages into a sequence")
    print("of numbers representing the Unicode encoding.\n")

    #Get teh message to encode
    message = input("Please enter the message to encode:")
    print("\n Here are the unicode codes:")

    # Loop through the message and print out the Unicode values
    for ch in message:
        print(ord(ch), end=" ")
    print() #blank line after the loop

#Call the main function to run the porgram
encoder()

def decoder():
    print("This program converts a sequence of Unicode numbers into")
    print("the string of text that it represents.\n")

    # Get the message to encode
    inString = input("Please enter the Unicode-encoded message:")

    # Loop through each substring and build Unicode message
    message = ""
    for numStr in inString.split():
        # convert the (sub) string to a number
        codeNum = int(numStr)
        message += chr(codeNum)
    
    print("\n The decoded message is :", message)

# calling the main function to execute the program
decoder()
        