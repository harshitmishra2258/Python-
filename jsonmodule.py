import json
js_str = '{"Name":"Harshit","Boolean":true}'

py_obj=json.loads(js_str)

js=json.dumps(py_obj)

print(js)