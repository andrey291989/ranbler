import requests


# cписок групп в которых нужно узнать сколько подписчиком в ней
id = ['rambler', 'ramblermail', 'horoscopesrambler', 'championat',
      'championat.auto', 'championat_cybersport', 'livejournal', 'afisha']
# Токен для подключения к API
toc = ''

def namder(id, toc):
    """Возвращает список из кортежей [(имя группы, кол-во участников), ...]
    на вход принимает id = список из id группы и toc = access_token"""
    li = []
    li_1 = []
    for i in id:
        url = 'https://api.vk.com/method/groups.getMembers?group_id=' + i + '&count=0&access_token=' + toc + 'e&v=5.95'
        response = requests.get(url)
        data = response.json()
        li.append(i)
        li.append(data['response']['count'])
        e = tuple(li)
        li = []
        li_1.append(e)
    return li_1



if __name__ == '__main__':
    namder(id, toc)
