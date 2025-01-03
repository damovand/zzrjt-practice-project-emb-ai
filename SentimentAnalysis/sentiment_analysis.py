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

    ''' for testing with python3.11 directly ONLY - 
    # to use this test tool it require to hard code a text in myobj
    # print(response.status_code)
    '''
    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting sentiment label and score from the response
    # If the response status code is 200, extract the label and score from the response
    
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    # If the response status code is 500, set label and score to None
    else:
        label = None
        score = None


    # Returning a dictionary containing sentiment analysis results
    return {'label': label, 'score': score}