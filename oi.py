from interpreter import interpreter

#interpreter.offline = True # Disables online features like Open Procedures
interpreter.llm.model = "dolphin-mistral:latest"
interpreter.llm.api_base = "http://10.0.255.147:11434/v1"
interpreter.llm.max_tokens = 2048
interpreter.llm.context_window = 16000

#interpreter.computer.run("python", "print('Hello World!')")

#interpreter.chat() # Executes a single command
#interpreter.chat("%verbose true")
interpreter.chat("""ssh devusr@10.0.255.44 'ping -c3 8.8.8.8\n'""")
#print(interpreter.system_message)