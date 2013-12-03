from docker.zope.com:5000/centos5-min

run yum -y install \
  vixie-cron-4.1 \
  xinetd-2.3.14 \
  sbo-0.6.0 \
  subversion-1.6.11 \
  zaamdashboard-1.7.8 \
  zc.zopeorgkeyupload-0 \
  zeo-0.0.0 \
  viewvc-1.0.3 \
  file-4.17 \
  mailcap-2,1,23 \
  httpd-2.2.3 \
  openssh-server-4.3p2 \
  emacs-nox-21.4

add ./files /
add ./auth /

run /opt/cleanpython26/bin/python /setup.py

volume ["/data", "/home"]
expose 80 22 3690 2401
cmd ["/start.sh"]

