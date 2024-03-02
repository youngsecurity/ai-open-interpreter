from interpreter import interpreter

interpreter.offline = True # Disables online features like Open Procedures
interpreter.llm.model = "dolphin-mistral:latest"
interpreter.llm.api_base = "http://10.0.255.147:11434/v1"
interpreter.llm.max_tokens = 1000
interpreter.llm.context_window = 3000

#interpreter.chat() # Executes a single command

#interpreter.chat("""ssh devusr@10.0.255.44 'ping -c3 8.8.8.8; exit 0'""")

interpreter.chat("%verbose true")
interpreter.chat("""Write a bash script using as few lines as possible.
                Do not install any dependencies or suggest using other software. 
                Do not use python. 
                Do not run code in the background.
                Do not redirect the code to `/dev/null`.
                I want to see the results in the terminal.
                Use "-tt" with SSH.
                First, SSH to devusr@10.0.255.44. 
                Second, use the ping binary to check if 8.8.8.8 is up by sending 3 pings and quit without waiting or sleeping. 
                Third, use "exit 0" and disconnect from SSH.""")