import modem as modem
import fileConvert as convert

def fileEncode(inputFile, mNum):
    input = convert.convert2BIN(inputFile)
    modType = modem.QAMModem(mNum)
    output = modem.modulate(modType, input)
    return output