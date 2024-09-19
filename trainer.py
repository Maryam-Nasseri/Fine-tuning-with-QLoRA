my_trainer = Trainer (
  model=model,
  args=training_args,
  train_dataset=tokenised_train,
  eval_dataset=tokenised_eval
)
