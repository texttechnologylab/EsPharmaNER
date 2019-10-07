from flair.data import Span
from flair.datasets import ColumnCorpus
from flair.embeddings import *
from flair.models import SequenceTagger

device = torch.device('cuda:0')
tag_type = 'ner'


def process_file(tagger: SequenceTagger, file_path: Union[str, Path], out_path: Union[str, Path], print_corpus=None):
    try:
        corpus: ColumnCorpus = ColumnCorpus(
            data_folder=os.path.split(file_path)[0],
            train_file=os.path.split(file_path)[1],
            column_format={0: 'text', 1: 'begin', 2: 'end', 3: 'ner'}
        )
        if len(corpus.get_all_sentences()) == 0:
            return 0
        if print_corpus is not None:
            results: List[Span] = []
            result, loss = tagger.evaluate(corpus.train)
            print(result.detailed_results)
            if not os.path.isfile(print_corpus):
                for sentence in corpus.train:
                    for span in sentence.get_spans(tag_type):
                        if span.tag is not "O":
                            results.append(span)
                print_spans_in_brat_format(results, print_corpus)

        return tag_corpus(corpus, file_path, out_path, tagger)
    except IndexError:
        log.error(f'IndexError in file: "{file_path}"!')
        return 0


def tag_corpus(corpus, filename, outpath, tagger):
    results: List[Span] = []
    tagged: List[Sentence] = tagger.predict(sentences=corpus.get_all_sentences())
    for sentence in tagged:
        for span in sentence.get_spans(tag_type):
            if span.tag is not "O":
                results.append(span)
    log.debug(f'Found {len(results)} tags in {filename}')
    print_spans_in_brat_format(results, outpath)
    return len(results)


def print_spans_in_brat_format(results: List[Span], outpath: Union[str, Path], ralign=False):
    with open(outpath, 'w', encoding='utf-8') as outfile:
        if len(results) > 0:
            log10 = int(np.log10(len(results)) + 1)
        else:
            log10 = 1
        for i, span in enumerate(results, start=1):
            if ralign:
                print(f'T{i: <{log10}d}\t{span.tag} {span.start_pos} {span.end_pos}\t{span.text}', file=outfile)
            else:
                print(f'T{i}\t{span.tag} {span.start_pos} {span.end_pos}\t{span.text}', file=outfile)
