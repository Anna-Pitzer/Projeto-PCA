from modules.operacoes import *
from modules.arquivos import *
import sys


if __name__ == '__main__':
    edit = False
    op = Options(edit)


    match op:
        case 1:
            data = ReadInfo(op)
            CreateDF(data)

        #case 2:
            #Opcao Pesquisar

        case 3:
            sys.exit(0)