'''
This module is to initialize the server
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector


app = Flask("Emotion Detector")
@app.route('/emotionDetector')
def emo_detector():
    '''
    This function is to take the text from the front end and run the emotion detection algo
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominent_emotion']
    if dominant_emotion is None:
        return "Invalid Text! Please try again"
    return (f"For the given statement, the system response is: "
            f"anger: {anger}, disgust: {disgust}, fear: {fear}, joy: {joy}, sadness: {sadness}."
            f"The dominant emotion is {dominant_emotion}")

@app.route('/')
def render_index_page():
    '''
    This function is to render the index.html
    '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 9000)
