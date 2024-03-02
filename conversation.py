from interpreter import OpenInterpreter

agent_1 = OpenInterpreter()
agent_1.system_message = "This is a seperate instance."

agent_2 = OpenInterpreter()
agent_2.system_message = "This is yet another instance."

def swap_roles(messages):
    for message in messages:
        if message['role'] == 'user':
            message['role'] = 'assistant'
        elif message['role'] == 'assistant':
            message['role'] = 'user'
    return messages

agents = [agent_1, agent_2]

# Kick off the conversation
messages = [{"role": "user", "type": "message", "content": "Hello!"}]

while True:
    for agent in agents:
        messages = agent.chat(messages)
        messages = swap_roles(messages)
