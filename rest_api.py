from flask import Flask, jsonify, request
from nltk import Tree
from paraphrase import paraphrase

app = Flask(__name__)


@app.route('/paraphrase', methods=['GET'])
def paraphrase_api():
    # get the arguments
    tree_str = request.args.get("tree") # obligatory argument, the tree's representation
    limit_str = request.args.get('limit', 20) # optional argument, default is 20

    tree = Tree.fromstring(tree_str)
    limit = int(limit_str)

    # construct the paraphrases
    result = paraphrase(tree,limit)
    
    # turn each tree into a string representation
    infinity = float('inf')
    # nltk adds \n when printing big trees to make the
    # output multiline (I don't want to see them)
    # converting trees to string with pformat and setting margin maximal
    # makes it output virtually any tree without \n line separators
    result_str = [{'tree':r.pformat(margin=infinity)} for r in result]
    return jsonify({'paraphrases': result_str})
    # returns json like
    # {  "paraphrases": [ {"tree":...}, {"tree":....}....

# run it from here in debug mode
app.run(debug=True)
