### Para Treinar a Rede
```
ludwig experiment   --dataset audio_dataset.csv   --config_file config_file.yaml
```

### Clonar repositório
```
git clone https://github.com/AlvimPedro/audio_transversal2.git
```

### Instalando miniconda
```
cd audio_transversal2
bash Miniconda3-py39_4.10.3-Linux-x86_64.sh
```
Após a instalação fechar e abrir o terminal para ter efeito e então continuar:
```
conda config --set auto_activate_base false
```
Fechar e reabrir o terminal novamente.

### Criação do ambiente virtual com miniconda
```
conda create -n ludwig-audio
conda activate ludwig-audio
```

### Instalação do ambiente
```
pip install testresources
pip install ludwig
pip install ludwig[audio]
pip install petastorm
sudo apt-get install libjack-jackd2-dev portaudio19-dev
pip install PyAudio
pip install mysql-connector-python
```

### Colocar ID da coletora, latitude e longitude
```
echo "[id_coletora] [latitude] [longitude]" > info_coletora.txt
```
Exemplo:
```
echo "2  -15.873972 -47.821119" > info_coletora.txt
```

### Para rodar o script do projeto
```
python3 predict.py
```
