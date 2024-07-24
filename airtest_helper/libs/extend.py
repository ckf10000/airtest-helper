# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  airtest-helper
# FileName:     extend.py
# Description:  TODO
# Author:       zhouhanlin
# CreateDate:   2024/07/24
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import traceback
from time import sleep
from poco.proxy import UIObjectProxy
from airtest_helper.log import logger
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


def get_poco_factory(poco: AndroidUiautomationPoco, options: dict, loop: int, peroid: float = 0.5,
                     **kwargs) -> UIObjectProxy:
    poco_proxy = None
    is_ignore = kwargs.get("is_ignore", True)
    is_log_output = kwargs.get("is_log_output", True)
    is_log_traceback = kwargs.get("is_log_traceback", False)
    kwargs = dict()
    if options.get("type") or options.get("d_type"):
        kwargs["type"] = options.get("type") or options.get("d_type")
    if options.get("name"):
        kwargs["name"] = options.get("name")
    if options.get("text"):
        kwargs["text"] = options.get("text")
    if options.get("desc"):
        kwargs["desc"] = options.get("desc")
    if options.get("typeMatches"):
        kwargs["typeMatches"] = options.get("typeMatches")
    if options.get("nameMatches"):
        kwargs["nameMatches"] = options.get("nameMatches")
    if options.get("textMatches"):
        kwargs["textMatches"] = options.get("textMatches")
    for i in range(loop):
        try:
            # 根据实际情况定位按钮元素
            poco_proxy = poco(**kwargs)
            if poco_proxy.exists():
                return poco_proxy
        except Exception as e:
            if is_log_traceback is True:
                traceback.print_exc()
            err_str = "第{}次尝试查找，通过条件：{}，获取pocoUI控件元素失败，原因：{}".format(i + 1, options, e)
            if is_log_output is True:
                logger.error(err_str)
            if is_ignore is False:
                raise OverflowError(err_str)
        if peroid > 0:
            sleep(peroid)
    return poco_proxy
