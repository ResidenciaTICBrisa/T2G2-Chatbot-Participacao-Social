#!/bin/bash

# Atualização do sistema
sudo apt update && sudo apt upgrade -y

# Instalação de pacotes necessários
sudo apt-get install -y ca-certificates curl

# Criação do diretório para a chave GPG do Docker
sudo install -m 0755 -d /etc/apt/keyrings

# Baixando a chave GPG oficial do Docker
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Adicionando o repositório do Docker às fontes do APT
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Atualizando a lista de pacotes com o novo repositório do Docker
sudo apt-get update

# Instalando Docker compose e outros pacotes
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

