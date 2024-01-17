with open("./FileHandling/op-file.txt","at") as op_file:
    with open("./FileHandling/file.txt","rt") as ip_file:
        lines = ip_file.readlines()
        for line in lines:
            op_file.write(line)
        op_file.writelines(["\nGood night!","\nGoodbye!"])
        ip_file.close()
    op_file.close()