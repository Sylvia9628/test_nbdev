# test_nbdev
> This is a project to test out nbdev


This file will become your README and also the index of your documentation.

## Install

`pip install test_nbdev`

## How to use

### Lemmatize

```python
documents =  ["Hello world", "NLP is fun", "We work at the bank"]
text = Preprocess(documents)
preprocessed = text.lemmatize()
```

```python
preprocessed
```




    [['hello', 'world'], ['NLP', 'fun'], ['-PRON-', 'work', 'bank']]



## Stemming

```python
documents =  ["Hello world", "NLP is fun", "We work at the bank"]
text = Preprocess(documents)
preprocessed = text.stemming()
```

```python
preprocessed
```




    [['hello', 'world'], ['nlp', 'fun'], ['we', 'work', 'bank']]


