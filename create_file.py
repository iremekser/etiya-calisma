from multiprocessing import Process
import subprocess


def toSSH():
    subprocess.Popen("ssh {user}@{host} {cmd}".format(user='demeter', host='192.168.1.192', cmd='touch /home/demeter/irem/new.txt'),
                     shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()


def toLocal():
    f = open("new.txt", "w+")


pSSH = Process(target=toSSH, args=())
pLocal = Process(target=toLocal, args=())

pSSH.start()
pLocal.start()

pSSH.join()
pLocal.join()
