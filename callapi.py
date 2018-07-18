
# import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import json
import requests

from matplotlib import style

data1 = []
data2 = []
def create_odds_generator():   
    # for i in range(to):
    api_url = "http://localhost:3000/randomInt"
    response = requests.get(api_url, headers={'Content-Type': 'application/json'})
        #     print(response)
    if response.status_code == 200:
        content = json.loads(response.content.decode('utf-8'))
        if content['status']:
            data1.extend([content['status']])
            data2.extend([content['status']])
            print(data1)
            return data1
                    # time.sleep(1)

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
def animate(i):
#     xar = []
#     yar = []
    dataall = create_odds_generator()
#         xar.append(int(x))
#         yar.append(int(y))
    print(dataall)
#                 time.sleep(1)
#                 print(data)
#                 x.append(int(dd))
    ax1.clear()        
    ax1.plot(dataall)
            
ani = animation.FuncAnimation(fig, animate, interval=5000)
plt.show() 