import modem as modem
import fileConvert as convert

def fileDecode(inputWAV, mNum):
    modType = modem.QAMModem(mNum)
    output = modem.demodulate(modType, inputWAV)
    output = convert.convert2File(output)
    return output