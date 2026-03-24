import requests #Import the requests library to handle HTTP requests
import json #Import the json library to handle JSON data

def emotion_detector(text_to_analyze): #Define a function named sentiment_analyzer that takes a string input called text_to_analyze
    # Define the API endpoint and your API key
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
     
    #Constructin the request payload in the expected format for the API
    myobj = {
        "raw_document": {"text": text_to_analyze}
        }
     
    #Custom header specifying the model ID to be used for sentiment analysis service.
    header = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
        }
    
    #Sending a POST request to the sentiment analysis API 
    response = requests.post(url, json=myobj, headers=header)

    # Manejo de error para entradas en blanco (status code 400)
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }



    # Paso 1: Convertir el texto de respuesta a diccionario
    response_dict = json.loads(response.text)

    # Paso 2: Extraer las emociones
    emotions = response_dict['emotionPredictions'][0]['emotion']

    anger_score   = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score    = emotions['fear']
    joy_score     = emotions['joy']
    sadness_score = emotions['sadness']

    # Paso 3: Encontrar la emoción dominante
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)

    # Paso 4: Retornar el formato requerido
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
