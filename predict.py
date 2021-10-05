from ludwig.api import LudwigModel

import threading

import gravarAudio as gravar

model = LudwigModel.load('./results/experiment_run_5/model/')

def thread_prediction():
    predictions, output_directory = model.predict(dataset='./audio_predict.csv')   

    print(predictions.label_probabilities_0[0])
    print(predictions.label_probabilities_1[0])
    print(predictions.label_probabilities_2[0])
    print(predictions.label_probabilities_4[0])

while True:
    gravar.gravarAudio(10, './prediction/gravacao.wav')

    threading.Thread(target=thread_prediction).start()
    
    

    