l=[[(9,51),(7,9)],[(11,1),(22,19)]]
flat = [ele for sub in l for ele in sub]
res = list(zip(*flat))
print(res)
