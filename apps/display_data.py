#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : StreamlitApp.
# @File         : df_display
# @Time         : 2020/11/3 11:39 上午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 


import numpy as np
import pandas as pd

import streamlit as st

data = pd.DataFrame(np.random.randint(10, 10))

# Magic commands implicitly `st.write()`
''' _This_ is some __Markdown__ '''
a = 3
'dataframe:', data
