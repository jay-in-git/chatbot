
from linebot.models import (
    MessageEvent, FollowEvent, TextMessage, TextSendMessage
)
from linebot.models import (
    TemplateSendMessage, CarouselTemplate, CarouselColumn, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)
from linebot.models import (
    FlexSendMessage
)
import json

def handleFollow():
    num_block = 2
    urls = ['https://imgur.com/P9CHBgP.png', 'https://imgur.com/vUZhiXQ.png']
    titles = ['Profile', 'Projects']
    texts = ['The resume and introduction of Jay', 'The side projects and course projects of Jay.']
    message_acts = [{'label': 'View Introduction', 'text': 'Introduction'}, {'label': 'View all Projects', 'text': 'Projects'}]
    uri_acts = [{'label': 'Resume, Transcript', 'uri': 'https://drive.google.com/drive/folders/1BU3uA-FH03rizBMvLScJcq6ThwVni6l8?usp=sharing'}, {'label': 'Github Link', 'uri': 'https://github.com/jay-in-git'}]
    message = TemplateSendMessage(
            alt_text='Action List', 
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url=urls[i],
                        title=titles[i],
                        text=texts[i],
                        actions=[
                            MessageTemplateAction(
                                label=message_acts[i]['label'],
                                text=message_acts[i]['text']
                            ),
                            URITemplateAction(
                                label=uri_acts[i]['label'],
                                uri=uri_acts[i]['uri']
                            )
                        ]
                    ) for i in range(num_block) ]
            )
        )
    return message

def handleText(text):
    if text == 'Introduction':
        message = FlexSendMessage('Menu', json.load(open('introMenu.json','r',encoding='utf-8')))
    elif text == 'Projects':
        print('preparing')
    else:
        try:
            with open(f'textfiles/{text}.txt') as file:
                message = TextSendMessage(text=''.join(file.readlines()))
        except:
            message = TextSendMessage(text='Click the blocks above to get the information!')
    return message
def getResponse(event=None):
    if isinstance(event, FollowEvent):
        message = handleFollow()
    elif isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
        message = handleText(event.message.text)
    else:
        message = TextSendMessage(text='Click the blocks above to get the information!')
    return message