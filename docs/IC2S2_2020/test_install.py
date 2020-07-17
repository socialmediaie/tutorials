# coding: utf-8

from pathlib import Path
from allennlp.nn.util import move_to_device
import torch
import pandas as pd

from SocialMediaIE.data.tokenization import get_match_iter, get_match_object
from SocialMediaIE.predictor.model_predictor import run, get_args, PREFIX, get_model_output, output_to_df


# Tagging model
SERIALIZATION_DIR = Path("./SocialMediaIE/data/models/all_multitask_stacked_l2_0_lr_1e-3_no_neel/")
args = get_args(PREFIX, SERIALIZATION_DIR)
args = args._replace(dataset_paths_file = "./SocialMediaIE/experiments/all_dataset_paths.json", cuda=False)
TASKS, vocab, model, readers, test_iterator = run(args)

def tokenize(text):
    objects = [get_match_object(match) for match in get_match_iter(text)]
    n = len(objects)
    cleaned_objects = []
    for i, obj in enumerate(objects):
        obj["no_space"] = True
        if obj["type"] == "space":
            continue
        if i < n-1 and objects[i+1]["type"] == "space":
            obj["no_space"] = False
        cleaned_objects.append(obj)
    keys = cleaned_objects[0].keys()
    final_sequences = {}
    for k in keys:
        final_sequences[k] = [obj[k] for obj in cleaned_objects]
    return final_sequences

def predict_df(texts=None):
    # Empty cache to ensure larger batch can be loaded for testing
    if texts:
        data = [tokenize(text) for text in texts]
    else:
        text = "Barack Obama went to Paris and never returned to the USA."
        text1 = "Stan Lee was a legend who developed Spiderman and the Avengers movie series."
        text2 = "I just learned about donald drumph through john oliver. #JohnOliverShow such an awesome show."
        texts = [text, text1, text2]
        data = [tokenize(text) for text in texts]
    torch.cuda.empty_cache()
    tokens = [obj["value"] for obj in data]
    output = list(get_model_output(model, tokens, args, readers, vocab, test_iterator))
    idx = 0
    def _get_data_values(d):
      return {
        k: d[k]
        for k in d.keys()
        if k != "value"
    }
    #df = output_to_df(tokens[idx], output[idx], vocab)
    df = pd.concat([
                    output_to_df(tokens[i], output[i], vocab).assign(**_get_data_values(d)).assign(data_idx=i)
                    for i, d in enumerate(data)
          ])

    # for k in data[idx].keys():
    #     if k != "value":
    #         df[k] = data[idx][k]
    return df

print(predict_df())
texts = [
    "Beautiful day in Chicago! Nice to get away from the Florida heat.",
    "Barack obama went to New York.",
    "obama went to Paris.",
    "Facebook is a new company.",
    "New york is better than SFO",
    "Urbana Champaign is the best",
    "urbana champaign is the best place to live and study",
    "going to Ibiza"
]
df = predict_df(texts)
print(df)
print(df[df.data_idx == 7])

# Classification models
from SocialMediaIE.predictor.model_predictor_classification import run, get_args, PREFIX, get_model_output, output_to_json

SERIALIZATION_DIR = Path("./SocialMediaIE/data/models_classification/all_multitask_shared_bilstm_l2_0_lr_1e-3/")
args = get_args(PREFIX, SERIALIZATION_DIR)
args = args._replace(dataset_paths_file = "./SocialMediaIE/experiments/all_classification_dataset_paths.json", cuda=False)
TASKS, vocab, model, readers, test_iterator = run(args)

def tokenize(text):
    objects = [get_match_object(match) for match in get_match_iter(text)]
    n = len(objects)
    cleaned_objects = []
    for i, obj in enumerate(objects):
        obj["no_space"] = True
        if obj["type"] == "space":
            continue
        if i < n-1 and objects[i+1]["type"] == "space":
            obj["no_space"] = False
        cleaned_objects.append(obj)
    keys = cleaned_objects[0].keys()
    final_sequences = {}
    for k in keys:
        final_sequences[k] = [obj[k] for obj in cleaned_objects]
    return final_sequences

def predict_json(texts=None):
    # Empty cache to ensure larger batch can be loaded for testing
    if texts:
        data = [tokenize(text) for text in texts]
    else:
        text = "Barack Obama went to Paris and never returned to the USA."
        text1 = "Stan Lee was a legend who developed Spiderman and the Avengers movie series."
        text2 = "I just learned about donald drumph through john oliver. #JohnOliverShow such an awesome show."
        texts = [text, text1, text2]
        data = [tokenize(text) for text in texts]
    torch.cuda.empty_cache()
    tokens = [obj["value"] for obj in data]
    output = list(get_model_output(model, tokens, args, readers, vocab, test_iterator))

    output_json = [
                   dict(text=text, doc_idx=i, **output_to_json(tokens[i], output[i], vocab))
                   for i, text in enumerate(texts)
                   ]
    return output_json

output_json = predict_json()
print(output_json[0])
