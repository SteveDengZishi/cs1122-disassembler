'''
Deng Zishi
zd475
disassembler
'''
# Operation code to mnemonic dictionary
# You can use this to lookup the machine code
# and translate it to the mnemonic instruction
INS_REF = {
    "1": "ADD",
    "2": "SUB",
    "3": "STA",
    "5": "LDA",
    "6": "BRA",
    "7": "BRZ",
    "8": "BRP"
}

def disassemble(operation_code):
    # this function should take in an integer operation code
    # and convert it to a LMC mnemonic instruction and return
    # it as a string
    if operation_code[0] == "9":
        if operation_code[2] == "1":
            return "INP"
        elif operation_code[2] == "2":
            return "OUT"
    elif operation_code[0] == "0":
        return "HLT"
    else:
        return INS_REF[operation_code[0]]
    

def main():
    # The main function should read all operation codes from the
    # user until the HLT instruction is read. Once it is read,
    # all operation codes should be disassembled using "disasassembled"
    # and then printed out to the user
    disassembled = []
    instruction = input("Please input a operation code until '000': ")
    disassembled.append(disassemble(instruction))
    while instruction != "000":
        instruction = input("Please input a operation code until '000': ")
        disassembleCode = disassemble(instruction)
        if disassembleCode == "ADD" or disassembleCode == "SUB" or disassembleCode == "STA":
            disassembleCode = disassembleCode + " " + instruction[1:]
        disassembled.append(disassembleCode)
    if instruction == "000":
        for i in range(len(disassembled)):
            print(disassembled[i])

main()
