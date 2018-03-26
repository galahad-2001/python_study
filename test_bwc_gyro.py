# -*- coding:utf-8 -*-
import paramiko


# 执行命令
def buffer():
    stdin, stdout, stderr = ssh.exec_command(
        'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/buffer/enable')
    buffer_enable = stdout.read().strip()
    stdin, stdout, stderr = ssh.exec_command(
        'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/buffer/length')
    buffer_length = stdout.read().strip()
    stdin, stdout, stderr = ssh.exec_command(
        'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/buffer/watermark')
    buffer_watermark = stdout.read().strip()

    print '*' * 50
    print "buffer_enable = " + buffer_enable
    print "buffer_length = " + buffer_length
    print "buffer_watermark = " + buffer_watermark


def chipinfo():
    stdin, stdout, stderr = ssh.exec_command(
        'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/chipinfo')
    chipinfo = stdout.read().strip()

    print '*' * 50
    print "chipinfo = " + chipinfo


def in_accel():
    stdin, stdout, stderr = ssh.exec_command(
        'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/chipinfo')
    chipinfo = stdout.read()
    stdin, stdout, stderr = ssh.exec_command(
        'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_accel_scale')
    in_accel_scale = float(stdout.read())
    stdin, stdout, stderr = ssh.exec_command(
        'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_accel_x_raw')
    in_accel_x_raw = float(stdout.read())
    stdin, stdout, stderr = ssh.exec_command(
        'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_accel_y_raw')
    in_accel_y_raw = float(stdout.read())
    stdin, stdout, stderr = ssh.exec_command(
        'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_accel_z_raw')
    in_accel_z_raw = float(stdout.read())

    in_accel_x = in_accel_scale * in_accel_x_raw
    in_accel_y = in_accel_scale * in_accel_y_raw
    in_accel_z = in_accel_scale * in_accel_z_raw
    in_accel = (in_accel_x ** 2 + in_accel_y ** 2 + in_accel_z ** 2) ** 0.5

    print '*' * 50
    print "in_accel_scale = " + str(in_accel_scale)
    print "in_accel_x_raw = " + str(in_accel_x_raw)
    print "in_accel_y_raw = " + str(in_accel_y_raw)
    print "in_accel_z_raw = " + str(in_accel_z_raw)
    print "in_accel_x = " + str(in_accel_x)
    print "in_accel_y = " + str(in_accel_y)
    print "in_accel_z = " + str(in_accel_z)
    print "in_accel = " + str(in_accel)


def in_anglvel():
    stdin, stdout, stderr = ssh.exec_command(
        'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_anglvel_scale')
    in_anglvel_scale = float(stdout.read())
    stdin, stdout, stderr = ssh.exec_command(
        'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_anglvel_x_raw')
    in_anglvel_x_raw = float(stdout.read())
    stdin, stdout, stderr = ssh.exec_command(
        'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_anglvel_y_raw')
    in_anglvel_y_raw = float(stdout.read())
    stdin, stdout, stderr = ssh.exec_command(
        'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_anglvel_z_raw')
    in_anglvel_z_raw = float(stdout.read())

    in_anglvel_x = in_anglvel_scale * in_anglvel_x_raw
    in_anglvel_y = in_anglvel_scale * in_anglvel_y_raw
    in_anglvel_z = in_anglvel_scale * in_anglvel_z_raw

    print '*' * 50
    print "in_anglvel_scale = " + str(in_anglvel_scale)
    print "in_anglvel_x_raw = " + str(in_anglvel_x_raw)
    print "in_anglvel_y_raw = " + str(in_anglvel_y_raw)
    print "in_anglvel_z_raw = " + str(in_anglvel_z_raw)
    print "in_anglvel_x = " + str(in_anglvel_x)
    print "in_anglvel_y = " + str(in_anglvel_y)
    print "in_anglvel_z = " + str(in_anglvel_z)


def in_temp():
    stdin, stdout, stderr = ssh.exec_command(
        'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_temp_scale')
    in_temp_scale = float(stdout.read())
    stdin, stdout, stderr = ssh.exec_command(
        'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_temp_raw')
    in_temp_raw = float(stdout.read())

    in_temp = in_temp_scale * in_temp_raw

    print '*' * 50
    print "in_temp_scale = " + str(in_temp_scale)
    print "in_temp_raw = " + str(in_temp_raw)
    print "in_temp = " + str(in_temp)


if __name__ == "__main__":
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname='192.168.77.221', port=22,
                username='root', password='pass')

    buffer()
    chipinfo()
    in_accel()
    in_anglvel()
    in_temp()


    ssh.close()
