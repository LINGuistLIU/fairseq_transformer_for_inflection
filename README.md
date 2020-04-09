How to use the Transformer model from Fairseq for morphological inflection.

## Dependencies

## Preprocess

```
$ ./preprocess.sh 3LETTER-LANGUAGE-CODE
```

```
$ ./preprocess.sh eng
```

## Train

```
$ ./preprocess.sh 3LETTER-LANGUAGE-CODE
```

```
$ ./train.sh eng
```

## Generate and Evaluate

```
$ ./generate_eval.sh 3LETTER-LANGUAGE-CODE TYPE
```

TYPE can be either *dev* or *test*. It specifies the type of data you want to predict.

For example, to make predictions for the English dev set, use the following command line:

```
$ ./generate_eval.sh eng dev
```
