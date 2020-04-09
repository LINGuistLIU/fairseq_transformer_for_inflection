This repository is about how to use the Transformer model from [Fairseq](https://github.com/pytorch/fairseq) from the **command line** for morphological inflection, specifically [SIGMORPHON 2020 Shared Task task0](https://sigmorphon.github.io/sharedtasks/2020/task0/).

## Dependencies

- PyTorch version >= 1.4.0

  You can find how to install PyTorch [here](https://pytorch.org/get-started/locally/).

- Python version >= 3.6

- Fairseq (```$ pip install fairseq```)

- numpy (```$ pip install numpy```)

## Fairseq transformer for inflection

To use the transformer model from Fairseq for inflection, you can preprocess your data, train the model, and generate and evaluate as the following steps:

### Preprocess

This process presupposes that you have stored the SIGMORPHON 2020 Share Task0 data in the directory ```task0-data/```.

It preprocesses the train, dev, test (if there is test) data of the language you specify into the format Fairseq requires. The preprocessed data will be stored in ```data-bin/```. 

Command line to preprocess the data:

```
$ ./preprocess.sh 3LETTER-LANGUAGE-CODE
```

For example, if you want to preprocess the English data, use the following command line:

```
$ ./preprocess.sh eng
```

### Train

To train the model for a specific language, use the following command line:

The trained models will be save in the directory ```checkpoints/3LETTER-LANGUAGE-CODE-models/```.

```
$ ./train.sh 3LETTER-LANGUAGE-CODE
```
For example, the following command line will train the model on the English training data, and will save the models in ```checkpoints/eng-models/```.

```
$ ./train.sh eng
```

You can change parameters at the beginning of ```train.sh``` for parameter tuning.

NOTE: The training takes a long time, especially if you run on a CPU.

### Generate and Evaluate

To make the predictions for the dev or test data for a specific language, use the following command line. 

```
$ ./generate_eval.sh 3LETTER-LANGUAGE-CODE TYPE
```

TYPE can be either *dev* or *test*. It specifies the type of data you want to predict.

For example, to make predictions for the English dev set, use the following command line:

```
$ ./generate_eval.sh eng dev
```

**When you run on the dev set:**

  *if there more than 5 saved models in ```checkpoints/3LETTER-LANGUAGE-CODE-models/```*, it will generate the inflected form with models in ```checkpoints/3LETTER-LANGUAGE-CODE-models/```, find out models with the first 5 highest accuracy scores on the dev set, keep predictions from these five best models as well as ```checkpoints/3LETTER-LANGUAGE-CODE-models/checkpoint_best.pt``` and ```checkpoints/3LETTER-LANGUAGE-CODE-models/checkpoint_last.pt```, and delete all other models.
It will keep the inflected form with the first five best models as well as ```checkpoints/3LETTER-LANGUAGE-CODE-models/checkpoint_best.pt``` and ```checkpoints/3LETTER-LANGUAGE-CODE-models/checkpoint_last.pt```, give you the evaluation scores from the shared task evaluation metric for predictions of each model, and store predictions in the shared task format in the directory ```predictions/3LETTER-LANGUAGE-CODE/```.

  *if there are no more than 5 saved models in ```checkpoints/3LETTER-LANGUAGE-CODE-models/```*, it will generate the inflected form with models in ```checkpoints/3LETTER-LANGUAGE-CODE-models/```, give you the evaluation scores from the shared task evaluation metric for predictions of each model, and store predictions in the shared task format in the directory ```predictions/3LETTER-LANGUAGE-CODE/```.

**When you run on the test set:** 

it will generate the inflected form with models in ```checkpoints/3LETTER-LANGUAGE-CODE-models/```, give you the evaluation scores from the shared task evaluation metric for predictions of each model, and store predictions in the shared task format in the directory ```predictions/3LETTER-LANGUAGE-CODE/```.
