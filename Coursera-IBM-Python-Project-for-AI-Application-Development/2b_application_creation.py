from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Authenticate with Watson NLU service
authenticator = IAMAuthenticator('<YOUR_API_KEY>')
nlu = NaturalLanguageUnderstandingV1(
    version='2021-03-25',
    authenticator=authenticator
)

nlu.set_service_url('<YOUR_SERVICE_URL>')

# Analyze text for emotions
response = nlu.analyze(
    text='I am feeling happy today!',
    features=Features(emotion=EmotionOptions())
).get_result()

# Process emotion results
emotions = response['emotion']['document']['emotion']
print(emotions)
