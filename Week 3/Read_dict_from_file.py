import ast
with open("DNA-RNA.txt","r") as f:
    data=f.read()
js=ast.literal_eval(data)

txt = "ATCG"

print(txt.translate(js))
