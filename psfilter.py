import sys
import psutil
import time
import shutil


# 以 KB/s 为单位
NETSPEED_THRESHOLD = 25000  # 25M Byte/s
# byte 
DISKSPACE_THRESHOLD = 102400000 # 100G


# 检查网络速度
def calc_network_speed():
    interval = 1
    t0 = time.time()
    upload0 = psutil.net_io_counters().bytes_sent
    download0 = psutil.net_io_counters().bytes_recv
    time.sleep(interval)

    t1 = time.time()
    upload1 = psutil.net_io_counters().bytes_sent
    download1 = psutil.net_io_counters().bytes_recv

    upload_speed = (upload1 - upload0) / (t1 - t0) / 1024
    download_speed = (download1 - download0) / (t1 - t0) / 1024

    return upload_speed, download_speed


def main():
    total, used, free = shutil.disk_usage(__file__)
    if free < DISKSPACE_THRESHOLD:
        print("not enough disk space")
        sys.exit(1)

    up_speed, down_speed = calc_network_speed()
    print(f"up speed {up_speed}")
    if  up_speed < NETSPEED_THRESHOLD:
#        print("return 0")
        sys.exit(0)
    else:
#        print("network busy")
        sys.exit(1)



if __name__ == "__main__":
    main()
