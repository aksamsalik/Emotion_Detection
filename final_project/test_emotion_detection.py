from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        RESULT_1 = emotion_detector("I am glad this happened")
        self.assertEqual(RESULT_1['dominant_emotion'], 'joy')

        RESULT_2 = emotion_detector("I am really mad about this")
        self.assertEqual(RESULT_2['dominant_emotion'], 'anger')

        RESULT_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(RESULT_3['dominant_emotion'], 'disgust')

        RESULT_4 = emotion_detector("I am so sad about this")
        self.assertEqual(RESULT_4['dominant_emotion'], 'sadness')

        RESULT_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(RESULT_5['dominant_emotion'], 'fear')

unittest.main()