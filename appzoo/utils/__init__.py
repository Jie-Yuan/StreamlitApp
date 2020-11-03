#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : StreamlitApp.
# @File         : __init__.py
# @Time         : 2020/11/3 1:46 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

import os

get_module_path = lambda path, file=__file__: os.path.normpath(os.path.join(os.getcwd(), os.path.dirname(file), path))
