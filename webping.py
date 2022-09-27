import subprocess
import pyfiglet 
text = pyfiglet.figlet_format("Web  Ping")
print(text)

print("Enter Website Name")
i = input()

subprocess.call("ping "+i ,shell=True)
