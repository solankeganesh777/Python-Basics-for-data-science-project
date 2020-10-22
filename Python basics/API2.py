#API Part 2

#IBM Speech to text API

!pip install ibm_watson wget

#Speech to text

from ibm_watson import SpeechToTextV1
import json
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

#The service endpoint is based on the location of the service instance, 
#we store the information in the variable URL. 
#To find out which URL to use, view the service credentials
url_s2t = "https://stream.watsonplatform.net/speech-to-text/api"

#API Key
iam_apikey_s2t = "UQod4SGA2dPgCfBmew1lvV5ukmomVADJd3g_oIRRstV6"

#You create a Speech To Text Adapter object the parameters are the endpoint and API key.
authenticator = IAMAuthenticator(iam_apikey_s2t)
s2t = SpeechToTextV1(authenticator=authenticator)
s2t.set_service_url(url_s2t)
s2t

#Download audio file, which is to be converted to text
!wget -O PolynomialRegressionandPipelines.mp3  https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/labs/PolynomialRegressionandPipelines.mp3

#We have the path of the wav file we would like to convert to text    
filename='PolynomialRegressionandPipelines.mp3'

"""
We create the file object wav, with the wav file using open ;
we set the mode to "rb" , this is similar to read mode,
but it ensures the file is in binary mode.
We use the method recognize to return the recognized text. 
The parameter audio is the file object wav, 
the parameter content_type is the format of the audio file.
"""

with open(filename, mode="rb")  as wav:
    response = s2t.recognize(audio=wav, content_type='audio/mp3')
    
#The attribute result contains a dictionary that includes the translation
response.result

from pandas.io.json import json_normalize

json_normalize(response.result['results'],"alternatives")
response

# obtain the recognized text and assign it to the variable recognized_text

recognized_text=response.result['results'][0]["alternatives"][0]["transcript"]
type(recognized_text)
print(recognized_text)

#IBM Language Translator API

from ibm_watson import LanguageTranslatorV3

#The service endpoint is based on the location of the service instance, 
#we store the information in the variable URL. 
#To find out which URL to use, view the service credentials
url_lt='https://gateway.watsonplatform.net/language-translator/api'

#API Key
apikey_lt='TwZ-JNcr7tDffFE3ic5ytjLS9aruuQYOPK2FHH07tu8X'

#API requests require a version parameter that takes a date in the format version=YYYY-MM-DD
version_lt='2018-05-01'

#Creating object language_translator
authenticator = IAMAuthenticator(apikey_lt)
language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
language_translator.set_service_url(url_lt)
language_translator

"""
Get a Lists the languages that the service can identify. 
The method Returns the language code.
For example English (en) to Spanis (es) and name of each language.
"""
from pandas.io.json import json_normalize
json_normalize(language_translator.list_identifiable_languages().get_result(), "languages")

"""
We can use the method translate this will translate the text.
The parameter text is the text.
Model_id is the type of model we would like to use use we use list the the langwich . 
In this case, we set it to 'en-es' or English to Spanish.
We get a Detailed Response object translation_response
"""
translation_response = language_translator.translate(text=recognized_text, model_id='en-es')
translation_response

#Result is dictionary
translation=translation_response.get_result()
translation

#Actual translation is obtained as string
spanish_translation =translation['translations'][0]['translation']
spanish_translation 

#Translate back to english
translation_new = language_translator.translate(text=spanish_translation ,model_id='es-en').get_result()

translation_eng=translation_new['translations'][0]['translation']
translation_en
