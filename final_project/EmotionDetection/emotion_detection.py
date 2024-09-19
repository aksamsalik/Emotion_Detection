'''
This code is to detect emotions in the text
'''
import requests
import json
def emotion_detector(text_to_analyze):
    '''
    This function detects emotion in the given text
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = header)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        emotions = FORMATTED_RESPONSE['emotionPredictions'][0]['emotion']
        anger = emotions['anger']
        disgust = emotions['disgust']
        fear = emotions['fear']
        joy = emotions['joy']
        sadness = sadness['sadness']
        dominant_emotion = max(emotions, key = emotions.get)
    elif response.status_code == 400:
        emotions = None
        anger = None
        disgust = None
        fear = None
        joy = None
        sadness = None
        dominant_emotion = None
  
    return {'anger': anger, 
    'disgust': disgust, 
    'fear': fear, 
    'joy': joy, 
    'sadness': sadness, 
    'dominent_emotion': dominant_emotion}