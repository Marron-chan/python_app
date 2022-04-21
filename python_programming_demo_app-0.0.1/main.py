import roboter.controller.conversation
cols = ["red", "green", "blue", "yellow"]
for count in range(4):
    roboter.controller.conversation.talk_about_restaurant(cols[count])
