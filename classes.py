class Gerador_Relatorios:
    def gerar(self, *args, **kwargs):
        relatorio = ""

        match len(args):
            case 1:
                #Se apenas 1 argumento foi passado, ele assume que é o corpo do relatório.
                relatorio = args[0]
            case 2:
                #Se apenas 2 argumentos for passado, ele entende como um titulo e outro corpo de texto
                titulo, corpo = args
                relatorio = f"\n\n{'=' * 40}\n{titulo.upper()}\n{'=' * 40}\n{corpo}"
            case 3:
                titulo, corpo, rodape = args
                relatorio = (
                    f"\n\n{'=' * 40}\n{titulo.upper()}\n{'=' * 40}\n"
                    f"{corpo}\n{'-' * 40}\n{rodape}"
                )
            case 4:
                pass
            case _:
                pass
            
        if kwargs:
            pass

        return relatorio   # <-- ESSENCIAL
