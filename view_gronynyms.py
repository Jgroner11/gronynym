import pickle

with open('gronynyms.pkl', 'rb') as f:
    lst = pickle.load(f)
    gronynyms = lst[0]
    perfect_gronynyms = lst[1]

def length_alpha_sort(key):
    return (len(key), key)

gronynyms = {k:  v for k, v in sorted(gronynyms.items(), key=lambda item: length_alpha_sort(item[0]))}
perfect_gronynyms = {k:  v for k, v in sorted(perfect_gronynyms.items(), key=lambda item: length_alpha_sort(item[0]))}

with open('gronynyms.txt', 'w') as f:
    for k, v in  gronynyms.items():
        f.write(k + ' ' + str(v) + '\n')

with open('perfect_gronynyms.txt', 'w') as f:
    for k, v in  perfect_gronynyms.items():
        f.write(k + ' ' + str(v) + '\n')