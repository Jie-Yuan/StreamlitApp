#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : StreamlitApp.
# @File         : ocr
# @Time         : 2020/11/3 12:31 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

import os
import streamlit as st

from paddleocr import PaddleOCR

from appzoo.utils.ocr_utils import *

from appzoo.utils.streamlit_utils import *

ocr = st.cache(persist=True)(PaddleOCR(use_angle_cls=True, lang="ch"))

# side
st.sidebar.markdown('**OCR SideBar**')
biz = st.sidebar.selectbox('输入方式', ('ImageUrl', 'ImageFile'), index=0)

if biz == 'ImageUrl':
    ImageUrl = st.text_input("ImageUrl",
                             "https://dgss2.bdstatic.com/5eR1dDebRNRTm2_p8IuM_a/her/static/indexnew/container/search/baidu-logo.ba9d667.png")
    input_image = 'image.png'
    # import wget
    # wget.download(ImageUrl, img_path)
    os.system(f"wget {ImageUrl} -O {input_image}")
    result = ocr.ocr(input_image, cls=True)
    output_image = ocr_result_image(result, input_image)
    st.image(output_image)


elif biz == 'ImageFile':
    input_image = file_uploader(st)
    if input_image:
        result = ocr.ocr(input_image, cls=True)
        output_image = ocr_result_image(result, input_image)

        st.image(output_image)
