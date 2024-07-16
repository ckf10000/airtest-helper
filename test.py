# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  airtest-helper
# FileName:     test.py
# Description:  TODO
# Author:       zhouhanlin
# CreateDate:   2024/07/16
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
from airtest_helper.log import logger
from airtest_helper.core import DeviceProxy, DeviceApi


def test_adb():
    phone = DeviceProxy(device="192.168.9.97", port=5555, cap_type='adb', enable_debug=True, enable_log=False,
                        loglevel="debug")
    # ph = Phone(device_id="S2D0219126003408", cap_type='adb', enable_debug=True, enable_log=True, loglevel="error")
    api = DeviceApi(device=phone)
    logger.info("\n{}\n".format(api.shell("ls")))
    # print(ph.start_app("abc"))
    # print(ph.stop_app("abc"))
    # print(ph.wake())
    # print(ph.home())
    # ph.hide_keyword()


if __name__ == '__main__':
    test_adb()
