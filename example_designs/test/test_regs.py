def main(wb):
    wb.open()
    # # #
    identifier = ""
    for i in range(30):
        identifier += chr(wb.read(wb.bases.identifier_mem + 4*(i+1))) # TODO: why + 1?
    print(identifier)
    print("frequency : {}MHz".format(wb.constants.system_clock_frequency/1000000))
    # # #
    wb.close()
