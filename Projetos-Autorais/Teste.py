'''with open("imagem.jpg", "rb") as arquivo_jpeg:
    # Lendo o cabeçalho do arquivo JPEG
    cabecalho = arquivo_jpeg.read(512)

    # Verificando se o arquivo é um JPEG
    if cabecalho.startswith(b"\xFF\xD8"):
        # Localizando o início da seção de dados
        dados_inicio = cabecalho.find(b"\xFF\xDA") + 2

        # Localizando o fim da seção de dados
        dados_fim = cabecalho.find(b"\xFF\xD9")

        # Extraindo a seção de dados
        dados = cabecalho[dados_inicio:dados_fim]

        # Convertendo os dados para uma matriz de pixels
        pixels = [[], [], []]
        for i in range(0, len(dados), 3):
            r, g, b = dados[i:i+3]
            pixels[0].append(int(0.299 * r + 0.587 * g + 0.114 * b)) # componente de luminância
            pixels[1].append(0) # sem componente de crominância
            pixels[2].append(0) # sem componente de crominância

        # Salvando os dados da imagem em preto e branco
        with open("imagem_pb.jpg", "wb") as arquivo_pb:
            # Escrevendo o cabeçalho do arquivo JPEG
            arquivo_pb.write(cabecalho[:dados_inicio])

            # Escrevendo a seção de dados em preto e branco
            for i in range(0, len(dados), 3):
                arquivo_pb.write(bytes(pixels[0][i:i+3]))

            # Escrevendo o restante do arquivo JPEG
            arquivo_pb.write(cabecalho[dados_fim:])'''
