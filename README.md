# Fine-tuning-with-QLoRA

## Finetuning with PEFT (Parameter Efficient Fine Tuning) Methods:

- Only updating a small subset of the model's parameters, rather than all parameters
- More efficient than training the whole model
- PEFT techniques: Prefix Tuning and LoRA
- Minimising the number of trainable parameters in a neural network
- More adaptable and memory-efficient

## Fine-tuning process with LoRA

- The first section: follow the process of simple fine-tuning with the BERT uncased model in this link: [Fine-tuning LLMs Locally](https://github.com/Maryam-Nasseri/Fine-tuning-LLMs-Locally)
- Set up the LoRA configuration as in `lora-config.py`
- Set up the training arguments to pass to the SFTTrainer method, as in `training_args.py`

## Fine-tuning with QLoRA

- Follow the previous steps, then
- Set up the bitsandbytes configuration for quantisation as in `bnb_config.py`.
