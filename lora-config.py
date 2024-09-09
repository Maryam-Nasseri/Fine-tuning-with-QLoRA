# PEFT (QLoRA) important parameters:

peft_config = LoraConfig(
    lora_r = 64,
    lora_alpha=16,
    lora_dropout=0.01,
    bias="none",
    task_type="CAUSAL_LM",
)
