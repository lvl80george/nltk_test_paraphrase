# nltk_test_paraphrase
This is a test task

To run it, launch **rest_api.py** - it will open a debug Flask server on localhost

It will only serve one route **/paraphrase** and GET attributes **tree** and **limit** (optional, default 20, to remove limit set -1)

So it receives queries like 
*http://localhost:5000/paraphrase?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter)) (, ,) (CC or) (NP (NNP Barri) (NNP G\u00f2tic))) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets)) (VP (VBN filled) (PP (IN with) (NP (NP (JJ Catalan) (NNS restaurants)) (, ,) (NP (NNS clubs)) (CC and) (NP (JJ trendy) (NNS bars))))))))&limit=-1*
and returns json with generated variants
