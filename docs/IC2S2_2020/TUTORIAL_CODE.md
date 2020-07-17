## Get entities and chunks


```
def split_tag(tag):
    return tuple(tag.split("-", 1)) if tag != "O" else (tag, None) 
    
def extract_entities(tags):
    tags = list(tags)
    curr_entity = []
    entities = []
    for i,tag in enumerate(tags + ["O"]):
        # Add dummy tag in end to ensure the last entity is added to entities
        boundary, label = split_tag(tag)
        if curr_entity:
            # Exit entity
            if boundary in {"B", "O"} or label != curr_entity[-1][1]:
                start = i - len(curr_entity)
                end = i
                entity_label = curr_entity[-1][1]
                entities.append((entity_label, start, end))
                curr_entity = []
            elif boundary == "I":
                curr_entity.append((boundary, label))
        if boundary == "B":
            # Enter or inside entity
            assert not curr_entity, f"Entity should be empty. Found: {curr_entity}"
            curr_entity.append((boundary, label))
    return entities


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


def predict_json(text=None):
    # Empty cache to ensure larger batch can be loaded for testing
    if text:
      data = [tokenize(text)]
    else:
        text = "Barack Obama went to Paris and never returned to the USA."
        text1 = "Stan Lee was a legend who developed Spiderman and the Avengers movie series."
        text2 = "I just learned about donald drumph through john oliver. #JohnOliverShow such an awesome show."
        data = [text, text1, text2]
        data = [tokenize(text) for text in data]
    torch.cuda.empty_cache()
    tokens = [obj["value"] for obj in data]
    output = list(get_model_output(model, tokens, args, readers, vocab, test_iterator))
    idx = 0
    df = output_to_df(tokens[idx], output[idx], vocab)
    for k in data[idx].keys():
        if k != "value":
            df[k] = data[idx][k]
    #df = df.set_index("tokens")
    output_json = df.to_json(orient='table')
    return output_json
    
```


