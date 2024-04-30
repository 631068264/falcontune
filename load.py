#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os.path
import re

data_path = 'data/filter_cap.json'
tmp_dir = 'data'
d = {}
data_list = []



f_read = open(data_path)
with open(os.path.join(tmp_dir,'tmp.json'),'w') as f_write:
    lines = json.load(f_read)

    raw = lines['annotations'][:10]
    # for i, data in enumerate(lines):
    #     data_list.append({
    #         'image_id' : str(i),
    #         'caption' : data['label'],
    #     })

    d['annotations'] = raw
    f_write.write(json.dumps(d, ensure_ascii=False))
f_read.close()