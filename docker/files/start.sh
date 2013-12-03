#!/bin/bash
/etc/init.d/xinetd start
/etc/init.d/httpd start
/usr/sbin/sshd -D
