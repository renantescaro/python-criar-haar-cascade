* Criar pasta de trabalho:
sudo mkdir nome_pasta

* Permissão na pasta
sudo chmod -R 777 nome_pasta

* Entrar na pasta
cd nome_pasta

* Clonar repositório do OpenCv
git clone https://github.com/Itseez/opencv.git

* Instalar dependências
sudo apt-get install build-essential
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev

* Se der erro no último comando, instalar pacote por pacote:
sudo apt install python-dev
sudo apt install python3-numpy
etc

* Se der o erro 'Unable to locate package libjasper-dev':

sudo nano /etc/apt/sources.list
Adicionar:
deb http://ftp.fau.de/trinity/trinity-builddeps-r14.0.0/ubuntu/ bionic main

* Atualizar chaves
sudo apt-key adv --keyserver keyserver.quickbuild.io --recv-keys F5CFC95C

* Atualizar repositório local
sudo apt-get update

* Tentar instalar libjasper-dev
sudo apt-get install libjasper-dev

* Se der erro 'chave pública não disponível':
sudo apt-key adv --keyserver hkp://pool.sks-keyservers.net:80 --recv-keys CHAVE_DO_ERRO

* Tente instalar o libjasper-dev novamente
sudo apt-get install libjasper-dev