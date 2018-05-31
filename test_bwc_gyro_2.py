#!/usr/bin/python
"""
print pathname
print description

paramiko = imp.load_source('paramiko', fp, '/usr/local/lib/python2.7/dist-packages/paramiko/file.py')
 
"""
import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect("192.168.77.136", 22, "root", "pass")

time.strftime("%Y%m%d_%H%M%S", time.localtime())

f = open('gyrodata_%s.csv' % (time.strftime("%Y%m%d_%H%M%S", time.localtime())), 'w')

while True:
    #     stdin, stdout, stderr = ssh.exec_command("cat /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_accel_x_raw /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_accel_y_raw /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_accel_z_raw /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_accel_scale")
    #     x, y, z, s = stdout.readlines()
    # # print x, y, z

    #     print >> f, "Accel: %6f, %6f, %6f" % (float(x) * float(s), float(y) * float(s), float(z) * float(s))

    #     stdin, stdout, stderr = ssh.exec_command("cat /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_anglvel_x_raw /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_anglvel_y_raw /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_anglvel_z_raw /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_anglvel_scale")

    #     x, y, z, s = stdout.readlines()
    #     print >> f, "Angl: %6f, %6f, %6f" % (float(x) * float(s), float(y) * float(s), float(z) * float(s))

    stdin, stdout, stderr = ssh.exec_command("cat /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_accel_x_raw /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_accel_y_raw /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_accel_z_raw /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_accel_scale /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_anglvel_x_raw /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_anglvel_y_raw /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_anglvel_z_raw /sys/class/spi_master/spi0/spi0.0/iio\:device0/in_anglvel_scale")
    in_accel_x_raw, in_accel_y_raw, in_accel_z_raw, in_accel_scale, in_anglvel_x_raw, in_anglvel_y_raw, in_anglvel_z_raw, in_anglvel_scale = stdout.readlines()
    print >> f, "%s, %6f, %6f, %6f, %6f, %6f, %6f" % (time.strftime("%Y%m%d_%H%M%S", time.localtime()), float(in_accel_x_raw) * float(in_accel_scale), float(in_accel_y_raw) * float(in_accel_scale), float(in_accel_z_raw) * float(in_accel_scale), float(in_anglvel_x_raw) * float(in_anglvel_scale), float(in_anglvel_y_raw) * float(in_anglvel_scale), float(in_anglvel_z_raw) * float(in_anglvel_scale))


# print stdout.readlines()
ssh.close()
f.close()
