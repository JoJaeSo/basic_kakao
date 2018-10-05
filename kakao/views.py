from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def on_init(request):
    # 그냥 리턴하는 경우 dict 에 status_code가 없다며 에러 발생.
    return JsonResponse ({
        'type': 'buttons',
        'buttons': ['안녕하세요. :)'],
    })


@csrf_exempt
def on_message(request):

    json_str = ((request.body).decode('utf-8'))
    json_data = json.loads(json_str)
        
    print(json_data)
    
    if json_data['type'] == 'text':
        session_id = request.user.username
        print(session_id)
        speech = "테스트 메세지"
    else:
        speech = '{}타입 메세지는 지원하지 않습니다.'.format(json_data['type'])

    return JsonResponse({
        'message': {
            'text': speech,
        },
        "keyboard": {
            "type": "buttons",
            "buttons": [
              "버튼 1",
              "버튼 2",
              "버튼 3"
            ]
        }
    })


def on_added(request):
    pass

def on_block(request, user_key):
    pass