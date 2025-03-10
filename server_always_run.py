import os  
import subprocess  
import time  

print("Coded by Beny [Discord: BenyVK#0000 | Telegram: @i36vk]")  
print("")  

current_directory = os.getcwd()  
exe_path = os.path.join(current_directory, 'samp-server.exe')  
 
if not os.path.isfile(exe_path):  
    print("VK : I can't find any such file in the folder I'm in: samp-server.exe")  
else:  
    while True:   
        process = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)  
        output, _ = process.communicate()  
        
        if exe_path.split("\\")[-1] in output.decode():  
            time.sleep(1)  
        else:  
            print("[VK-SUCCESS] samp-server.exe Started!")  
            subprocess.Popen(['start', 'Votka Starter', exe_path], shell=True)  
            time.sleep(1)
