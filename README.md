# EsPharmaNER
This repository contains the source code and data to reproduce the results of [Stoeckel et. al (2019)](#Cite) 
on the [PharmaCoNER](http://temu.bsc.es/pharmaconer/) Challenge. 

### Setup
- Extract the CoNLL 2003 formatted datasets from `/resources/data.7z` into `/resources/`.
- Download the test data from [here](http://temu.bsc.es/pharmaconer/wp-content/uploads/2019/06/test-set_1.1.zip) 
and extract the contents of the `test-set_1.1.zip` folder to `gold/`. 
    - The relative path for gold annotated data should now be `gold/test/subtrack1/`.

### Hardware Pre-requisites
You will need a CUDA compatible GPU with ~6GB VRAM available.
During our experiments we used a NVIDIA GeForce GTX 1660.

### Dataset
#### PharmaCoNER Corpus
The PharmaCoNER dataset was released as part of the [PharmaCoNER Challenge](http://temu.bsc.es/pharmaconer).
It contains 1000 clinical cases from spanish open access literature with gold standard annotations for four categories.
For more information, refer to the challenge organizers website: http://temu.bsc.es/pharmaconer/index.php/datasets/

#### Spanish Health Corpus
The Spanish Health Corpus is comprised of a selection of Spanish Health Science documents. 
These documents were obtained from [SciElo](https://scielo.org/) by means of an automated crawler.
The full list of document ids that were used to create the corpus can be found in the
`Spanish_Health_Corpus-document_ids.txt` file that is part of this repository.

These IDs can be used to obtain the document text from its corresponding collection like this:
http://scielo.isciii.es/scielo.php?script=sci_arttext&pid=S0004-05922010000100016

Please note, that the IDs must be mapped to the correct collection to obtain the documents.
See https://scielo.org/ or the list below for a all available collections:
- http://www.scielo.org.ar 
- http://www.scielo.org.bo 
- http://www.scielo.br 
- http://www.scielo.cl 
- http://www.scielo.org.co 
- http://www.scielo.sa.cr 
- http://scielo.sld.cu 
- http://www.scielo.org.mx 
- http://scielo.iics.una.py 
- http://www.scielo.org.pe 
- http://www.scielo.mec.pt 
- http://www.scielosp.org 
- http://www.scielo.org.za 
- http://scielo.isciii.es 
- http://www.scielo.edu.uy 
- http://scielo.senescyt.gob.ec 
- http://ve.scielo.org 
- http://westindies.scielo.org 
    
### Cite
Please use the following citation:

>M. Stoeckel, W. Hemati, and A. Mehler,
>"When Specialization Helps: Using Pooled Contextualized Embeddings to Detect Chemical and Biomedical Entities in Spanish",
>in <i>Proceedings of the International Workshop on BioNLP Open Shared Tasks (BioNLP-OST)</i>, 2019.
><i>accepted</i>

BibTex entry:
```
@InProceedings{Stoeckel:Hemati:Mehler:2019,
    author = {Manuel Stoeckel and Wahed Hemati and Alexander Mehler},
    title = {{When Specialization Helps: Using Pooled Contextualized Embeddings to Detect Chemical and Biomedical Entities in Spanish}},
    booktitle = {Proceedings of the International Workshop on BioNLP Open Shared Tasks (BioNLP-OST)},
    publisher = {Association for Computational Linguistics SIGDAT and Asian Federation of Natural Language Processing},
    location = {Hong Kong, China},
    year = 2019,
    note = {accepted}
}
```

### Acknowledgements
This publication is part of the BIOfid project. Visit https://www.biofid.de/en/ for more information. 
