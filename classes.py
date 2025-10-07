class Gerador_Relatorios:
    def gerar(self, *args, **kwargs):
        relatorio = ""

        match len(args):
            case 1:
                #Se apenas 1 argumento foi passado, ele assume que é o corpo do relatório.
                relatorio = args[0]
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case _:
                pass
            
        if kwargs:
            pass

        return relatorio   # <-- ESSENCIAL
