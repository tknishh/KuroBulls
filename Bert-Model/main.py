# create flask app
import re
from flask import Flask, request, jsonify
import pandas as pd
import torch
import numpy as np
from transformers import BertTokenizer, BertModel
from torch import nn
from torch.optim import Adam
from tqdm import tqdm
import re
app = Flask(__name__)

#######################################
def preprocess_text(sen):
    sentence = remove_tags(sen)
    sentence = re.sub('[^a-zA-Z]', ' ', sentence)
    sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)
    sentence = re.sub(r'\s+', ' ', sentence)
    return sentence


TAG_RE = re.compile(r'<[^>]+>')
def remove_tags(text):
    return TAG_RE.sub('', text)


tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
labels = { 'spam':1, 'ham':0 }

class Dataset(torch.utils.data.Dataset):

    def __init__(self, df):
        self.labels = [labels[label] for label in df['Category']]
        self.texts = [tokenizer(text, 
                                padding='max_length', max_length = 512, truncation=True,
                                return_tensors="pt") for text in df['Message']]

    def classes(self):
        return self.labels

    def __len__(self):
        return len(self.labels)

    # Fetch a batch of labels
    def get_batch_labels(self, idx):
        return np.array(self.labels[idx])

    # Fetch a batch of inputs
    def get_batch_texts(self, idx):
        return self.texts[idx]

    def __getitem__(self, idx):
        batch_texts = self.get_batch_texts(idx)
        batch_y = self.get_batch_labels(idx)
        return batch_texts, batch_y


class BertClassifier(nn.Module):

    def __init__(self, dropout=0.2):
        super(BertClassifier, self).__init__()
        self.bert = BertModel.from_pretrained('bert-base-cased')
        self.dropout = nn.Dropout(dropout)
        self.linear = nn.Linear(768, 5)
        self.relu = nn.ReLU()

    def forward(self, input_id, mask):
        _, pooled_output = self.bert(input_ids= input_id, attention_mask=mask,return_dict=False)
        dropout_output = self.dropout(pooled_output)
        linear_output = self.linear(dropout_output)
        final_layer = self.relu(linear_output)
        return final_layer


#######################################



MODEL = BertClassifier()




# post end point to recieve a string
@app.route('/', methods=['POST'])
def post():
    print("a")
    try:
    # get the string from the post request
        data = request.get_json()
        # return the message back for empty string
        print(data)
        if data == None or data['data'] == '' :
            return jsonify({'data': 'Please enter a message'})
        data = data['data']
        print(data)
        data = operate(MODEL, data)
        print(data)
        data = {'data': str(data)}
        # print(data)
        return jsonify(data)
    except Exception as e:
        return(str(e))



def operate(MODEL, data):
    # print(type(data))
    my_data = {
    'Category' : ['ham'],
    'Message' : [data],
    'spam' : [0]
    }
    print(my_data)
    df = pd.DataFrame(my_data)
    test = Dataset(df)
    test_dataloader = torch.utils.data.DataLoader(test, batch_size=2)
    use_cuda = torch.cuda.is_available()
    device = torch.device("cuda" if use_cuda else "cpu")
    if use_cuda:
        MODEL = MODEL.cuda()
    with torch.no_grad():
        for test_input in test_dataloader:
            print("b")
            # print("test", test_input)
            mask = test_input[0]['attention_mask'].to(device)
            # print(type(mask))
            input_id = test_input[0]['input_ids'].squeeze(1).to(device)
            # print(input_id)
            output = MODEL(input_id, mask)
            # print(type(output))
            # print(output.shape)
            print(output.argmax(dim=1).item())
            return output.argmax(dim=1).item()
    # MODEL.predict(data)
    return None


if __name__ == '__main__':
    MODEL = BertClassifier()
    MODEL.load_state_dict(torch.load('./weights.pth'))
    MODEL.eval()
    print("listening on port 5000")
    app.run(debug=True, port=5000)
