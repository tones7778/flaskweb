import paramiko

print('ssh-mon-get-hostname is running')

mydevices = ['mon.home.lan']
mycommand = 'free -m'
myusername = ['root']
mypassword = ['xxxxxxxx']

try:
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(mydevices[0], username=myusername[0], password=mypassword[0])
except paramiko.SSHException:
    print("Connection Failed")
    quit()

stdin,stdout,stderr = ssh.exec_command(mycommand)
results = stdout.read()
print(results)
#for m in mycommand:
#    stdin,stdout,stderr = ssh.exec_command(m)
#    for line in stdout.readlines():
#        myresults =  line.strip()

ssh.close()
