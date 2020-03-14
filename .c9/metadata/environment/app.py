{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":100,"position":100,"stack":[[{"start":{"row":24,"column":12},"end":{"row":25,"column":0},"action":"insert","lines":["",""],"id":895},{"start":{"row":25,"column":0},"end":{"row":25,"column":1},"action":"insert","lines":["\t"]}],[{"start":{"row":25,"column":1},"end":{"row":45,"column":41},"action":"insert","lines":["form = request.form.to_dict()","\tuser_in_db = users_collection.find_one({\"username\": form['username']})","\t# Check for user in database","\tif user_in_db:","\t\t# If passwords match (hashed / real password)","\t\tif check_password_hash(user_in_db['password'], form['password']):","\t\t\t# Log user in (add to session)","\t\t\tsession['user'] = form['username']","\t\t\t# If the user is admin redirect him to admin area","\t\t\tif session['user'] == \"user\":","\t\t\t\treturn redirect(url_for('get_recipes'))","\t\t\telse:","\t\t\t\tflash(\"You were logged in!\")","\t\t\t\treturn redirect(url_for('get_recipes', user=user_in_db['username']))","\t\t\t","\t\telse:","\t\t\tflash(\"Wrong password or username!\")","\t\t\treturn redirect(url_for('login'))","\telse:","\t\tflash(\"You need to signup !\")","\t\treturn redirect(url_for('get_recipes'))"],"id":896}],[{"start":{"row":47,"column":0},"end":{"row":57,"column":42},"action":"remove","lines":["\tif 'user' in session:","\t\tuser_in_db = users_collection.find_one({\"username\": session['user']})","\t\tif user_in_db:","\t\t\t# If so redirect user to main page","\t\t\tflash(\"You are logged in already!\")","\t\t\treturn redirect(url_for('get_recipes', user=user_in_db['username']))","\telse:","\t\t# Render the page for user to be able to log in","\t\treturn render_template(\"recipes.html\")","","# Check user login details from login form"],"id":906}],[{"start":{"row":49,"column":0},"end":{"row":50,"column":16},"action":"remove","lines":["@app.route('/user_auth', methods=['POST'])","def user_auth():"],"id":911},{"start":{"row":48,"column":0},"end":{"row":49,"column":0},"action":"remove","lines":["",""]},{"start":{"row":47,"column":0},"end":{"row":48,"column":0},"action":"remove","lines":["",""]},{"start":{"row":46,"column":41},"end":{"row":47,"column":0},"action":"remove","lines":["",""]},{"start":{"row":46,"column":40},"end":{"row":46,"column":41},"action":"remove","lines":["n"]}],[{"start":{"row":46,"column":39},"end":{"row":46,"column":40},"action":"remove","lines":["i"],"id":912},{"start":{"row":46,"column":38},"end":{"row":46,"column":39},"action":"remove","lines":[" "]},{"start":{"row":46,"column":37},"end":{"row":46,"column":38},"action":"remove","lines":["d"]},{"start":{"row":46,"column":36},"end":{"row":46,"column":37},"action":"remove","lines":["e"]},{"start":{"row":46,"column":35},"end":{"row":46,"column":36},"action":"remove","lines":["g"]},{"start":{"row":46,"column":34},"end":{"row":46,"column":35},"action":"remove","lines":["g"]},{"start":{"row":46,"column":33},"end":{"row":46,"column":34},"action":"remove","lines":["o"]},{"start":{"row":46,"column":32},"end":{"row":46,"column":33},"action":"remove","lines":["l"]},{"start":{"row":46,"column":31},"end":{"row":46,"column":32},"action":"remove","lines":[" "]},{"start":{"row":46,"column":30},"end":{"row":46,"column":31},"action":"remove","lines":["y"]},{"start":{"row":46,"column":29},"end":{"row":46,"column":30},"action":"remove","lines":["d"]},{"start":{"row":46,"column":28},"end":{"row":46,"column":29},"action":"remove","lines":["a"]},{"start":{"row":46,"column":27},"end":{"row":46,"column":28},"action":"remove","lines":["e"]},{"start":{"row":46,"column":26},"end":{"row":46,"column":27},"action":"remove","lines":["r"]},{"start":{"row":46,"column":25},"end":{"row":46,"column":26},"action":"remove","lines":["l"]},{"start":{"row":46,"column":24},"end":{"row":46,"column":25},"action":"remove","lines":["a"]},{"start":{"row":46,"column":23},"end":{"row":46,"column":24},"action":"remove","lines":[" "]},{"start":{"row":46,"column":22},"end":{"row":46,"column":23},"action":"remove","lines":["t"]},{"start":{"row":46,"column":21},"end":{"row":46,"column":22},"action":"remove","lines":["o"]},{"start":{"row":46,"column":20},"end":{"row":46,"column":21},"action":"remove","lines":["n"]},{"start":{"row":46,"column":19},"end":{"row":46,"column":20},"action":"remove","lines":[" "]},{"start":{"row":46,"column":18},"end":{"row":46,"column":19},"action":"remove","lines":["s"]},{"start":{"row":46,"column":17},"end":{"row":46,"column":18},"action":"remove","lines":["i"]},{"start":{"row":46,"column":16},"end":{"row":46,"column":17},"action":"remove","lines":[" "]},{"start":{"row":46,"column":15},"end":{"row":46,"column":16},"action":"remove","lines":["r"]},{"start":{"row":46,"column":14},"end":{"row":46,"column":15},"action":"remove","lines":["e"]},{"start":{"row":46,"column":13},"end":{"row":46,"column":14},"action":"remove","lines":["s"]},{"start":{"row":46,"column":12},"end":{"row":46,"column":13},"action":"remove","lines":["u"]},{"start":{"row":46,"column":11},"end":{"row":46,"column":12},"action":"remove","lines":[" "]},{"start":{"row":46,"column":10},"end":{"row":46,"column":11},"action":"remove","lines":["f"]},{"start":{"row":46,"column":9},"end":{"row":46,"column":10},"action":"remove","lines":["i"]},{"start":{"row":46,"column":8},"end":{"row":46,"column":9},"action":"remove","lines":[" "]},{"start":{"row":46,"column":7},"end":{"row":46,"column":8},"action":"remove","lines":["k"]},{"start":{"row":46,"column":6},"end":{"row":46,"column":7},"action":"remove","lines":["c"]},{"start":{"row":46,"column":5},"end":{"row":46,"column":6},"action":"remove","lines":["e"]},{"start":{"row":46,"column":4},"end":{"row":46,"column":5},"action":"remove","lines":["h"]},{"start":{"row":46,"column":3},"end":{"row":46,"column":4},"action":"remove","lines":["C"]},{"start":{"row":46,"column":2},"end":{"row":46,"column":3},"action":"remove","lines":[" "]},{"start":{"row":46,"column":1},"end":{"row":46,"column":2},"action":"remove","lines":["#"]},{"start":{"row":46,"column":0},"end":{"row":46,"column":1},"action":"remove","lines":["\t"]}],[{"start":{"row":58,"column":38},"end":{"row":58,"column":39},"action":"insert","lines":["1"],"id":913}],[{"start":{"row":61,"column":68},"end":{"row":62,"column":0},"action":"insert","lines":["",""],"id":921},{"start":{"row":62,"column":0},"end":{"row":62,"column":3},"action":"insert","lines":["\t\t\t"]},{"start":{"row":62,"column":3},"end":{"row":62,"column":4},"action":"insert","lines":["p"]},{"start":{"row":62,"column":4},"end":{"row":62,"column":5},"action":"insert","lines":["r"]},{"start":{"row":62,"column":5},"end":{"row":62,"column":6},"action":"insert","lines":["i"]},{"start":{"row":62,"column":6},"end":{"row":62,"column":7},"action":"insert","lines":["n"]}],[{"start":{"row":62,"column":7},"end":{"row":62,"column":8},"action":"insert","lines":["t"],"id":922}],[{"start":{"row":62,"column":8},"end":{"row":62,"column":10},"action":"insert","lines":["()"],"id":923}],[{"start":{"row":62,"column":9},"end":{"row":62,"column":10},"action":"insert","lines":["f"],"id":924},{"start":{"row":62,"column":10},"end":{"row":62,"column":11},"action":"insert","lines":["o"]},{"start":{"row":62,"column":11},"end":{"row":62,"column":12},"action":"insert","lines":["r"]},{"start":{"row":62,"column":12},"end":{"row":62,"column":13},"action":"insert","lines":["m"]}],[{"start":{"row":26,"column":41},"end":{"row":26,"column":42},"action":"remove","lines":["\""],"id":925}],[{"start":{"row":26,"column":41},"end":{"row":26,"column":42},"action":"insert","lines":["'"],"id":926}],[{"start":{"row":26,"column":50},"end":{"row":26,"column":51},"action":"remove","lines":["\""],"id":927}],[{"start":{"row":26,"column":50},"end":{"row":26,"column":51},"action":"insert","lines":["'"],"id":928}],[{"start":{"row":59,"column":39},"end":{"row":59,"column":40},"action":"insert","lines":["1"],"id":929}],[{"start":{"row":42,"column":28},"end":{"row":42,"column":33},"action":"remove","lines":["login"],"id":930},{"start":{"row":42,"column":28},"end":{"row":42,"column":29},"action":"insert","lines":["g"]},{"start":{"row":42,"column":29},"end":{"row":42,"column":30},"action":"insert","lines":["e"]},{"start":{"row":42,"column":30},"end":{"row":42,"column":31},"action":"insert","lines":["t"]},{"start":{"row":42,"column":31},"end":{"row":42,"column":32},"action":"insert","lines":["_"]}],[{"start":{"row":42,"column":32},"end":{"row":42,"column":33},"action":"insert","lines":["r"],"id":931},{"start":{"row":42,"column":33},"end":{"row":42,"column":34},"action":"insert","lines":["e"]},{"start":{"row":42,"column":34},"end":{"row":42,"column":35},"action":"insert","lines":["c"]},{"start":{"row":42,"column":35},"end":{"row":42,"column":36},"action":"insert","lines":["i"]},{"start":{"row":42,"column":36},"end":{"row":42,"column":37},"action":"insert","lines":["p"]},{"start":{"row":42,"column":37},"end":{"row":42,"column":38},"action":"insert","lines":["e"]},{"start":{"row":42,"column":38},"end":{"row":42,"column":39},"action":"insert","lines":["s"]}],[{"start":{"row":41,"column":39},"end":{"row":42,"column":0},"action":"insert","lines":["",""],"id":932},{"start":{"row":42,"column":0},"end":{"row":42,"column":3},"action":"insert","lines":["\t\t\t"]},{"start":{"row":42,"column":3},"end":{"row":42,"column":4},"action":"insert","lines":["f"]},{"start":{"row":42,"column":4},"end":{"row":42,"column":5},"action":"insert","lines":["l"]},{"start":{"row":42,"column":5},"end":{"row":42,"column":6},"action":"insert","lines":["a"]}],[{"start":{"row":42,"column":6},"end":{"row":42,"column":7},"action":"insert","lines":["s"],"id":933},{"start":{"row":42,"column":7},"end":{"row":42,"column":8},"action":"insert","lines":["h"]}],[{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"insert","lines":["\""],"id":934}],[{"start":{"row":42,"column":8},"end":{"row":42,"column":9},"action":"remove","lines":["\""],"id":935}],[{"start":{"row":42,"column":8},"end":{"row":42,"column":10},"action":"insert","lines":["()"],"id":936}],[{"start":{"row":42,"column":9},"end":{"row":42,"column":11},"action":"insert","lines":["\"\""],"id":937}],[{"start":{"row":42,"column":10},"end":{"row":42,"column":11},"action":"insert","lines":["T"],"id":938},{"start":{"row":42,"column":11},"end":{"row":42,"column":12},"action":"insert","lines":["r"]},{"start":{"row":42,"column":12},"end":{"row":42,"column":13},"action":"insert","lines":["y"]}],[{"start":{"row":42,"column":13},"end":{"row":42,"column":14},"action":"insert","lines":[" "],"id":939},{"start":{"row":42,"column":14},"end":{"row":42,"column":15},"action":"insert","lines":["l"]},{"start":{"row":42,"column":15},"end":{"row":42,"column":16},"action":"insert","lines":["o"]},{"start":{"row":42,"column":16},"end":{"row":42,"column":17},"action":"insert","lines":["g"]},{"start":{"row":42,"column":17},"end":{"row":42,"column":18},"action":"insert","lines":["i"]}],[{"start":{"row":42,"column":18},"end":{"row":42,"column":19},"action":"insert","lines":["n"],"id":940}],[{"start":{"row":42,"column":19},"end":{"row":42,"column":20},"action":"insert","lines":[" "],"id":941},{"start":{"row":42,"column":20},"end":{"row":42,"column":21},"action":"insert","lines":["a"]},{"start":{"row":42,"column":21},"end":{"row":42,"column":22},"action":"insert","lines":["g"]},{"start":{"row":42,"column":22},"end":{"row":42,"column":23},"action":"insert","lines":["a"]},{"start":{"row":42,"column":23},"end":{"row":42,"column":24},"action":"insert","lines":["i"]},{"start":{"row":42,"column":24},"end":{"row":42,"column":25},"action":"insert","lines":["n"]}],[{"start":{"row":37,"column":18},"end":{"row":37,"column":19},"action":"remove","lines":["e"],"id":942},{"start":{"row":37,"column":17},"end":{"row":37,"column":18},"action":"remove","lines":["r"]},{"start":{"row":37,"column":16},"end":{"row":37,"column":17},"action":"remove","lines":["e"]},{"start":{"row":37,"column":15},"end":{"row":37,"column":16},"action":"remove","lines":["w"]},{"start":{"row":37,"column":14},"end":{"row":37,"column":15},"action":"remove","lines":[" "]},{"start":{"row":37,"column":13},"end":{"row":37,"column":14},"action":"remove","lines":["u"]},{"start":{"row":37,"column":12},"end":{"row":37,"column":13},"action":"remove","lines":["o"]},{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"remove","lines":["Y"]}],[{"start":{"row":37,"column":12},"end":{"row":37,"column":13},"action":"remove","lines":["l"],"id":943},{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"remove","lines":[" "]}],[{"start":{"row":37,"column":11},"end":{"row":37,"column":12},"action":"insert","lines":["L"],"id":944}],[{"start":{"row":37,"column":20},"end":{"row":37,"column":21},"action":"insert","lines":[" "],"id":945},{"start":{"row":37,"column":21},"end":{"row":37,"column":22},"action":"insert","lines":["s"]},{"start":{"row":37,"column":22},"end":{"row":37,"column":23},"action":"insert","lines":["u"]},{"start":{"row":37,"column":23},"end":{"row":37,"column":24},"action":"insert","lines":["c"]},{"start":{"row":37,"column":24},"end":{"row":37,"column":25},"action":"insert","lines":["c"]},{"start":{"row":37,"column":25},"end":{"row":37,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":37,"column":26},"end":{"row":37,"column":27},"action":"insert","lines":["s"],"id":946},{"start":{"row":37,"column":27},"end":{"row":37,"column":28},"action":"insert","lines":["s"]},{"start":{"row":37,"column":28},"end":{"row":37,"column":29},"action":"insert","lines":["f"]},{"start":{"row":37,"column":29},"end":{"row":37,"column":30},"action":"insert","lines":["u"]},{"start":{"row":37,"column":30},"end":{"row":37,"column":31},"action":"insert","lines":["k"]}],[{"start":{"row":37,"column":30},"end":{"row":37,"column":31},"action":"remove","lines":["k"],"id":947}],[{"start":{"row":37,"column":30},"end":{"row":37,"column":31},"action":"insert","lines":["l"],"id":948}],[{"start":{"row":99,"column":30},"end":{"row":100,"column":0},"action":"insert","lines":["",""],"id":949},{"start":{"row":100,"column":0},"end":{"row":100,"column":1},"action":"insert","lines":["\t"]}],[{"start":{"row":100,"column":1},"end":{"row":100,"column":45},"action":"insert","lines":["flash(f\"{form['username']} already exists!\")"],"id":950}],[{"start":{"row":100,"column":13},"end":{"row":100,"column":14},"action":"remove","lines":["m"],"id":951},{"start":{"row":100,"column":12},"end":{"row":100,"column":13},"action":"remove","lines":["r"]},{"start":{"row":100,"column":11},"end":{"row":100,"column":12},"action":"remove","lines":["o"]},{"start":{"row":100,"column":10},"end":{"row":100,"column":11},"action":"remove","lines":["f"]}],[{"start":{"row":100,"column":24},"end":{"row":100,"column":38},"action":"remove","lines":["already exists"],"id":952},{"start":{"row":100,"column":24},"end":{"row":100,"column":43},"action":"insert","lines":["You were logged out"]}],[{"start":{"row":100,"column":23},"end":{"row":100,"column":24},"action":"remove","lines":[" "],"id":953}],[{"start":{"row":100,"column":23},"end":{"row":100,"column":24},"action":"insert","lines":[","],"id":954}],[{"start":{"row":100,"column":24},"end":{"row":100,"column":25},"action":"insert","lines":[" "],"id":955}],[{"start":{"row":100,"column":25},"end":{"row":100,"column":26},"action":"remove","lines":["Y"],"id":956}],[{"start":{"row":100,"column":25},"end":{"row":100,"column":26},"action":"insert","lines":["y"],"id":957}],[{"start":{"row":100,"column":1},"end":{"row":100,"column":47},"action":"remove","lines":["flash(f\"{['username']}, you were logged out!\")"],"id":958},{"start":{"row":100,"column":0},"end":{"row":100,"column":1},"action":"remove","lines":["\t"]},{"start":{"row":99,"column":30},"end":{"row":100,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":6,"column":19},"end":{"row":7,"column":0},"action":"insert","lines":["",""],"id":959}],[{"start":{"row":3,"column":0},"end":{"row":3,"column":13},"action":"remove","lines":["import bcrypt"],"id":961},{"start":{"row":2,"column":33},"end":{"row":3,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":118,"column":34},"end":{"row":118,"column":35},"action":"remove","lines":[">"],"id":962},{"start":{"row":118,"column":33},"end":{"row":118,"column":34},"action":"remove","lines":["d"]},{"start":{"row":118,"column":32},"end":{"row":118,"column":33},"action":"remove","lines":["i"]},{"start":{"row":118,"column":31},"end":{"row":118,"column":32},"action":"remove","lines":["_"]},{"start":{"row":118,"column":30},"end":{"row":118,"column":31},"action":"remove","lines":["e"]},{"start":{"row":118,"column":29},"end":{"row":118,"column":30},"action":"remove","lines":["p"]},{"start":{"row":118,"column":28},"end":{"row":118,"column":29},"action":"remove","lines":["i"]},{"start":{"row":118,"column":27},"end":{"row":118,"column":28},"action":"remove","lines":["c"]},{"start":{"row":118,"column":26},"end":{"row":118,"column":27},"action":"remove","lines":["e"]},{"start":{"row":118,"column":25},"end":{"row":118,"column":26},"action":"remove","lines":["r"]},{"start":{"row":118,"column":24},"end":{"row":118,"column":25},"action":"remove","lines":["<"]}],[{"start":{"row":118,"column":23},"end":{"row":118,"column":24},"action":"remove","lines":["/"],"id":963}],[{"start":{"row":126,"column":28},"end":{"row":126,"column":39},"action":"remove","lines":["<recipe_id>"],"id":964},{"start":{"row":126,"column":27},"end":{"row":126,"column":28},"action":"remove","lines":["/"]}],[{"start":{"row":133,"column":24},"end":{"row":133,"column":25},"action":"remove","lines":["d"],"id":967},{"start":{"row":133,"column":23},"end":{"row":133,"column":24},"action":"remove","lines":["i"]},{"start":{"row":133,"column":22},"end":{"row":133,"column":23},"action":"remove","lines":["_"]},{"start":{"row":133,"column":21},"end":{"row":133,"column":22},"action":"remove","lines":["e"]},{"start":{"row":133,"column":20},"end":{"row":133,"column":21},"action":"remove","lines":["p"]},{"start":{"row":133,"column":19},"end":{"row":133,"column":20},"action":"remove","lines":["i"]},{"start":{"row":133,"column":18},"end":{"row":133,"column":19},"action":"remove","lines":["c"]},{"start":{"row":133,"column":17},"end":{"row":133,"column":18},"action":"remove","lines":["e"]},{"start":{"row":133,"column":16},"end":{"row":133,"column":17},"action":"remove","lines":["r"]}],[{"start":{"row":132,"column":35},"end":{"row":132,"column":36},"action":"remove","lines":[">"],"id":968},{"start":{"row":132,"column":34},"end":{"row":132,"column":35},"action":"remove","lines":["d"]},{"start":{"row":132,"column":33},"end":{"row":132,"column":34},"action":"remove","lines":["i"]},{"start":{"row":132,"column":32},"end":{"row":132,"column":33},"action":"remove","lines":["_"]},{"start":{"row":132,"column":31},"end":{"row":132,"column":32},"action":"remove","lines":["e"]},{"start":{"row":132,"column":30},"end":{"row":132,"column":31},"action":"remove","lines":["p"]},{"start":{"row":132,"column":29},"end":{"row":132,"column":30},"action":"remove","lines":["i"]},{"start":{"row":132,"column":28},"end":{"row":132,"column":29},"action":"remove","lines":["c"]},{"start":{"row":132,"column":27},"end":{"row":132,"column":28},"action":"remove","lines":["e"]},{"start":{"row":132,"column":26},"end":{"row":132,"column":27},"action":"remove","lines":["r"]},{"start":{"row":132,"column":25},"end":{"row":132,"column":26},"action":"remove","lines":["<"]},{"start":{"row":132,"column":24},"end":{"row":132,"column":25},"action":"remove","lines":["/"]}],[{"start":{"row":133,"column":16},"end":{"row":133,"column":25},"action":"insert","lines":["recipe_id"],"id":969}],[{"start":{"row":169,"column":43},"end":{"row":170,"column":0},"action":"insert","lines":["",""],"id":970},{"start":{"row":170,"column":0},"end":{"row":170,"column":4},"action":"insert","lines":["    "]},{"start":{"row":170,"column":4},"end":{"row":171,"column":0},"action":"insert","lines":["",""]},{"start":{"row":171,"column":0},"end":{"row":171,"column":4},"action":"insert","lines":["    "]}],[{"start":{"row":171,"column":3},"end":{"row":171,"column":4},"action":"remove","lines":[" "],"id":971},{"start":{"row":171,"column":2},"end":{"row":171,"column":3},"action":"remove","lines":[" "]},{"start":{"row":171,"column":1},"end":{"row":171,"column":2},"action":"remove","lines":[" "]},{"start":{"row":171,"column":0},"end":{"row":171,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":171,"column":0},"end":{"row":179,"column":4},"action":"insert","lines":["@app.route('/edit_recipe', methods=['POST'])","def edit_recipe(recipe_id):","    if 'user' in session:","        the_recipe = mongo.db.recipes.find_one({\"_id\": ObjectId(recipe_id)})","        all_categories = mongo.db.categories.find()","        return render_template('edit_recipe.html', recipe=the_recipe, categories=all_categories)","    else:","        return render_template(\"recipes.html\", recipes=mongo.db.recipes.find())","    "],"id":972}],[{"start":{"row":171,"column":16},"end":{"row":171,"column":17},"action":"remove","lines":["t"],"id":973},{"start":{"row":171,"column":15},"end":{"row":171,"column":16},"action":"remove","lines":["i"]},{"start":{"row":171,"column":14},"end":{"row":171,"column":15},"action":"remove","lines":["d"]},{"start":{"row":171,"column":13},"end":{"row":171,"column":14},"action":"remove","lines":["e"]}],[{"start":{"row":171,"column":13},"end":{"row":171,"column":14},"action":"insert","lines":["s"],"id":974},{"start":{"row":171,"column":14},"end":{"row":171,"column":15},"action":"insert","lines":["h"]},{"start":{"row":171,"column":15},"end":{"row":171,"column":16},"action":"insert","lines":["o"]},{"start":{"row":171,"column":16},"end":{"row":171,"column":17},"action":"insert","lines":["w"]}],[{"start":{"row":172,"column":7},"end":{"row":172,"column":8},"action":"remove","lines":["t"],"id":975},{"start":{"row":172,"column":6},"end":{"row":172,"column":7},"action":"remove","lines":["i"]},{"start":{"row":172,"column":5},"end":{"row":172,"column":6},"action":"remove","lines":["d"]},{"start":{"row":172,"column":4},"end":{"row":172,"column":5},"action":"remove","lines":["e"]}],[{"start":{"row":172,"column":4},"end":{"row":172,"column":5},"action":"insert","lines":["s"],"id":976},{"start":{"row":172,"column":5},"end":{"row":172,"column":6},"action":"insert","lines":["h"]},{"start":{"row":172,"column":6},"end":{"row":172,"column":7},"action":"insert","lines":["o"]},{"start":{"row":172,"column":7},"end":{"row":172,"column":8},"action":"insert","lines":["w"]}],[{"start":{"row":176,"column":35},"end":{"row":176,"column":36},"action":"remove","lines":["t"],"id":977},{"start":{"row":176,"column":34},"end":{"row":176,"column":35},"action":"remove","lines":["i"]},{"start":{"row":176,"column":33},"end":{"row":176,"column":34},"action":"remove","lines":["d"]},{"start":{"row":176,"column":32},"end":{"row":176,"column":33},"action":"remove","lines":["e"]}],[{"start":{"row":176,"column":32},"end":{"row":176,"column":33},"action":"insert","lines":["s"],"id":978},{"start":{"row":176,"column":33},"end":{"row":176,"column":34},"action":"insert","lines":["h"]},{"start":{"row":176,"column":34},"end":{"row":176,"column":35},"action":"insert","lines":["o"]},{"start":{"row":176,"column":35},"end":{"row":176,"column":36},"action":"insert","lines":["w"]}],[{"start":{"row":171,"column":13},"end":{"row":171,"column":14},"action":"remove","lines":["s"],"id":979}],[{"start":{"row":171,"column":17},"end":{"row":171,"column":23},"action":"remove","lines":["recipe"],"id":980},{"start":{"row":171,"column":17},"end":{"row":171,"column":18},"action":"insert","lines":["t"]},{"start":{"row":171,"column":18},"end":{"row":171,"column":19},"action":"insert","lines":["o"]}],[{"start":{"row":176,"column":32},"end":{"row":176,"column":33},"action":"remove","lines":["s"],"id":981}],[{"start":{"row":176,"column":36},"end":{"row":176,"column":42},"action":"remove","lines":["recipe"],"id":982},{"start":{"row":176,"column":36},"end":{"row":176,"column":37},"action":"insert","lines":["t"]},{"start":{"row":176,"column":37},"end":{"row":176,"column":38},"action":"insert","lines":["o"]}],[{"start":{"row":172,"column":4},"end":{"row":172,"column":5},"action":"remove","lines":["s"],"id":983}],[{"start":{"row":172,"column":8},"end":{"row":172,"column":14},"action":"remove","lines":["recipe"],"id":984},{"start":{"row":172,"column":8},"end":{"row":172,"column":9},"action":"insert","lines":["t"]},{"start":{"row":172,"column":9},"end":{"row":172,"column":10},"action":"insert","lines":["o"]}],[{"start":{"row":171,"column":20},"end":{"row":171,"column":38},"action":"remove","lines":[", methods=['POST']"],"id":985}],[{"start":{"row":121,"column":45},"end":{"row":122,"column":0},"action":"insert","lines":["",""],"id":986},{"start":{"row":122,"column":0},"end":{"row":122,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":122,"column":8},"end":{"row":122,"column":31},"action":"insert","lines":["flash('Recipe deleted')"],"id":987}],[{"start":{"row":122,"column":22},"end":{"row":122,"column":27},"action":"remove","lines":["delet"],"id":988},{"start":{"row":122,"column":22},"end":{"row":122,"column":23},"action":"insert","lines":["a"]},{"start":{"row":122,"column":23},"end":{"row":122,"column":24},"action":"insert","lines":["d"]},{"start":{"row":122,"column":24},"end":{"row":122,"column":25},"action":"insert","lines":["d"]},{"start":{"row":122,"column":25},"end":{"row":122,"column":26},"action":"insert","lines":["e"]}],[{"start":{"row":122,"column":25},"end":{"row":122,"column":26},"action":"remove","lines":["e"],"id":989}],[{"start":{"row":172,"column":19},"end":{"row":172,"column":20},"action":"insert","lines":["/"],"id":990},{"start":{"row":172,"column":20},"end":{"row":172,"column":21},"action":"insert","lines":["<"]}],[{"start":{"row":172,"column":21},"end":{"row":172,"column":22},"action":"insert","lines":["r"],"id":991},{"start":{"row":172,"column":22},"end":{"row":172,"column":23},"action":"insert","lines":["e"]},{"start":{"row":172,"column":23},"end":{"row":172,"column":24},"action":"insert","lines":["c"]}],[{"start":{"row":172,"column":24},"end":{"row":172,"column":25},"action":"insert","lines":["i"],"id":992},{"start":{"row":172,"column":25},"end":{"row":172,"column":26},"action":"insert","lines":["p"]},{"start":{"row":172,"column":26},"end":{"row":172,"column":27},"action":"insert","lines":["e"]}],[{"start":{"row":172,"column":27},"end":{"row":172,"column":28},"action":"insert","lines":["_"],"id":993},{"start":{"row":172,"column":28},"end":{"row":172,"column":29},"action":"insert","lines":["i"]},{"start":{"row":172,"column":29},"end":{"row":172,"column":30},"action":"insert","lines":["d"]}],[{"start":{"row":172,"column":30},"end":{"row":172,"column":31},"action":"insert","lines":[">"],"id":994}],[{"start":{"row":174,"column":24},"end":{"row":174,"column":25},"action":"remove","lines":[":"],"id":995},{"start":{"row":174,"column":23},"end":{"row":174,"column":24},"action":"remove","lines":["n"]},{"start":{"row":174,"column":22},"end":{"row":174,"column":23},"action":"remove","lines":["o"]},{"start":{"row":174,"column":21},"end":{"row":174,"column":22},"action":"remove","lines":["i"]},{"start":{"row":174,"column":20},"end":{"row":174,"column":21},"action":"remove","lines":["s"]},{"start":{"row":174,"column":19},"end":{"row":174,"column":20},"action":"remove","lines":["s"]},{"start":{"row":174,"column":18},"end":{"row":174,"column":19},"action":"remove","lines":["e"]},{"start":{"row":174,"column":17},"end":{"row":174,"column":18},"action":"remove","lines":["s"]},{"start":{"row":174,"column":16},"end":{"row":174,"column":17},"action":"remove","lines":[" "]},{"start":{"row":174,"column":15},"end":{"row":174,"column":16},"action":"remove","lines":["n"]},{"start":{"row":174,"column":14},"end":{"row":174,"column":15},"action":"remove","lines":["i"]},{"start":{"row":174,"column":13},"end":{"row":174,"column":14},"action":"remove","lines":[" "]},{"start":{"row":174,"column":12},"end":{"row":174,"column":13},"action":"remove","lines":["'"]},{"start":{"row":174,"column":11},"end":{"row":174,"column":12},"action":"remove","lines":["r"]},{"start":{"row":174,"column":10},"end":{"row":174,"column":11},"action":"remove","lines":["e"]},{"start":{"row":174,"column":9},"end":{"row":174,"column":10},"action":"remove","lines":["s"]},{"start":{"row":174,"column":8},"end":{"row":174,"column":9},"action":"remove","lines":["u"]},{"start":{"row":174,"column":7},"end":{"row":174,"column":8},"action":"remove","lines":["'"]},{"start":{"row":174,"column":6},"end":{"row":174,"column":7},"action":"remove","lines":[" "]},{"start":{"row":174,"column":5},"end":{"row":174,"column":6},"action":"remove","lines":["f"]},{"start":{"row":174,"column":4},"end":{"row":174,"column":5},"action":"remove","lines":["i"]},{"start":{"row":174,"column":3},"end":{"row":174,"column":4},"action":"remove","lines":[" "]}],[{"start":{"row":174,"column":2},"end":{"row":174,"column":3},"action":"remove","lines":[" "],"id":996},{"start":{"row":174,"column":1},"end":{"row":174,"column":2},"action":"remove","lines":[" "]},{"start":{"row":174,"column":0},"end":{"row":174,"column":1},"action":"remove","lines":[" "]},{"start":{"row":173,"column":22},"end":{"row":174,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":177,"column":4},"end":{"row":178,"column":79},"action":"remove","lines":["else:","        return render_template(\"recipes.html\", recipes=mongo.db.recipes.find())"],"id":997}],[{"start":{"row":173,"column":22},"end":{"row":174,"column":0},"action":"insert","lines":["",""],"id":998},{"start":{"row":174,"column":0},"end":{"row":174,"column":1},"action":"insert","lines":["\t"]}],[{"start":{"row":174,"column":1},"end":{"row":174,"column":22},"action":"insert","lines":["if 'user' in session:"],"id":999}],[{"start":{"row":174,"column":0},"end":{"row":174,"column":1},"action":"insert","lines":[" "],"id":1000}],[{"start":{"row":174,"column":2},"end":{"row":174,"column":3},"action":"insert","lines":[" "],"id":1001},{"start":{"row":174,"column":3},"end":{"row":174,"column":4},"action":"insert","lines":[" "]},{"start":{"row":174,"column":4},"end":{"row":174,"column":5},"action":"insert","lines":[" "]},{"start":{"row":174,"column":5},"end":{"row":174,"column":6},"action":"insert","lines":[" "]}],[{"start":{"row":174,"column":5},"end":{"row":174,"column":6},"action":"remove","lines":[" "],"id":1002},{"start":{"row":174,"column":4},"end":{"row":174,"column":5},"action":"remove","lines":[" "]},{"start":{"row":174,"column":3},"end":{"row":174,"column":4},"action":"remove","lines":[" "]},{"start":{"row":174,"column":2},"end":{"row":174,"column":3},"action":"remove","lines":[" "]}],[{"start":{"row":178,"column":4},"end":{"row":178,"column":5},"action":"insert","lines":["e"],"id":1003},{"start":{"row":178,"column":5},"end":{"row":178,"column":6},"action":"insert","lines":["l"]},{"start":{"row":178,"column":6},"end":{"row":178,"column":7},"action":"insert","lines":["s"]},{"start":{"row":178,"column":7},"end":{"row":178,"column":8},"action":"insert","lines":["e"]},{"start":{"row":178,"column":8},"end":{"row":178,"column":9},"action":"insert","lines":[":"]}],[{"start":{"row":178,"column":9},"end":{"row":179,"column":0},"action":"insert","lines":["",""],"id":1004},{"start":{"row":179,"column":0},"end":{"row":179,"column":5},"action":"insert","lines":["    \t"]}],[{"start":{"row":179,"column":5},"end":{"row":179,"column":76},"action":"insert","lines":["return render_template(\"recipes.html\", recipes=mongo.db.recipes.find())"],"id":1005}],[{"start":{"row":181,"column":0},"end":{"row":188,"column":79},"action":"insert","lines":["@app.route('/add_recipe')","def add_recipe():","    if 'user' in session:","        categories=mongo.db.categories.find()","        flash('Recipe added')","        return render_template('add_recipe.html', categories = categories)","    else:","        return render_template(\"recipes.html\", recipes=mongo.db.recipes.find())"],"id":1006}],[{"start":{"row":175,"column":7},"end":{"row":175,"column":8},"action":"remove","lines":[" "],"id":1007},{"start":{"row":175,"column":6},"end":{"row":175,"column":7},"action":"remove","lines":[" "]},{"start":{"row":175,"column":5},"end":{"row":175,"column":6},"action":"remove","lines":[" "]}],[{"start":{"row":175,"column":4},"end":{"row":175,"column":5},"action":"remove","lines":[" "],"id":1008}],[{"start":{"row":176,"column":7},"end":{"row":176,"column":8},"action":"remove","lines":[" "],"id":1009},{"start":{"row":176,"column":6},"end":{"row":176,"column":7},"action":"remove","lines":[" "]},{"start":{"row":176,"column":5},"end":{"row":176,"column":6},"action":"remove","lines":[" "]},{"start":{"row":176,"column":4},"end":{"row":176,"column":5},"action":"remove","lines":[" "]}],[{"start":{"row":174,"column":1},"end":{"row":174,"column":2},"action":"remove","lines":["\t"],"id":1010},{"start":{"row":174,"column":0},"end":{"row":174,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":174,"column":0},"end":{"row":174,"column":1},"action":"insert","lines":[" "],"id":1011},{"start":{"row":174,"column":1},"end":{"row":174,"column":2},"action":"insert","lines":[" "]},{"start":{"row":174,"column":2},"end":{"row":174,"column":3},"action":"insert","lines":[" "]},{"start":{"row":174,"column":3},"end":{"row":174,"column":4},"action":"insert","lines":[" "]}],[{"start":{"row":175,"column":4},"end":{"row":175,"column":5},"action":"insert","lines":[" "],"id":1012},{"start":{"row":175,"column":5},"end":{"row":175,"column":6},"action":"insert","lines":[" "]},{"start":{"row":175,"column":6},"end":{"row":175,"column":7},"action":"insert","lines":[" "]},{"start":{"row":175,"column":7},"end":{"row":175,"column":8},"action":"insert","lines":[" "]}],[{"start":{"row":176,"column":4},"end":{"row":176,"column":5},"action":"insert","lines":[" "],"id":1013},{"start":{"row":176,"column":5},"end":{"row":176,"column":6},"action":"insert","lines":[" "]},{"start":{"row":176,"column":6},"end":{"row":176,"column":7},"action":"insert","lines":[" "]},{"start":{"row":176,"column":7},"end":{"row":176,"column":8},"action":"insert","lines":[" "]}],[{"start":{"row":181,"column":0},"end":{"row":189,"column":4},"action":"remove","lines":["@app.route('/add_recipe')","def add_recipe():","    if 'user' in session:","        categories=mongo.db.categories.find()","        flash('Recipe added')","        return render_template('add_recipe.html', categories = categories)","    else:","        return render_template(\"recipes.html\", recipes=mongo.db.recipes.find())","    "],"id":1014}],[{"start":{"row":174,"column":24},"end":{"row":174,"column":25},"action":"remove","lines":[":"],"id":1015},{"start":{"row":174,"column":23},"end":{"row":174,"column":24},"action":"remove","lines":["n"]},{"start":{"row":174,"column":22},"end":{"row":174,"column":23},"action":"remove","lines":["o"]},{"start":{"row":174,"column":21},"end":{"row":174,"column":22},"action":"remove","lines":["i"]},{"start":{"row":174,"column":20},"end":{"row":174,"column":21},"action":"remove","lines":["s"]},{"start":{"row":174,"column":19},"end":{"row":174,"column":20},"action":"remove","lines":["s"]},{"start":{"row":174,"column":18},"end":{"row":174,"column":19},"action":"remove","lines":["e"]},{"start":{"row":174,"column":17},"end":{"row":174,"column":18},"action":"remove","lines":["s"]},{"start":{"row":174,"column":16},"end":{"row":174,"column":17},"action":"remove","lines":[" "]},{"start":{"row":174,"column":15},"end":{"row":174,"column":16},"action":"remove","lines":["n"]},{"start":{"row":174,"column":14},"end":{"row":174,"column":15},"action":"remove","lines":["i"]},{"start":{"row":174,"column":13},"end":{"row":174,"column":14},"action":"remove","lines":[" "]},{"start":{"row":174,"column":12},"end":{"row":174,"column":13},"action":"remove","lines":["'"]},{"start":{"row":174,"column":11},"end":{"row":174,"column":12},"action":"remove","lines":["r"]},{"start":{"row":174,"column":10},"end":{"row":174,"column":11},"action":"remove","lines":["e"]},{"start":{"row":174,"column":9},"end":{"row":174,"column":10},"action":"remove","lines":["s"]},{"start":{"row":174,"column":8},"end":{"row":174,"column":9},"action":"remove","lines":["u"]},{"start":{"row":174,"column":7},"end":{"row":174,"column":8},"action":"remove","lines":["'"]},{"start":{"row":174,"column":6},"end":{"row":174,"column":7},"action":"remove","lines":[" "]},{"start":{"row":174,"column":5},"end":{"row":174,"column":6},"action":"remove","lines":["f"]},{"start":{"row":174,"column":4},"end":{"row":174,"column":5},"action":"remove","lines":["i"]},{"start":{"row":174,"column":3},"end":{"row":174,"column":4},"action":"remove","lines":[" "]}],[{"start":{"row":178,"column":3},"end":{"row":180,"column":4},"action":"remove","lines":[" else:","    \treturn render_template(\"recipes.html\", recipes=mongo.db.recipes.find())","    "],"id":1016},{"start":{"row":178,"column":2},"end":{"row":178,"column":3},"action":"remove","lines":[" "]}],[{"start":{"row":133,"column":24},"end":{"row":133,"column":25},"action":"insert","lines":["/"],"id":1017}],[{"start":{"row":133,"column":25},"end":{"row":133,"column":36},"action":"insert","lines":["<recipe_id>"],"id":1018}],[{"start":{"row":124,"column":8},"end":{"row":124,"column":30},"action":"insert","lines":[" flash('Recipe added')"],"id":1021}],[{"start":{"row":123,"column":74},"end":{"row":124,"column":0},"action":"insert","lines":["",""],"id":1021},{"start":{"row":124,"column":0},"end":{"row":124,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":122,"column":7},"end":{"row":122,"column":29},"action":"remove","lines":[" flash('Recipe added')"],"id":1022}]]},"ace":{"folds":[],"scrolltop":1236,"scrollleft":0,"selection":{"start":{"row":113,"column":12},"end":{"row":113,"column":12},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":21,"state":"start","mode":"ace/mode/python"}},"timestamp":1583426743542,"hash":"15218b5ec2de3bbb5774d907653e219ac16d37ff"}