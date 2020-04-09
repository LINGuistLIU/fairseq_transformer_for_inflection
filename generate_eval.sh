#!/bin/bash

DATABIN=data-bin
CKPTS=checkpoints

LANGUAGE=$1
TYPE=$2

CHECKPOINT_DIR="${CKPTS}/${LANGUAGE}-models"
PRED="${CKPTS}/${LANGUAGE}-predictions/test"

mkdir -p "${CKPTS}/${LANGUAGE}-predictions"

if [[ "${TYPE}" == "dev" ]]; then
    TYPE=valid
    PRED="${CKPTS}/${LANGUAGE}-predictions/dev"
fi

for MODEL in $(ls "${CHECKPOINT_DIR}"); do
  echo "... generating with model ${MODEL} ..."

  fairseq-generate \
      "${DATABIN}/${LANGUAGE}" \
      --gen-subset "${TYPE}" \
      --source-lang "${LANGUAGE}.input" \
      --target-lang "${LANGUAGE}.output" \
      --path "${CHECKPOINT_DIR}/${MODEL}" \
      --beam 5 \
      > "${PRED}-${MODEL}.txt"

done

# Reformat the predictions to the shared task data format

if [[ "${TYPE}" == "valid" ]]; then
    TYPE=dev
    python best_model_on_dev.py $LANGUAGE
fi

python pred2task0Format.py $LANGUAGE $TYPE

## Evaluation
#echo "... evaluating ..."
#python evaluate.py --ref "task0-data/${LANGUAGE}.${TYPE}" --hyp "predictions/${LANGUAGE}.${TYPE}.output"


