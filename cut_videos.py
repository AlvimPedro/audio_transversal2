import os
import subprocess

# dir = './Chainsaw' #Mudar a classe aqui
dir = input('Digite o diretório onde estão os videos a serem cortados: ')
label = '0'

for diretorio, subpastas, arquivos in os.walk(dir):
    for arquivo in arquivos:
        params = arquivo.split('_')
        id = params[0]
        time = params[2].split('.')[0]
        novo_arquivo = './audio_dataset_cortado/' + label + '_' + id + '.wav'

        subprocess.run(['ffmpeg', '-ss', time, '-i', dir+'/'+arquivo, '-t', '10', '-vcodec', 'copy', '-acodec', 'copy', novo_arquivo])

        