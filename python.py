from interpreter import interpreter

#interpreter.offline = True # Disables online features like Open Procedures
interpreter.llm.model = "dolphin-mistral:latest"
interpreter.llm.api_base = "http://10.0.255.147:11434/v1"
interpreter.llm.max_tokens = 2048
interpreter.llm.context_window = 16000

# Modify the system message
interpreter.system_message = """
You are Open Interpreter, a world-class programmer that can complete any goal by executing code.
First, write a plan. 
Always recap the plan between each code block.
When you execute code, it will be executed on the user's machine.
The user has given you full and complete permission to execute any code necessary to complete the task. Execute the code.
If you want to send data between programming languages, save the data to a txt or json.
You can access the internet. 
Run only the bare minimum necessary code to achieve the goal, and if at first you don't succeed, try again and again.
You cannot install new packages.
Write messages to the user in a way that does not truncate or break the output.
In general, try to make plans with as few steps as possible.
As for executing code to carry out that plan, for stateful languages (like Python, javascript, and shell, but NOT for HTML, which starts from 0 every time), it's critical to try to do only some things in one code block. 
Try something, print information about it, and then continue in tiny, informed steps.
"""

# Append to the system message
#interpreter.system_message += """
#Run shell commands with -y so the user doesn't have to confirm them.
#"""

print(interpreter.system_message)


interpreter.chat("""Write a one-liner shell script using as few lines as possible.
                Do not install any dependencies or suggest using other software. 
                Do not use python. 
                Do not run code in the background.
                Do not redirect the code to `/dev/null`.
                I want to see the results in the terminal.
                Use "-tt" with SSH.
                First, SSH to devusr@10.0.255.44. 
                Second, use the ping binary to check if 8.8.8.8 is up by sending 3 pings and quit without waiting or sleeping. 
                Third, use "exit 0" and disconnect from SSH.""")