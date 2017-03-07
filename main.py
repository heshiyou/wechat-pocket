# coding: utf-8


import itchat
import logging
import pocket

import settings
import robot


logger = logging.getLogger('wechat-pocket')
if settings.DEBUG:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


@itchat.msg_register(itchat.content.SHARING, isFriendChat=True)
def sharing_handler(msg):
    answer = ''
    # get the link from msg
    url = msg['Url']
    if url:
        pocket_instance = pocket.Pocket(consumer_key=settings.CONSUMER_KEY, access_token=settings.ACCESS_TOKEN)
        resp = pocket_instance.add(url)
        logger.debug(resp)
        answer = '[OK]✌️ saved successful!'
    return answer


@itchat.msg_register([itchat.content.TEXT], isFriendChat=True)
def text_handler(msg):

    def get_location(_user):
        province = _user['Province']
        city = _user['City']

        if province in ('北京', '上海', '天津', '重庆'):
            return '{}市{}区'.format(province, city)
        elif province and city:
            return '{}省{}市'.format(province, city)
        else:
            return ''

    logger.debug(msg)
    user_name = msg['FromUserName']
    user = itchat.search_friends(userName=user_name)
    logger.debug(user)
    location = get_location(user)
    logger.debug(location)
    tuling = robot.Tuling(settings.TULING_KEY)
    return tuling.reply_text(msg['Text'], user_name, location)


if __name__ == '__main__':
    itchat.auto_login()
    itchat.run(debug=settings.DEBUG)

