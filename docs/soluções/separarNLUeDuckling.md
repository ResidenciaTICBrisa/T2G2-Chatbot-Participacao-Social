### Hospedando o NLU e Duckling Localmente no Botpress

Por padrão, o Botpress utiliza o serviço Duckling e consulta o NLU em servidores remotos, o que implica que todas as requisições são encaminhadas e aguardam o retorno desses servidores. Dependendo da conexão com a internet, esse processo pode ser lento, comprometendo a eficiência do bot.

Essa documentação é destinada a desenvolvedores que desejam hospedar o NLU e o Duckling localmente, proporcionando uma significativa melhoria no tempo de resposta das requisições. Testes realizados com usuários mostraram uma diferença notável na rapidez das respostas ao adotar essa configuração local.

#### Configuração no Docker Compose ou Dockerfile

Primeiro, verifique se o arquivo `nlu.json`, localizado em `data/global/config/nlu.json`, contém as seguintes configurações:

```json
{
  "ducklingURL": "http://localhost:8000",
  "languageSources": [
    {
      "endpoint": "http://localhost:3100"
    }
  ]
}
```

Para baixar os binários do modelo de linguagem, acesse o link https://botpress-public.nyc3.digitaloceanspaces.com/embeddings/index.json e escolha o arquivo BPE referente ao idioma desejado, juntamente com o tamanho do NLU. O NLU é responsável pelo reconhecimento de tokens, e você pode ajustar a capacidade conforme necessário. No Dockerfile localizado na raiz do projeto, inserimos as URLs para o BPE e o modelo NLU, com a configuração padrão para o idioma português e 100 dimensões.

Execute os comandos abaixo para baixar os binários:
```bash
wget --progress=bar http://botpress-public.nyc3.digitaloceanspaces.com/embeddings/bp.pt.bpe.model && \
wget --progress=bar http://botpress-public.nyc3.digitaloceanspaces.com/embeddings/bp.pt.100.bin && \
```

Certifique-se de ajustar o parâmetro de dimensão na URL com o mesmo valor do parâmetro --dim especificado:

```bash
command: bash -c "./duckling & ./bp lang --offline --dim 100 --langDir /botpress & ./bp"
```

Essa configuração permitirá que tanto o Duckling quanto o NLU rodem localmente, resultando em tempos de resposta mais rápidos e um desempenho geral melhorado.
## Histórico de versão

| Versão |    Data    |                       Descrição                       |      Autor       |
| :----: | :--------: | :---------------------------------------------------: | :--------------: |
|  1.0   | 14/08/2024 |           Criação do documento                        |  Gabriel Scheidt   |
