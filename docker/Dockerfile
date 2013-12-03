from docker.zope.com:5000/centos5-min

run yum -y install \
  vixie-cron-4.1 \
  xinetd-2.3.14 \
  sbo-0.6.0 \
  subversion-1.6.11 \
  zaamdashboard-1.7.8 \
  zc.zopeorgkeyupload-0 \
  zeo-0.0.0 \
  httpd-2.0.52 \
  openssh-server-4.3p2

add ./files /
add ./auth /

run /opt/cleanpython26/bin/python /setup.py

volume ["/data", "/home"]
expose 80 22 3690 2401

