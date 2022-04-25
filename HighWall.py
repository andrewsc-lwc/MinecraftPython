def on_on_chat():
    agent.teleport_to_player()
    agent.move(FORWARD, 1)
    agent.set_item(STONE, 1, 1)
    agent.move(UP,1)
    length = 12
    height = 14
    for y in range(0,height):
        for x in range(0,length):
            agent.place(DOWN)
            agent.move(FORWARD,1)
        agent.move(UP,1)
        agent.move(BACK,10)
	
player.on_chat("run", on_on_chat)
