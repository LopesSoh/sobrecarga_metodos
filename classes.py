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
            case _ if len(args) > 3:
                # Case 4: título + dois ou mais parágrafos
                titulo = args[0]
                paragrafos = args[1:]  # todos os parágrafos depois do título
                relatorio = f"\n\n{'=' * 40}\n{titulo.upper()}\n{'=' * 40}\n"
                for i in range(len(paragrafos)):
                    relatorio += paragrafos[i]
                    if i < len(paragrafos) - 1:
                        relatorio += "\n\n"

        # Metadados opcionais em qualquer case
        if kwargs:
            relatorio += "\n\n" + "=" * 20 + " METADADOS " + "=" * 20 + "\n"
            for chave, valor in kwargs.items():
                relatorio += f"{chave.capitalize()}: {valor}\n"

        return relatorio   # <-- ESSENCIAL
