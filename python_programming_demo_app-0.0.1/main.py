import roboter.controller.conversation
cols = ["red", "green", "blue", "yellow"]
for count in range(1):
    roboter.controller.conversation.talk_about_restaurant(color = cols[count])
