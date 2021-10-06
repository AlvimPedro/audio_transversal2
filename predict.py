from ludwig.api import LudwigModel

import threading

import gravarAudio as gravar

import mysql.connector

def mysql_data_send(sql, val):
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    mycursor.execute(sql, val)

    mydb.commit()

def thread_prediction(model):
    predictions, output_directory = model.predict(dataset='./audio_predict.csv')   

    print(predictions.label_probabilities_0[0])
    print(predictions.label_probabilities_1[0])
    print(predictions.label_probabilities_2[0])
    print(predictions.label_probabilities_4[0])

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = ("John", "Highway 21")   

    mysql_data_send(sql, val)

def main():
    model = LudwigModel.load('./results/experiment_run_5/model/')

    while True:
        gravar.gravarAudio(10, './prediction/gravacao.wav')

        threading.Thread(target=thread_prediction(model)).start()

if __name__ == '__main__':
    main()
        
    

    