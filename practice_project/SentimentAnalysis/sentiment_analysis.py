'''
This is tested by starting a python3.11 shell and executing the test steps from that shell

Command to start python shell:	
	python3.11
	
Commands once inside the python shell
		---  Either without creating a package
	>>> from sentiment_analysis import sentiment_analyzer
	>>> sentiment_analyzer("I love this new technology")
	
		--- Or with creating a package called SentimentAnalysis
	
	>>> from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
	>>> sentiment_analyzer("I love this new technology")

Results shown in python shell:
	
	{'label': 'SENT_POSITIVE', 'score': 0.996954}
>>> 
'''

import requests
import json

def sentiment_analyzer(text_to_analyse):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Custom header specifying the model ID for the sentiment analysis service
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting sentiment label and score from the response
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']

    # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}