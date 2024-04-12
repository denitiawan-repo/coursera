from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Authenticate
authenticator = IAMAuthenticator('<api_key>')
nlu = NaturalLanguageUnderstandingV1(version='2021-08-01', authenticator=authenticator)
nlu.set_service_url('<service_url>')

# Analyze emotions
text = "I am feeling happy today!"
response = nlu.analyze(text=text, features=Features(emotion=EmotionOptions())).get_result()

# Extract emotions
emotions = response['emotion']['document']['emotion']
print(emotions)
