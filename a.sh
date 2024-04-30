export WANDB_DISABLED=true
export CUDA_VISIBLE_DEVICES=1


falcontune finetune \
    --model=falcon-7b \
    --weights=tiiuae/falcon-7b \
    --dataset=/data/home/yaokj5/dl/dataset/falcon \
    --data_type=alpaca \
    --lora_out_dir=./falcon-7b-big-alpaca/ \
    --mbatch_size=1 \
    --batch_size=2 \
    --epochs=3 \
    --lr=3e-4 \
    --cutoff_len=256 \
    --lora_r=8 \
    --lora_alpha=16 \
    --lora_dropout=0.05 \
    --warmup_steps=5 \
    --save_steps=50 \
    --save_total_limit=3 \
    --logging_steps=5 \
    --target_modules='["query_key_value"]'


falcontune finetune \
    --model=falcon-7b \
    --weights=tiiuae/falcon-7b \
    --dataset=/data/home/yaokj5/dl/dataset/multiturn \
    --data_type=multiturn \
    --lora_out_dir=./falcon-7b-multiturn/ \
    --mbatch_size=2 \
    --batch_size=4 \
    --epochs=3 \
    --lr=2e-2 \
    --cutoff_len=256 \
    --lora_r=8 \
    --lora_alpha=16 \
    --lora_dropout=0.05 \
    --warmup_steps=5 \
    --save_steps=50 \
    --save_total_limit=3 \
    --logging_steps=5 \
    --target_modules='["query_key_value"]'

falcontune generate \
    --interactive \
    --model falcon-7b \
    --weights tiiuae/falcon-7b \
    --lora_apply_dir falcon-7b-alpaca \
    --max_new_tokens 500 \
    --use_cache \
    --do_sample \
    --instruction "列出人工智能的五个可能应用"

falcontune generate \
    --interactive \
    --model falcon-7b \
    --weights tiiuae/falcon-7b \
    --lora_apply_dir falcon-7b-alpaca \
    --max_new_tokens 500 \
    --use_cache \
    --do_sample \
    --prompt "番茄炒蛋的配料"