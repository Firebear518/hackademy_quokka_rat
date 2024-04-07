import subprocess

output = subprocess.run('ls', shell=True, stdout=subprocess.PIPE, text=True)

print(output.stdout)