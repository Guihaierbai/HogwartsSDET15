'''
声明一个fixture
'''
import os
import signal
import subprocess

import pytest


# 如果要每条用例单独录屏则将scope改成method级别
@pytest.fixture(scope="module", autouse=True)
def record_vedio():
    # 在命令行中执行命令,开启scrcpy进行录屏
    command = "scrcpy --record tmp.mp4"
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p)
    # 结束后根据pid找到程序，发送ctrl+c
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)
