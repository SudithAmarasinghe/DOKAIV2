# https://replicate.com/lucataco/deepseek-vl-7b-base
# read more on API call of deepseek-vl from replicate

import os
import replicate



def get_description(image):
    input = {
        "image": image,
        "prompt": "Give a description of the given chart"
    }
    output = replicate.run(
        "lucataco/deepseek-vl-7b-base:d1823e6f68cd3d57f2d315b9357dfa85f53817120ae0de8d2b95fbc8e93a1385",
        input=input
    )
    return "".join(output)

def get_title(image):
    input = {
        "image": image,
        "prompt": "Give the title of the given chart"
    }
    output = replicate.run(
        "lucataco/deepseek-vl-7b-base:d1823e6f68cd3d57f2d315b9357dfa85f53817120ae0de8d2b95fbc8e93a1385",
        input=input
    )
    return "".join(output)

def get_summ(image):
    input = {
        "image": image,
        "prompt": "Give a summery of the given table"
    }
    output = replicate.run(
        "lucataco/deepseek-vl-7b-base:d1823e6f68cd3d57f2d315b9357dfa85f53817120ae0de8d2b95fbc8e93a1385",
        input=input
    )
    return "".join(output)

def get_text(image):
    input = {
        "image": image,
        "prompt": "Give the text of the given image of text"
    }
    output = replicate.run(
        "lucataco/deepseek-vl-7b-base:d1823e6f68cd3d57f2d315b9357dfa85f53817120ae0de8d2b95fbc8e93a1385",
        input=input
    )
    return "".join(output)

def img_des(image):
    input = {
        "image": image,
        "prompt": "Give a description of the given image"
    }
    output = replicate.run(
        "lucataco/deepseek-vl-7b-base:d1823e6f68cd3d57f2d315b9357dfa85f53817120ae0de8d2b95fbc8e93a1385",
        input=input
    )
    return "".join(output)