import json
import random

class Vivoresponse:
    def __init__(self, status_code, data=None, text=None):
        self.status_code = status_code
        self.data = data
        self.text = text
    def json(self):
        return self.data
    

class Vivorequest:
    def __init__(self):
        pass

    def post(url, json, headers, params):
        def authcheck(headers):
            return 1 if headers.get('X-AI-GATEWAY-APP-ID', '') == '20240422' else 0
        def urlcheck(url):
            return 1 if url == 'https://api-ai.vivo.com.cn/vivogpt/completions' else 0
        response = Vivoresponse(status_code=200)
        response_database = ['您好，我的名字是蓝心小V，我是一款人工智能助手。我可以回答各种问题和提供各种服务，例如聊天、翻译、计算、推荐等等。如果您有任何问题或需要帮助，请随时告诉我，我会尽力为您提供最好的服务。',
        '这是一个随机固定回复1',
        '这是一个随机固定回复2',
        '这是一个随机固定回复3',
        '这是一个随机固定回复4']
        random_num = random.randint(0, 4)
        # Check authorization
        if authcheck(headers) == 0:
            response.status_code = 401
            response.text = '{"message": "Invalid access key"}'
            return response
        # Check URL validity
        if urlcheck(url) == 0:
            response.status_code = 404
            response.text = '{"error_msg": "404 Route Not Found"}'
            return response
        # If both checks pass, prepare the response data
        response.data = {
            'code': 0,
            'data': {
                'sessionId': json['sessionId'],
                'requestId': params['requestId'],
                'content': response_database[random_num],
                'image': None,
                'functionCall': None,
                'toolCall': None,
                'toolCalls': None,
                'contentList': None,
                'searchInfo': None,
                'usage': {
                    'promptTokens': None,
                    'completionTokens': None,
                    'totalTokens': None,
                    'duration': None
                },
                'provider': 'vivo',
                'model': 'vivo-BlueLM-TB',
                'finishReason': 'STOP'
            },
            'msg': 'done.'
        }
        return response



