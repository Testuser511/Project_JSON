import json

data = {
    "groupname": "vpi22",
    "Makbuk": {
        "firstName": "timur",
        "lastName": "tarkovskiy",
        "Patronymic": "makbukovich",
        "phoneNumber": 88005553535,
        "vkId": "vk.com/blablabla"
    },
    "Jorik": {
        "firstName": "Georgiy",
        "lastName": "Ogre",
        "Patronymic": "Grigorievich",
        "phoneNumber": 88005553636,
        "vkId": "vk.com/georgiy111"
    },
    "Vanek": {
        "firstName": "Ivan",
        "lastName": "Ivanickiy",
        "Patronymic": "Ivanov",
        "phoneNumber": 88004443535,
        "vkId": "vk.com/vanek02"
    },
    "Dimon": {
        "firstName": "Dmitriy",
        "lastName": "Dmitriev",
        "Patronymic": "Dmitrievich",
        "phoneNumber": 88002224535,
        "vkId": "vk.com/dimooooon"
    },
}
with open('jsonvpi22.json', 'w') as outfile:
    json.dump(data, outfile)