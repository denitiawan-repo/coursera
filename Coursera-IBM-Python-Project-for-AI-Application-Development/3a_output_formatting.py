from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

def emotion_predictor(text, service_url, api_key, version):
    # Initialize Watson NLU service
    nlu = NaturalLanguageUnderstandingV1(version=version, iam_apikey=api_key, url=service_url)

    # Analyze emotions in text
    response = nlu.analyze(text=text, features=Features(emotion=EmotionOptions())).get_result()

    # Extract emotions from the response
    emotions = response['emotion']['document']['emotion']

    return emotions

# Example usage
text = 'Your text goes here.'
service_url = 'YOUR_SERVICE_URL'
api_key = 'YOUR_API_KEY'
version = 'YOUR_VERSION'

emotions = emotion_predictor(text, service_url, api_key, version)

# Format the output
formatted_output = {key: round(value, 2) for key, value in emotions.items()}
print(formatted_output)
