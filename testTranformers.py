# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 13:36:45 2022

@author: chonlatid.d
"""
#%%
from transformers import pipeline
classifier = pipeline('sentiment-analysis')
classifier('I not like it')

#%%
import requests
from PIL import Image
from transformers import pipeline
url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/coco_sample.png"
image_data = requests.get(url, stream=True).raw
image = Image.open(image_data)
object_detector = pipeline('object-detection')
object_detector(image)

#%%
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

inputs = tokenizer("Hello world!", return_tensors="pt")
outputs = model(**inputs)

#%%
from transformers import AutoTokenizer, TFAutoModel

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = TFAutoModel.from_pretrained("bert-base-uncased")

inputs = tokenizer("Hello world!", return_tensors="tf")
outputs = model(**inputs)

#%%
from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
generator("I have big dick", max_length=128, num_return_sequences=5)

#%%
from transformers import pipeline
question_answerer = pipeline("question-answering", model='distilbert-base-uncased-distilled-squad')

context = r"""
Sedimentary rocks are formed by the process of sedimentation. Layer after layer of minerals is deposited over a great span of time, 
resulting in the formation of a sedimentary rock. As a result, each layer is different if the conditions under which its deposits were different. 
Thus we can say that a sedimentary rock is a sort of museum, holding the records of all the time over which it was formed,
 which by all means can be as long as a billion years.
"""

result = question_answerer(question="A sedimentary rock gets its name from the fact that?",     context=context)
print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

#%%
from transformers import pipeline
unmasker = pipeline('fill-mask', model='bert-base-uncased')
unmasker("Space exploration is a very exciting [MASK] of research.")
