from interpreter import interpreter

interpreter.offline = True # Disables online features like Open Procedures
interpreter.llm.api_key = "fake_key" # LiteLLM, which we use to talk to LM Studio, requires this
interpreter.llm.model = "dolphin-mistral:latest" # makes a big difference to the experience
interpreter.llm.api_base = "http://10.0.255.147:11434/v1" # the `/v1` is necessary

interpreter.llm.max_tokens = 1000
interpreter.llm.context_window = 3000

#interpreter.chat("install ping and check if 8.8.8.8 is up") # Executes a single command
interpreter.chat()