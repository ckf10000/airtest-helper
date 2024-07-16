# -*- coding: utf-8 -*-
"""
# ---------------------------------------------------------------------------------------------------------
# ProjectName:  airtest-helper
# FileName:     log.py
# Description:  TODO
# Author:       mfkifhss2023
# CreateDate:   2024/07/15
# Copyright ©2011-2024. Hunan xxxxxxx Company limited. All rights reserved.
# ---------------------------------------------------------------------------------------------------------
"""
import logging

logger = logging.getLogger("root")


def reset_airtest_loglevel(loglevel: str = "error"):
    log = logging.getLogger("airtest")
    if loglevel == "debug":
        log.setLevel(logging.DEBUG)
    elif loglevel == "info":
        log.setLevel(logging.INFO)
    elif loglevel == "warning":
        log.setLevel(logging.WARNING)
    else:
        log.setLevel(logging.ERROR)
