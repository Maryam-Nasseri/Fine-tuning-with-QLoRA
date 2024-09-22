# Fine-tuning-with-LoRA & QLoRA

This repository contains:
1. A brief overview of Parameter Efficient Fine Tuning (PEFT)
2. The process for fine-tuning/training with LoRA (Low-Rank Adaptation) and a link to a video tutorial
3. The process of fine-tuning with QLoRA

## Finetuning with PEFT (Parameter Efficient Fine Tuning) Methods:

- Only updating a small subset of the model's parameters, rather than all parameters
- More efficient than training the whole model
- PEFT techniques: Prefix Tuning and LoRA
- Minimising the number of trainable parameters in a neural network
- More adaptable and memory-efficient
- Main methods: Prefix-Tuning, LoRA (Low-Rank Adaptation), QLoRA (Quantised LoRA)

## Fine-tuning process with LoRA

1. The first section: follow the process of simple fine-tuning with the BERT uncased model in this link: [Fine-tuning LLMs Locally](https://github.com/Maryam-Nasseri/Fine-tuning-LLMs-Locally)
2. Set up the LoRA configuration as in `lora-config.py`
3. Set up the training arguments to pass to the Trainer method, as in `training_args.py`.
4. Set up the `Trainer` arguments as in `trainer.py`.
5. Train/fine-tune the model using `train()` on the Trainer object (e.g., my_trainer in the above file).
6. Save the model using `save_pretrained("name")` on the peft model.
7. Optional: merge the base model with the adapter using `merge_and_unload()`.

## Fine-tuning with QLoRA

- Follow the previous steps, then
- Set up the bitsandbytes configuration for quantisation as in `bnb_config.py`.
- Instead of `Trainer()` method (as in full fine-tuning and fine-tuning with LoRA), use the `SFTTrainer()` method.
