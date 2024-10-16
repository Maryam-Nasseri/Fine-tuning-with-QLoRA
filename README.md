# Fine-tuning-with-LoRA & QLoRA

This repository contains:
1. A brief overview of Parameter Efficient Fine Tuning (PEFT)
2. The process for fine-tuning/training with LoRA (Low-Rank Adaptation) and a link to a video tutorial
3. The process of fine-tuning with QLoRA  and a link to a video tutorial

## Finetuning with PEFT (Parameter Efficient Fine Tuning) Methods:

- Only updating a small subset of the model's parameters, rather than all parameters
- More efficient than training the whole model
- PEFT techniques: Prefix Tuning and LoRA
- Minimising the number of trainable parameters in a neural network
- More adaptable and memory-efficient
- Main methods: Prefix-Tuning, LoRA (Low-Rank Adaptation), QLoRA (Quantised LoRA)
-- LoRA:
  - allows small adapters to be tailored to specific datasets or users.
  - Less memory needed for loading and processing
  - Introduces new parameters only during the training

## Fine-tuning process with LoRA

1. The first section: follow the process of simple fine-tuning with the BERT uncased model in this link: [Fine-tuning LLMs Locally](https://github.com/Maryam-Nasseri/Fine-tuning-LLMs-Locally)
2. Main installs in `install_libraries.py`.
3. Set up the LoRA configuration as in `lora-config.py`
4. Set up the training arguments to pass to the Trainer method, as in `training_args.py`.
5. Set up the `Trainer` arguments as in `trainer.py`.
6. Train/fine-tune the model using `train()` on the Trainer object (e.g., my_trainer in the above file).
7. Save the model using `save_pretrained("name")` on the peft model.
8. Optional: merge the base model with the adapter using `merge_and_unload()`.
9. Below is the link to the video tutorial with LoRA:

[![Watch the video on fine-tuning LLMs with LoRA PEFT with code](https://img.youtube.com/vi/aj1V9_5nAfo/maxresdefault.jpg)](https://youtu.be/aj1V9_5nAfo) 

## Fine-tuning with QLoRA

- Follow the steps in the previous section (fine-tuning with LoRA) first; here we need to make the peft model in quantised versions. 
- Set up the bitsandbytes configuration for quantisation as in `bnb_config.py`.
- If needed, you can prepare the model's embedding layers for gradient updating after setting the bitsandbytes parameters.
- Instead of `Trainer()` method (as in full fine-tuning and fine-tuning with LoRA), use the `SFTTrainer()` method.

Below is the link to the tutorial of fine-tuning with QLoRA:

[![Watch the video on fine-tuning LLMs with QLoRA PEFT with code](https://img.youtube.com/vi/QzsjHUhZZLE/maxresdefault.jpg)](https://youtu.be/QzsjHUhZZLE) 

## Practical Considerations:
- For learning and practice purposes, start with a lightweight model which is faster to load and train, and move on to larger models only for performance.
- Before using any dataset on any model (LLM), be sure that the input data format of that dataset matches the model's data template; otherwise, you need to make a function to format the data. An example of an input/output format for the decoder models such as LLAMA2 is `example_format.png`.
