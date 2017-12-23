""" Удаляет все записи со стены ПРОТОТИП"""

import math
from time import sleep

from vkapi import VK

TOKEN = "token here"
vk = VK(TOKEN)

# получение всех записей стены
posts_count = vk.api("wall.get", count=0)["response"]["count"]
print("Posts: ", posts_count)

# вычисляем количество офсетов
multiplier = 0
if posts_count >= 100:
    offsets = math.ceil(posts_count / 100)
else:
    offsets = 1

post_ides = []
# обходим все записи со стены
for i in range(offsets):
    posts = vk.api("wall.get", count=100,
                   offset=0 + 100 * multiplier)["response"]
    # получаем id записей
    post_ides.extend([x["id"] for x in posts["items"]])
    multiplier += 1
    sleep(0.3)

for i in post_ides:
    status = vk.api("wall.delete", post_id=i)
    print(status, "{}/{}".format(i, posts_count))
    sleep(0.35)
print("Done!")
