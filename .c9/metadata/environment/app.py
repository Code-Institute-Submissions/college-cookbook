{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":78,"position":78,"stack":[[{"start":{"row":119,"column":7},"end":{"row":119,"column":8},"action":"remove","lines":["w"],"id":2410},{"start":{"row":119,"column":6},"end":{"row":119,"column":7},"action":"remove","lines":["o"]},{"start":{"row":119,"column":5},"end":{"row":119,"column":6},"action":"remove","lines":["h"]},{"start":{"row":119,"column":4},"end":{"row":119,"column":5},"action":"remove","lines":["s"]}],[{"start":{"row":119,"column":4},"end":{"row":119,"column":5},"action":"insert","lines":["g"],"id":2411},{"start":{"row":119,"column":5},"end":{"row":119,"column":6},"action":"insert","lines":["e"]},{"start":{"row":119,"column":6},"end":{"row":119,"column":7},"action":"insert","lines":["t"]}],[{"start":{"row":119,"column":4},"end":{"row":119,"column":14},"action":"remove","lines":["getRecipes"],"id":2412},{"start":{"row":119,"column":4},"end":{"row":119,"column":15},"action":"insert","lines":["get_recipes"]}],[{"start":{"row":118,"column":1},"end":{"row":119,"column":0},"action":"remove","lines":["",""],"id":2413}],[{"start":{"row":118,"column":0},"end":{"row":118,"column":1},"action":"remove","lines":["\t"],"id":2414}],[{"start":{"row":119,"column":4},"end":{"row":124,"column":41},"action":"remove","lines":["page, per_page, offset = get_page_args(page_parameter='page',","\tper_page_parameter='per_page'),","total = mongo.db.recipes.find().count()","paginatedRecipes = get_recipes(offset=offset, per_page=per_page)","pagination = Pagination(page=page, per_page=per_page, total=total,","\t             css_framework='bootstrap4')"],"id":2415},{"start":{"row":119,"column":4},"end":{"row":119,"column":37},"action":"insert","lines":["recipes = mongo.db.recipes.find()"]}],[{"start":{"row":124,"column":11},"end":{"row":128,"column":0},"action":"remove","lines":["page=page,","           per_page=per_page,","           pagination=pagination,","                                 )",""],"id":2416}],[{"start":{"row":120,"column":0},"end":{"row":120,"column":1},"action":"insert","lines":[" "],"id":2417}],[{"start":{"row":120,"column":1},"end":{"row":120,"column":72},"action":"insert","lines":["return render_template(\"recipes.html\", recipes=mongo.db.recipes.find())"],"id":2418}],[{"start":{"row":122,"column":0},"end":{"row":124,"column":11},"action":"remove","lines":["return render_template('recipes.html',","\t\t   recipes=paginatedRecipes,","           "],"id":2419}],[{"start":{"row":120,"column":0},"end":{"row":120,"column":1},"action":"remove","lines":[" "],"id":2420}],[{"start":{"row":120,"column":0},"end":{"row":120,"column":1},"action":"insert","lines":["\t"],"id":2421}],[{"start":{"row":117,"column":0},"end":{"row":118,"column":0},"action":"insert","lines":["",""],"id":2422}],[{"start":{"row":102,"column":0},"end":{"row":116,"column":42},"action":"remove","lines":["def get_recipes(offset=0, per_page=3):","\trecipes = mongo.db.recipes.find()","\tprint (\"herl\")","\treturn recipes[offset:offset + per_page]","\t","@app.route('get_recipes')","def showRecipes():","\tpage, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')","\ttotal = mong.db.recipes.find()","","","\tdef get_recipes(offset=0, per_page=3):","\t  recipes = mongo.db.recipes.find()","\tprint(\"herl\")","\treturn recipes[offset: offset + per_page]"],"id":2423}],[{"start":{"row":102,"column":0},"end":{"row":103,"column":0},"action":"remove","lines":["",""],"id":2424}],[{"start":{"row":109,"column":3},"end":{"row":109,"column":4},"action":"remove","lines":[" "],"id":2425},{"start":{"row":109,"column":2},"end":{"row":109,"column":3},"action":"remove","lines":[" "]},{"start":{"row":109,"column":1},"end":{"row":109,"column":2},"action":"remove","lines":[" "]}],[{"start":{"row":102,"column":0},"end":{"row":103,"column":0},"action":"remove","lines":["",""],"id":2426}],[{"start":{"row":102,"column":0},"end":{"row":103,"column":0},"action":"insert","lines":["",""],"id":2427}],[{"start":{"row":106,"column":0},"end":{"row":106,"column":1},"action":"remove","lines":["\t"],"id":2428}],[{"start":{"row":105,"column":3},"end":{"row":105,"column":4},"action":"remove","lines":[" "],"id":2429},{"start":{"row":105,"column":2},"end":{"row":105,"column":3},"action":"remove","lines":[" "]},{"start":{"row":105,"column":1},"end":{"row":105,"column":2},"action":"remove","lines":[" "]},{"start":{"row":105,"column":0},"end":{"row":105,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":105,"column":0},"end":{"row":105,"column":1},"action":"insert","lines":["\t"],"id":2430}],[{"start":{"row":106,"column":0},"end":{"row":106,"column":1},"action":"insert","lines":["\t"],"id":2431}],[{"start":{"row":103,"column":0},"end":{"row":107,"column":1},"action":"remove","lines":["@app.route('/get_recipes')","def get_recipes():","\trecipes = mongo.db.recipes.find()","\treturn render_template(\"recipes.html\", recipes=mongo.db.recipes.find())"," "],"id":2432},{"start":{"row":103,"column":0},"end":{"row":109,"column":77},"action":"insert","lines":["@app.route('/')","@app.route('/get_recipes')","def get_recipes():","    if 'user' in session:","      return render_template(\"recipes.html\", recipes=mongo.db.recipes.find(), user = session['user'])","    else:","      return render_template(\"recipes.html\", recipes=mongo.db.recipes.find())"]}],[{"start":{"row":138,"column":51},"end":{"row":139,"column":0},"action":"insert","lines":["",""],"id":2433},{"start":{"row":139,"column":0},"end":{"row":139,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":139,"column":8},"end":{"row":139,"column":29},"action":"insert","lines":["flash('Recipe added')"],"id":2434}],[{"start":{"row":139,"column":24},"end":{"row":139,"column":25},"action":"remove","lines":["d"],"id":2435},{"start":{"row":139,"column":23},"end":{"row":139,"column":24},"action":"remove","lines":["d"]},{"start":{"row":139,"column":22},"end":{"row":139,"column":23},"action":"remove","lines":["a"]}],[{"start":{"row":139,"column":22},"end":{"row":139,"column":23},"action":"insert","lines":["e"],"id":2436},{"start":{"row":139,"column":23},"end":{"row":139,"column":24},"action":"insert","lines":["d"]},{"start":{"row":139,"column":24},"end":{"row":139,"column":25},"action":"insert","lines":["i"]}],[{"start":{"row":139,"column":25},"end":{"row":139,"column":26},"action":"insert","lines":["t"],"id":2437}],[{"start":{"row":141,"column":9},"end":{"row":142,"column":0},"action":"insert","lines":["",""],"id":2462},{"start":{"row":142,"column":0},"end":{"row":142,"column":5},"action":"insert","lines":["    \t"]}],[{"start":{"row":142,"column":4},"end":{"row":142,"column":5},"action":"remove","lines":["\t"],"id":2464},{"start":{"row":142,"column":3},"end":{"row":142,"column":4},"action":"remove","lines":[" "]},{"start":{"row":142,"column":2},"end":{"row":142,"column":3},"action":"remove","lines":[" "]},{"start":{"row":142,"column":1},"end":{"row":142,"column":2},"action":"remove","lines":[" "]},{"start":{"row":142,"column":0},"end":{"row":142,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":141,"column":9},"end":{"row":142,"column":0},"action":"remove","lines":["",""],"id":2465}],[{"start":{"row":142,"column":79},"end":{"row":143,"column":0},"action":"insert","lines":["",""],"id":2466},{"start":{"row":143,"column":0},"end":{"row":143,"column":8},"action":"insert","lines":["        "]}],[{"start":{"row":143,"column":8},"end":{"row":143,"column":29},"action":"insert","lines":["flash('Recipe added')"],"id":2467}],[{"start":{"row":143,"column":28},"end":{"row":143,"column":29},"action":"remove","lines":[")"],"id":2468},{"start":{"row":143,"column":27},"end":{"row":143,"column":28},"action":"remove","lines":["'"]},{"start":{"row":143,"column":26},"end":{"row":143,"column":27},"action":"remove","lines":["d"]},{"start":{"row":143,"column":25},"end":{"row":143,"column":26},"action":"remove","lines":["e"]},{"start":{"row":143,"column":24},"end":{"row":143,"column":25},"action":"remove","lines":["d"]},{"start":{"row":143,"column":23},"end":{"row":143,"column":24},"action":"remove","lines":["d"]},{"start":{"row":143,"column":22},"end":{"row":143,"column":23},"action":"remove","lines":["a"]},{"start":{"row":143,"column":21},"end":{"row":143,"column":22},"action":"remove","lines":[" "]},{"start":{"row":143,"column":20},"end":{"row":143,"column":21},"action":"remove","lines":["e"]},{"start":{"row":143,"column":19},"end":{"row":143,"column":20},"action":"remove","lines":["p"]},{"start":{"row":143,"column":18},"end":{"row":143,"column":19},"action":"remove","lines":["i"]},{"start":{"row":143,"column":17},"end":{"row":143,"column":18},"action":"remove","lines":["c"]},{"start":{"row":143,"column":16},"end":{"row":143,"column":17},"action":"remove","lines":["e"]},{"start":{"row":143,"column":15},"end":{"row":143,"column":16},"action":"remove","lines":["R"]},{"start":{"row":143,"column":14},"end":{"row":143,"column":15},"action":"remove","lines":["'"]},{"start":{"row":143,"column":13},"end":{"row":143,"column":14},"action":"remove","lines":["("]},{"start":{"row":143,"column":12},"end":{"row":143,"column":13},"action":"remove","lines":["h"]},{"start":{"row":143,"column":11},"end":{"row":143,"column":12},"action":"remove","lines":["s"]},{"start":{"row":143,"column":10},"end":{"row":143,"column":11},"action":"remove","lines":["a"]},{"start":{"row":143,"column":9},"end":{"row":143,"column":10},"action":"remove","lines":["l"]},{"start":{"row":143,"column":8},"end":{"row":143,"column":9},"action":"remove","lines":["f"]},{"start":{"row":143,"column":7},"end":{"row":143,"column":8},"action":"remove","lines":[" "]}],[{"start":{"row":143,"column":6},"end":{"row":143,"column":7},"action":"remove","lines":[" "],"id":2469},{"start":{"row":143,"column":5},"end":{"row":143,"column":6},"action":"remove","lines":[" "]},{"start":{"row":143,"column":4},"end":{"row":143,"column":5},"action":"remove","lines":[" "]},{"start":{"row":143,"column":3},"end":{"row":143,"column":4},"action":"remove","lines":[" "]},{"start":{"row":143,"column":2},"end":{"row":143,"column":3},"action":"remove","lines":[" "]}],[{"start":{"row":143,"column":1},"end":{"row":143,"column":2},"action":"remove","lines":[" "],"id":2470},{"start":{"row":143,"column":0},"end":{"row":143,"column":1},"action":"remove","lines":[" "]},{"start":{"row":142,"column":79},"end":{"row":143,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":141,"column":9},"end":{"row":141,"column":10},"action":"insert","lines":["\t"],"id":2471}],[{"start":{"row":141,"column":10},"end":{"row":141,"column":11},"action":"insert","lines":["f"],"id":2472},{"start":{"row":141,"column":11},"end":{"row":141,"column":12},"action":"insert","lines":["l"]},{"start":{"row":141,"column":12},"end":{"row":141,"column":13},"action":"insert","lines":["a"]},{"start":{"row":141,"column":13},"end":{"row":141,"column":14},"action":"insert","lines":["s"]}],[{"start":{"row":141,"column":14},"end":{"row":141,"column":15},"action":"insert","lines":["h"],"id":2473}],[{"start":{"row":141,"column":15},"end":{"row":141,"column":17},"action":"insert","lines":["()"],"id":2474}],[{"start":{"row":123,"column":27},"end":{"row":123,"column":28},"action":"insert","lines":[" "],"id":2475},{"start":{"row":123,"column":28},"end":{"row":123,"column":29},"action":"insert","lines":["s"]}],[{"start":{"row":123,"column":29},"end":{"row":123,"column":30},"action":"insert","lines":["u"],"id":2476},{"start":{"row":123,"column":30},"end":{"row":123,"column":31},"action":"insert","lines":["c"]}],[{"start":{"row":123,"column":31},"end":{"row":123,"column":32},"action":"insert","lines":["c"],"id":2477}],[{"start":{"row":123,"column":28},"end":{"row":123,"column":32},"action":"remove","lines":["succ"],"id":2478},{"start":{"row":123,"column":28},"end":{"row":123,"column":38},"action":"insert","lines":["successful"]}],[{"start":{"row":123,"column":38},"end":{"row":123,"column":39},"action":"insert","lines":["l"],"id":2479},{"start":{"row":123,"column":39},"end":{"row":123,"column":40},"action":"insert","lines":["y"]}],[{"start":{"row":141,"column":16},"end":{"row":141,"column":17},"action":"remove","lines":[")"],"id":2480},{"start":{"row":141,"column":15},"end":{"row":141,"column":16},"action":"remove","lines":["("]},{"start":{"row":141,"column":14},"end":{"row":141,"column":15},"action":"remove","lines":["h"]},{"start":{"row":141,"column":13},"end":{"row":141,"column":14},"action":"remove","lines":["s"]},{"start":{"row":141,"column":12},"end":{"row":141,"column":13},"action":"remove","lines":["a"]},{"start":{"row":141,"column":11},"end":{"row":141,"column":12},"action":"remove","lines":["l"]},{"start":{"row":141,"column":10},"end":{"row":141,"column":11},"action":"remove","lines":["f"]},{"start":{"row":141,"column":9},"end":{"row":141,"column":10},"action":"remove","lines":["\t"]}],[{"start":{"row":141,"column":9},"end":{"row":142,"column":0},"action":"insert","lines":["",""],"id":2511},{"start":{"row":142,"column":0},"end":{"row":142,"column":5},"action":"insert","lines":["    \t"]}],[{"start":{"row":142,"column":5},"end":{"row":142,"column":6},"action":"insert","lines":["f"],"id":2512},{"start":{"row":142,"column":6},"end":{"row":142,"column":7},"action":"insert","lines":["l"]},{"start":{"row":142,"column":7},"end":{"row":142,"column":8},"action":"insert","lines":["a"]},{"start":{"row":142,"column":8},"end":{"row":142,"column":9},"action":"insert","lines":["s"]},{"start":{"row":142,"column":9},"end":{"row":142,"column":10},"action":"insert","lines":["h"]}],[{"start":{"row":142,"column":10},"end":{"row":142,"column":11},"action":"insert","lines":["\""],"id":2513}],[{"start":{"row":142,"column":10},"end":{"row":142,"column":11},"action":"remove","lines":["\""],"id":2514}],[{"start":{"row":142,"column":10},"end":{"row":142,"column":12},"action":"insert","lines":["()"],"id":2515}],[{"start":{"row":142,"column":11},"end":{"row":142,"column":13},"action":"insert","lines":["\"\""],"id":2516}],[{"start":{"row":142,"column":13},"end":{"row":142,"column":14},"action":"remove","lines":[")"],"id":2517},{"start":{"row":142,"column":12},"end":{"row":142,"column":13},"action":"remove","lines":["\""]},{"start":{"row":142,"column":11},"end":{"row":142,"column":12},"action":"remove","lines":["\""]},{"start":{"row":142,"column":10},"end":{"row":142,"column":11},"action":"remove","lines":["("]},{"start":{"row":142,"column":9},"end":{"row":142,"column":10},"action":"remove","lines":["h"]},{"start":{"row":142,"column":8},"end":{"row":142,"column":9},"action":"remove","lines":["s"]},{"start":{"row":142,"column":7},"end":{"row":142,"column":8},"action":"remove","lines":["a"]},{"start":{"row":142,"column":6},"end":{"row":142,"column":7},"action":"remove","lines":["l"]},{"start":{"row":142,"column":5},"end":{"row":142,"column":6},"action":"remove","lines":["f"]},{"start":{"row":142,"column":4},"end":{"row":142,"column":5},"action":"remove","lines":["\t"]},{"start":{"row":142,"column":3},"end":{"row":142,"column":4},"action":"remove","lines":[" "]}],[{"start":{"row":142,"column":2},"end":{"row":142,"column":3},"action":"remove","lines":[" "],"id":2518},{"start":{"row":142,"column":1},"end":{"row":142,"column":2},"action":"remove","lines":[" "]},{"start":{"row":142,"column":0},"end":{"row":142,"column":1},"action":"remove","lines":[" "]},{"start":{"row":141,"column":9},"end":{"row":142,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":141,"column":9},"end":{"row":142,"column":0},"action":"insert","lines":["",""],"id":2519},{"start":{"row":142,"column":0},"end":{"row":142,"column":5},"action":"insert","lines":["    \t"]}],[{"start":{"row":142,"column":5},"end":{"row":142,"column":6},"action":"insert","lines":["f"],"id":2520}],[{"start":{"row":142,"column":5},"end":{"row":142,"column":6},"action":"remove","lines":["f"],"id":2521},{"start":{"row":142,"column":5},"end":{"row":142,"column":10},"action":"insert","lines":["flash"]}],[{"start":{"row":142,"column":9},"end":{"row":142,"column":10},"action":"remove","lines":["h"],"id":2522},{"start":{"row":142,"column":8},"end":{"row":142,"column":9},"action":"remove","lines":["s"]},{"start":{"row":142,"column":7},"end":{"row":142,"column":8},"action":"remove","lines":["a"]},{"start":{"row":142,"column":6},"end":{"row":142,"column":7},"action":"remove","lines":["l"]},{"start":{"row":142,"column":5},"end":{"row":142,"column":6},"action":"remove","lines":["f"]},{"start":{"row":142,"column":4},"end":{"row":142,"column":5},"action":"remove","lines":["\t"]},{"start":{"row":142,"column":3},"end":{"row":142,"column":4},"action":"remove","lines":[" "]},{"start":{"row":142,"column":2},"end":{"row":142,"column":3},"action":"remove","lines":[" "]}],[{"start":{"row":142,"column":1},"end":{"row":142,"column":2},"action":"remove","lines":[" "],"id":2523},{"start":{"row":142,"column":0},"end":{"row":142,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":142,"column":0},"end":{"row":142,"column":1},"action":"insert","lines":["f"],"id":2524},{"start":{"row":142,"column":1},"end":{"row":142,"column":2},"action":"insert","lines":["l"]},{"start":{"row":142,"column":2},"end":{"row":142,"column":3},"action":"insert","lines":["a"]},{"start":{"row":142,"column":3},"end":{"row":142,"column":4},"action":"insert","lines":["s"]}],[{"start":{"row":142,"column":0},"end":{"row":142,"column":4},"action":"remove","lines":["flas"],"id":2525},{"start":{"row":142,"column":0},"end":{"row":142,"column":5},"action":"insert","lines":["flash"]}],[{"start":{"row":142,"column":5},"end":{"row":142,"column":6},"action":"insert","lines":[" "],"id":2526}],[{"start":{"row":142,"column":5},"end":{"row":142,"column":6},"action":"remove","lines":[" "],"id":2527}],[{"start":{"row":142,"column":0},"end":{"row":142,"column":1},"action":"insert","lines":["\t"],"id":2528}],[{"start":{"row":142,"column":1},"end":{"row":142,"column":2},"action":"insert","lines":["\t"],"id":2529}],[{"start":{"row":142,"column":2},"end":{"row":142,"column":3},"action":"insert","lines":["\t"],"id":2530}],[{"start":{"row":142,"column":3},"end":{"row":142,"column":4},"action":"insert","lines":["\t"],"id":2531}],[{"start":{"row":142,"column":4},"end":{"row":142,"column":5},"action":"insert","lines":["\t"],"id":2532}],[{"start":{"row":142,"column":5},"end":{"row":142,"column":6},"action":"insert","lines":["\t"],"id":2533}],[{"start":{"row":142,"column":6},"end":{"row":142,"column":7},"action":"insert","lines":["\t"],"id":2534}],[{"start":{"row":142,"column":7},"end":{"row":142,"column":8},"action":"insert","lines":["\t"],"id":2535}],[{"start":{"row":142,"column":7},"end":{"row":142,"column":8},"action":"remove","lines":["\t"],"id":2536},{"start":{"row":142,"column":6},"end":{"row":142,"column":7},"action":"remove","lines":["\t"]},{"start":{"row":142,"column":5},"end":{"row":142,"column":6},"action":"remove","lines":["\t"]},{"start":{"row":142,"column":4},"end":{"row":142,"column":5},"action":"remove","lines":["\t"]},{"start":{"row":142,"column":3},"end":{"row":142,"column":4},"action":"remove","lines":["\t"]},{"start":{"row":142,"column":2},"end":{"row":142,"column":3},"action":"remove","lines":["\t"]},{"start":{"row":142,"column":1},"end":{"row":142,"column":2},"action":"remove","lines":["\t"]},{"start":{"row":142,"column":0},"end":{"row":142,"column":1},"action":"remove","lines":["\t"]},{"start":{"row":141,"column":9},"end":{"row":142,"column":0},"action":"remove","lines":["",""]},{"start":{"row":141,"column":8},"end":{"row":141,"column":9},"action":"remove","lines":[":"]}],[{"start":{"row":141,"column":8},"end":{"row":141,"column":9},"action":"insert","lines":["\""],"id":2537}],[{"start":{"row":141,"column":8},"end":{"row":141,"column":9},"action":"remove","lines":["\""],"id":2538}],[{"start":{"row":141,"column":8},"end":{"row":141,"column":9},"action":"insert","lines":[":"],"id":2539}],[{"start":{"row":141,"column":9},"end":{"row":141,"column":10},"action":"insert","lines":[" "],"id":2540}],[{"start":{"row":141,"column":10},"end":{"row":142,"column":0},"action":"insert","lines":["",""],"id":2541},{"start":{"row":142,"column":0},"end":{"row":142,"column":5},"action":"insert","lines":["    \t"]}],[{"start":{"row":142,"column":9},"end":{"row":142,"column":10},"action":"remove","lines":["h"],"id":2542},{"start":{"row":142,"column":8},"end":{"row":142,"column":9},"action":"remove","lines":["s"]},{"start":{"row":142,"column":7},"end":{"row":142,"column":8},"action":"remove","lines":["a"]},{"start":{"row":142,"column":6},"end":{"row":142,"column":7},"action":"remove","lines":["l"]},{"start":{"row":142,"column":5},"end":{"row":142,"column":6},"action":"remove","lines":["f"]},{"start":{"row":142,"column":4},"end":{"row":142,"column":5},"action":"remove","lines":["\t"]},{"start":{"row":142,"column":3},"end":{"row":142,"column":4},"action":"remove","lines":[" "]},{"start":{"row":142,"column":2},"end":{"row":142,"column":3},"action":"remove","lines":[" "]},{"start":{"row":142,"column":1},"end":{"row":142,"column":2},"action":"remove","lines":[" "]},{"start":{"row":142,"column":0},"end":{"row":142,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":141,"column":10},"end":{"row":142,"column":0},"action":"remove","lines":["",""],"id":2543}],[{"start":{"row":173,"column":9},"end":{"row":174,"column":0},"action":"insert","lines":["",""],"id":2547},{"start":{"row":174,"column":0},"end":{"row":174,"column":5},"action":"insert","lines":["    \t"]}],[{"start":{"row":173,"column":8},"end":{"row":173,"column":9},"action":"insert","lines":[":"],"id":2547}],[{"start":{"row":173,"column":4},"end":{"row":173,"column":5},"action":"insert","lines":["e"],"id":2548},{"start":{"row":173,"column":5},"end":{"row":173,"column":6},"action":"insert","lines":["l"]},{"start":{"row":173,"column":6},"end":{"row":173,"column":7},"action":"insert","lines":["s"]},{"start":{"row":173,"column":7},"end":{"row":173,"column":8},"action":"insert","lines":["e"]}],[{"start":{"row":172,"column":43},"end":{"row":173,"column":0},"action":"insert","lines":["",""],"id":2549},{"start":{"row":173,"column":0},"end":{"row":173,"column":4},"action":"insert","lines":["    "]}]]},"ace":{"folds":[],"scrolltop":1964.5,"scrollleft":0,"selection":{"start":{"row":138,"column":51},"end":{"row":138,"column":51},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":34,"state":"start","mode":"ace/mode/python"}},"timestamp":1589015869187,"hash":"ebe0bc80b2d108946f9349d3495e9a3e3037d9c7"}