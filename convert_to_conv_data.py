#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import json
import datetime
import os
import re

'''
orig_data: {"instruction": "题目：小明买了一支钢笔，花费了5元，又买了一本书，花费8元，现在他手里还有10元钱，他手上原来有多少钱？", "input": "", "output": "\n令小明手上原来有的钱为X元。根据题目描述，得出以下方程式：\nX - 5 - 8 = 10\n化简可得：\nX = 23\n因此，小明手上原来有23元钱。"}
convert: {
    "id": xxx,
    "conversations":[
        {"from": "human", "value": "题目：小明买了一支钢笔，花费了5元，又买了一本书，花费8元，现在他手里还有10元钱，他手上原来有多少钱？"},
        {"from": "assistant", "value": "\n令小明手上原来有的钱为X元。根据题目描述，得出以下方程式：\nX - 5 - 8 = 10\n化简可得：\nX = 23\n因此，小明手上原来有23元钱。"},
    ]
}
'''


def belle(f_read, f_write, dataset_name):
    lines = f_read.readlines()
    num_id = 1
    for line in lines:
        data = json.loads(line)
        conversations = [{"from": "human", "value": data['instruction'] + data['input']},
                         {"from": "assistant", "value": data['output']}]
        # conversations = [{"from": "human", "value": data['input']},{"from": "assistant", "value": data['target']}]
        uniq_id = data['id'] if "id" in data else dataset_name + "-" + str(num_id)
        item = {"id": uniq_id, "conversations": conversations}
        f_write.write(json.dumps(item, ensure_ascii=False) + "\n")
        num_id += 1


def alpaca(f_read, f_write, dataset_name):
    lines = json.load(f_read)
    num_id = 1
    for data in lines:
        # data = json.loads(line)
        conversations = [{"from": "human", "value": data['instruction'] + data['input']},
                         {"from": "assistant", "value": data['output']}]
        # conversations = [{"from": "human", "value": data['input']},{"from": "assistant", "value": data['target']}]
        uniq_id = data['id'] if "id" in data else dataset_name + "-" + str(num_id)
        item = {"id": uniq_id, "conversations": conversations}
        f_write.write(json.dumps(item, ensure_ascii=False) + "\n")
        num_id += 1


def baize(f_read, f_write, dataset_name):
    lines = json.load(f_read)
    num_id = 1
    for data in lines:
        inputs = data['input'].split('\n')
        conversations = []
        for conversation in inputs:
            matched = re.search(r'\[\|(.*?)\|\] (.*)', conversation, re.I)
            if not matched:
                continue
            data = {"from": matched.group(1).lower() if matched.group(1).lower() == 'human' else 'assistant',
                    "value": matched.group(2)}
            conversations.append(data)
        uniq_id = data['id'] if "id" in data else dataset_name + "-" + str(num_id)
        item = {"id": uniq_id, "conversations": conversations}
        f_write.write(json.dumps(item, ensure_ascii=False) + "\n")
        num_id += 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--orig_data",
    )
    parser.add_argument(
        "--write_data",
    )
    parser.add_argument(
        "--dataset_name",
    )
    args = parser.parse_args()
    f_write = open(args.write_data, "w")
    with open(args.orig_data) as f:
        if args.dataset_name == 'belle':
            belle(f, f_write, args.dataset_name)
        elif args.dataset_name == 'alpaca':
            alpaca(f, f_write, args.dataset_name)
        elif args.dataset_name == 'baize':
            baize(f, f_write, args.dataset_name)
    f_write.close()


if __name__ == "__main__":
    main()
