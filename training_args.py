# important training argument here; check out there is a ton of them in HUgging Face Trainer() 
training_args = TrainingArguments(
    output_dir='final',               # name of output folder/directory
    overwrite_output_dir = True,      # set to True if you want to incrementally train and test the model
    evaluation_strategy="epoch",      # evaluation in steps or epochs
    num_train_epochs=1,               # how many times to go through the whole training dataset 
)

# additional arguments to set:
#weight_decay=0.01,
#adam_beta1=0.9,
#adam_beta2=0.999,
#fp16 = False,
#bf16 = False, 
