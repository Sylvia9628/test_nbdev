# test_nbdev
> This is a project to test out nbdev


This file will become your README and also the index of your documentation.

## Install

`pip install testnbdev`

## How to use

### Lemmatize

```
documents =  ["Hello world", "NLP is fun", "We work at the bank"]
text = Preprocess(documents)
preprocessed = text.lemmatize()
```

```
preprocessed
```




    [['hello', 'world'], ['NLP', 'fun'], ['-PRON-', 'work', 'bank']]


