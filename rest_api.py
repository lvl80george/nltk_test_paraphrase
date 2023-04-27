from flask import Flask, jsonify, request
from nltk import Tree
from paraphrase import paraphrase

app = Flask(__name__)


@app.route('/paraphrase', methods=['GET'])
def paraphrase_api():
    tree_str = request.args.get("tree") # obligatory argument, the tree's representation
    limit_str = request.args.get('limit', 20) # optional argument
    
    tree = Tree.fromstring(tree_str)
    limit = int(limit_str)
    
    result = paraphrase(tree,limit)
    # turn each tree into string representation
    result_str = [{'tree':str(r)} for r in result]
    return jsonify({'paraphrases': result_str})

# run it from here in debug
app.run(debug=True)
