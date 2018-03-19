# -*- coding:utf-8 -*-
import paramiko

# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='192.168.77.221', port=22,
            username='root', password='pass')

# 执行命令
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

print '*' * 50
print in_accel_x
print in_accel_y
print in_accel_z
print '*' * 50

in_accel = (in_accel_x ** 2 + in_accel_y ** 2 + in_accel_z ** 2) ** 0.5

print in_accel
print '*' * 50

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

print in_anglvel_x
print in_anglvel_y
print in_anglvel_z
print '*' * 50

stdin, stdout, stderr = ssh.exec_command(
    'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_temp_scale')
in_temp_scale = float(stdout.read())
stdin, stdout, stderr = ssh.exec_command(
    'cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_temp_raw')
in_temp_raw = float(stdout.read())

in_temp = in_temp_scale * in_temp_raw

print in_temp
print '*' * 50

stdin, stdout, stderr = ssh.exec_command('/tmp/test_gyro.sh')
result = stdout.read()
print result
print '*' * 50


# 获取命令结果
# result = stdout.read()
# 关闭连接
ssh.close()


# chipinfo=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/chipinfo)
# current_timestamp_clock=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/current_timestamp_clock)
# dev=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/dev)
# in_accel_matrix=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_accel_matrix)
# in_accel_mount_matrix=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_accel_mount_matrix)
# in_accel_scale=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_accel_scale)
# in_accel_scale_available=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_accel_scale_available)
# in_accel_x_calibbias=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_accel_x_calibbias)
# in_accel_x_raw=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_accel_x_raw)
# in_accel_y_calibbias=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_accel_y_calibbias)
# in_accel_y_raw=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_accel_y_raw)
# in_accel_z_calibbias=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_accel_z_calibbias)
# in_accel_z_raw=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_accel_z_raw)
# in_anglvel_mount_matrix=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_anglvel_mount_matrix)
# in_anglvel_scale=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_anglvel_scale)
# in_anglvel_scale_available=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_anglvel_scale_available)
# in_anglvel_x_calibbias=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_anglvel_x_calibbias)
# in_anglvel_x_raw=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_anglvel_x_raw)
# in_anglvel_y_calibbias=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_anglvel_y_calibbias)
# in_anglvel_y_raw=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_anglvel_y_raw)
# in_anglvel_z_calibbias=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_anglvel_z_calibbias)
# in_anglvel_z_raw=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_anglvel_z_raw)
# in_gyro_matrix=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_gyro_matrix)
# in_temp_offset=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_temp_offset)
# in_temp_raw=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_temp_raw)
# in_temp_scale=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/in_temp_scale)
# name=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/name)
# sampling_frequency=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/sampling_frequency)
# sampling_frequency_available=$(cat /sys/devices/platform/e0000000.ahb/e0020000.spi/spi_master/spi0/spi0.0/iio:device0/sampling_frequency_available)
