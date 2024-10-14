# Important libraries to work with for fine-tuning with the LoRA and QLoRA methods


pip install transformers==4.38.2   #transformers library for all models and configurations
pip install peft==0.4.0  #for the peft model and peft configuration
pip install trl==0.4.7
pip install accelerate==0.27.2
pip install pandas==2.1.4  #processing data
pip install torch==2.2.1   #Pytorch for deep learning


# Additional useful libraries for the fine-tuning process          
pip install datasets==2.20.0
pip install keras==2.16.0  #training/evaluation datasets
pip install einops  #for working with tensors
pip install numpy==1.26.4
pip install evaluate==0.4.2   #training evaluation

# for pulling models and pushing fine-tuned models
pip install --upgrade huggingface_hub==0.23.4
