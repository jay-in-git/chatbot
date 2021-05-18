
from linebot.models import (
    MessageEvent, FollowEvent, TextMessage, TextSendMessage
)
from linebot.models import (
    TemplateSendMessage, CarouselTemplate, CarouselColumn, PostbackTemplateAction, MessageTemplateAction, URITemplateAction
)

def handleFollow():
    message = TemplateSendMessage(
            alt_text='Action List', 
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://imgur.com/P9CHBgP.png',
                        title='Profile',
                        text='The resume and introduction of Jay',
                        actions=[
                            MessageTemplateAction(
                                label='View Introduction',
                                text='Introduction'
                            ),
                            URITemplateAction(
                                label='Resume, Transcript',
                                uri='https://drive.google.com/drive/folders/1BU3uA-FH03rizBMvLScJcq6ThwVni6l8?usp=sharing'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://imgur.com/vUZhiXQ.png',
                        title='Projects',
                        text='The side projects and course projects of Jay.',
                        actions=[
                            MessageTemplateAction(
                                label='View all Projects',
                                text='Projects'
                            ),
                            URITemplateAction(
                                label='Github Link',
                                uri='https://github.com/jay-in-git'
                            )
                        ]
                    ),
                ]
            )
        )
    return message

def handleText(text):
    if text == 'Introduction':
        with open('introduction.txt') as f:
            message = TextSendMessage(text=''.join(f.readlines()))
    elif text == 'Projects':
        
def getResponse(event=None):
    if isinstance(event, FollowEvent):
        message = handleFollow()
    elif isinstance(event, MessageEvent) and isinstance(event.message, TextMessage):
        message = handleText(event.message.text)
    else:
        message = TextSendMessage(text='Click the blocks above to get the information!')
    return message