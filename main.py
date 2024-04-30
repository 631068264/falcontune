#!/usr/bin/env python
# -*- coding: utf-8 -*-
from transformers import AutoTokenizer, AutoModelForCausalLM
import transformers
import torch
import time

model = "/data/home/yaokj5/dl/models/falcon-40b"
text = "你好,介绍一下你自己"



tokenizer = AutoTokenizer.from_pretrained(model)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)


start_time = time.time()
print(start_time)
sequences = pipeline(
    text,
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    pad_token_id=tokenizer.eos_token_id,
)


end_time = time.time()
print(end_time)

for seq in sequences:
    print(f"Result: {seq['generated_text']}")


print(end_time - start_time)