# Fine-tuning-with-QLoRA

## Finetuning with PEFT (Parameter Efficient Fine Tuning) Methods:

- Only updating a small subset of the model's parameters, rather than all parameters
- More efficient than training the whole model
- PEFT techniques: Prefix Tuning and LoRA
- Minimising the number of trainable parameters in a neural network
- More adaptable and memory-efficient

## Fine-tuning process with QLoRA

- The first section: follow the process of simple fine-tuning with the BERT uncased model in this link
- Set up the LoRA configuration as in `lora-config.py`
- Set up the bitsandbytes configuration for quantisation
