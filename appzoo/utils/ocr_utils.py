#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : StreamlitApp.
# @File         : ocr_utils
# @Time         : 2020/11/3 1:45 下午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

from PIL import Image
from paddleocr import PaddleOCR, draw_ocr
from appzoo.utils import get_module_path


def ocr_result_image(result, input_image, output_image='output_image.png'):
    # https://raw.githubusercontent.com/PaddlePaddle/PaddleOCR/develop/doc/simfang.ttf
    image = Image.open(input_image).convert('RGB')
    boxes = [line[0] for line in result]
    txts = [line[1][0] for line in result]
    scores = [line[1][1] for line in result]
    im_show = draw_ocr(image, boxes, txts, scores, font_path=get_module_path("../data/simfang.ttf", __file__))
    im_show = Image.fromarray(im_show)
    im_show.save(output_image)
    return output_image
