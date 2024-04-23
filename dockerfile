# Usa a imagem oficial do Botpress como base
FROM botpress/server:v12_26_7

# Define o diretório de trabalho no contêiner
WORKDIR /botpress

# Copia a pasta 'botpress' do seu diretório local para o diretório de trabalho no contêiner
COPY /botpress/ /botpress/

# Expõe a porta 3000 para acesso externo
EXPOSE 3000

# Executa o Botpress ao iniciar o contêiner
CMD ["./bp"]
