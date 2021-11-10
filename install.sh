# Requires: Python version: Python 3.6+ (only 64 bit)

pip install -r requirements.txt

curl -C - https://data.kb.se/datasets/2020/10/swedish_nlp/spacy/sv_pipeline-0.0.0.tar.gz -O
curl -C - https://s3.amazonaws.com/models.huggingface.co/bert/KB/bert-base-swedish-cased/pytorch_model.bin -O
curl -C - https://s3.amazonaws.com/models.huggingface.co/bert/KB/bert-base-swedish-cased/config.json -O
curl -C - https://s3.amazonaws.com/models.huggingface.co/bert/KB/bert-base-swedish-cased/vocab.txt -O

tar -xf sv_pipeline-0.0.0.tar.gz

mkdir models
cd models
mkdir bert-base-swedish-cased
cd ..

mv ./sv_pipeline-0.0.0 ./models 
mv ./pytorch_model.bin ./models/bert-base-swedish-cased
mv ./config.json ./models/bert-base-swedish-cased
mv ./vocab.txt ./models/bert-base-swedish-cased
