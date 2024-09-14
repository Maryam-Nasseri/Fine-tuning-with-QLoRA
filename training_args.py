# important training argument here; check out there is a ton of them in HUgging Face Trainer() 
training_args = TrainingArguments(
    output_dir='final',               # name of output folder/directory
    overwrite_output_dir = True,      # set to True if you want to incrementally train and test the model
    evaluation_strategy="epoch",
    num_train_epochs=1,
)
