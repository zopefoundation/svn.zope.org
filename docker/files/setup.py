
import os

def c(command):
    print command
    if os.system(command):
        raise SystemError("command failed", command)

os.mkdir('/var/run/sshd')
c("/etc/init.d/sshd start")

c("sbo zc.zopeorgkeyupload svn")
c("sbo zeo zaam")
c("sbo zaamdashboard zope")
c("rm -rf /home")
c("ln -s /data/svn /svn")
c("ln -s /data/cvs-repository /cvs-repository")
