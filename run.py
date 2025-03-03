import subprocess
import time
import random

def mseive(number,timeout,core):
    try:
        command = ['msieve153.exe', '-t', str(core) ,'-v' ,'-e', '-q' ,str(number)]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        try:
            stdout, stderr = process.communicate(timeout=timeout)
            if process.returncode == 0:
                return stdout.decode().strip()
            else:
                return f"Error: {stderr.decode().strip()}"
        except subprocess.TimeoutExpired:
            process.kill()
            return "Timeout: The process took too long to complete."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def run(dig,t,timeout,core):
    print("Finding Start")
    print(f"Take up to {t*timeout}sec")
    for _ in range(t):
        i = random.randrange(10**(dig-1), 10**(dig))
        n = ((i*2)*(i*2))+1
        result = mseive(n,timeout,core)
        if len(result.split('\n')) == 2:
            print(f"Found N={i} {result.split('\n')[1]}")
    print("Finding Finish")
    
D = int(input("Digits:"))
T = int(input("Trials:"))
timeout = int(input("TimeOut(sec):"))
core = int(input("UseCores:"))
run(D,T,timeout,core)
