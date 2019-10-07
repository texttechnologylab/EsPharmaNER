from os import system

from flair.data import Span
from flair.datasets import ColumnCorpus
from flair.embeddings import *
from flair.models import SequenceTagger

import util

device = torch.device('cuda:0')

for name, model in ('model_name', ...):  # TODO: model path
    util.print_flag('Loading Model')
    tagger: SequenceTagger = SequenceTagger.load(model)
    print(tagger)

    util.print_flag('Loading Corpus')
    corpus: ColumnCorpus = ColumnCorpus(
        data_folder=os.path.split('resources/data/background_processed.conll')[0],
        train_file=os.path.split('resources/data/background_processed.conll')[1],
        column_format={0: 'text', 1: 'begin', 2: 'end', 3: 'ner'}
    )
    print(corpus)

    util.print_flag('Tagging')
    results: List[Span] = []
    tag_type = 'ner'
    tagged: List[Sentence] = tagger.predict(sentences=corpus.get_all_sentences())
    for sentence in tagged:
        for span in sentence.get_spans(tag_type):
            if span.tag is not "O":
                results.append(span)

    util.print_flag('Evaluating')
    system(f'python3 evaluate.py ner gold/test/subtrack1 system/{model}/ | '
           f'tee resources/models/{model}/eval_results.txt')
