import subprocess

r = subprocess.run(['ls', '-al'])
print(r.returncode)

subprocess.run(['ls', '-al'], check=True)
# subprocess.run(['ls', '-al'], shell=True)  shell injection
