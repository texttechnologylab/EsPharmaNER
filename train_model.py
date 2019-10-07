from glob import glob
from os import system

from flair.datasets import ColumnCorpus
from flair.embeddings import *
from flair.models import SequenceTagger
from flair.trainers import ModelTrainer
from tqdm import tqdm

import util
from tag import process_file

device = torch.device('cuda:0')

if __name__ == '__main__':
    util.print_flag('Loading')
    util.print_flag('Dataset', big=False)
    corpus: ColumnCorpus = ColumnCorpus(
        data_folder='resources/data/',
        train_file='concat_PharmaCoNER.conll',
        dev_file=None,
        test_file='test_PharmaCoNER.conll',
        column_format={0: 'text', 1: 'begin', 2: 'end', 3: 'ner'}
    )

    util.print_flag('Embeddings', big=False)
    pooling_op = 'min'
    embeddings: StackedEmbeddings = util.get_embeddings(pooling_op)

    util.print_flag('Training')
    tag_type = 'ner'
    model = f'PharmaCoNER-PCE_{pooling_op}-BPEmb-FT-w2v'
    tagger: SequenceTagger = SequenceTagger(
        embeddings=embeddings,
        tag_dictionary=corpus.make_tag_dictionary(tag_type=tag_type),
        tag_type=tag_type,
        hidden_size=256,
        rnn_layers=1,
        dropout=0.0
    )
    print(tagger)

    trainer: ModelTrainer = ModelTrainer(tagger, corpus)
    trainer.train(
        f'resources/models/{model}',
        learning_rate=0.1,
        mini_batch_size=32,
        patience=3
    )

    util.print_flag('Tagging')
    out_path = f'system/{model}/'
    os.makedirs(out_path, exist_ok=True)

    found_tags = 0
    tq = tqdm(glob('resources/data/background_processed/*.conll'))
    for file in tq:
        file_name = os.path.split(file)[1]
        found_tags += process_file(tagger, file,
                                   os.path.join(out_path, file_name.replace('.conll', '.ann')))
        tq.set_postfix(Tags=found_tags)

    util.print_flag('Evaluating')
    system(
        f'python3 evaluate.py ner gold/test/subtrack1 system/{model}/ | tee resources/models/{model}/eval_results.txt')
