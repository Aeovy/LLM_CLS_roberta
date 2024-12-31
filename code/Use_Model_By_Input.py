from Use_model_Functions import load_model,encoding,tokenizer,custom_mapping_function
from transformers import BertTokenizer
import torch
def predict(text,model,tokenizer = tokenizer):
    result=None
    with torch.no_grad():
        input_ids, attention_mask = encoding(text, tokenizer)
        result = model(input_ids, attention_mask)
        result=result.item()
        #result=custom_mapping_function(result)
    return result
if __name__ == '__main__':
    model=load_model('robertaLargeBiLSTMTextCNN2DCNN')
    tokenizer = tokenizer
    while True:
        text = input("Please enter the sentence you want to detect (or type 'False' to exit): ")
        if text.lower() == 'false':
            break
        result = predict(text, model,tokenizer)
        print('The probability of the sentence being AI-generated is:', result)