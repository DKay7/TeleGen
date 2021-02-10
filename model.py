import torch
import logging
from config import pre_trained_path
from transformers import AutoTokenizer, GPT2LMHeadModel


class Model:
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        logging.getLogger().setLevel(logging.INFO)
        logging.log(logging.INFO, f'Computing on: {self.device}')

        self.tokenizer = AutoTokenizer.from_pretrained("sberbank-ai/rugpt3small_based_on_gpt2")
        # self.tokenizer.pad_token = self.tokenizer.eos_token
        self.model = GPT2LMHeadModel.from_pretrained("sberbank-ai/rugpt3small_based_on_gpt2")

        self.model.load_state_dict(torch.load(pre_trained_path))
        self.model.to(self.device).eval()

    def generate(self, initital_text):
        result = self.model.generate(
            input_ids=self.tokenizer(initital_text, return_tensors='pt').input_ids.to(self.device),
            attention_mask=self.tokenizer(initital_text, return_tensors='pt').attention_mask.to(self.device),
            num_beams=8,
            top_p=16,
            top_k=16,
            min_length=100,
            max_length=128,
            no_repeat_ngram_size=2)

        return self.tokenizer.decode(result[0], skip_special_tokens=True)
