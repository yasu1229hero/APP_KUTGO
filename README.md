# KUTGO
## About this App
This App name is KUTGO, and this App introduces open campus of our university for foreign students because it is difficult to understand Japanese for them. The 3 main functions are followings:

1. GoChat (App users talk with Chatbot and can ask about KUT.)

2. GoRoom (App users can check a laboratory's information that they're interested in and the current number of people in the laboratory.)

3. GoSchedule (App users select laboratories and facilities where they want to go, and then App provide the best route following the select.)

By this application, app users can:
1. know about KUT in English
2. check congestion of all room
3. look around many laboratories and facilities in KUT, efficiently

## All code for implementation
- GoChat
    - `Chatbot/KutGo`
- GoRoom
    - `app/darknet/goroom.py`
- GoSchedule
    - `app/darknet/labrecommend.py`
    - `app/routerecommend.py`

## How to build their function
- GoChat
    - Using Google Framework
- GoRoom
    - Raspberry Pi with Web camera is put in one cornar of a room, and the raspberry Pi take a picture once in 5 minutes and send the picture to server(AWS). The server extract `person` within a image using Yolov3. Finally, the server count number of the `person` and show the number.
- GoSchedule
    - A route is determined by the number of selected rooms in each building. For example, if App users select 5 rooms in A-building, 4 rooms in C-building, and 2 rooms in B-building, the best route becomes A-building -> C-building -> B-building. Thus, A-building becomes the start point and B-building becomes the final point.
After the determination of the best route, the start point, final point, and the route are drawn to map of our university. 


## What the code can do and output? Explain Processing of the code
```You can see the function and output on each of the code. Processing of the code also included in the comment of the code```
