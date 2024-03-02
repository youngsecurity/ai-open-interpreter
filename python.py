from interpreter import interpreter

interpreter.offline = True # Disables online features like Open Procedures
interpreter.llm.model = "dolphin-mistral:latest"
interpreter.llm.api_base = "http://10.0.255.147:11434/v1"
interpreter.llm.max_tokens = 1000
interpreter.llm.context_window = 3000


interpreter.system_message += """
Run shell commands with -y so the user doesn't have to confirm them.
"""
print(interpreter.system_message)