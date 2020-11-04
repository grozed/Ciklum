import pytest

def generate_sentences_loop(subjects,predicates,objects):
	subjects.sort()
	predicates.sort()
	objects.sort()
	for subs in subjects:
		for pred in predicates:
			for obj in objects:
				frase= subs + " " + pred + " " + obj + "."
				print(frase)


def recursive_gen(arr, m, n, output):
    global sentence
    output[m] = arr[m][n]
    if m==2:
        for i in range(2):
            sentence=sentence + output[i] + " "
        sentence = sentence + output[m] + ". "
        return

    for i in range(Len):
        try:
            recursive_gen(arr, m+1, i, output)
        except:
            err2=err2+1
            if (err2==3):
                sentence=rstrip(sentence)
 
def generate_sentences(subjects,predicates,objects):
    subjects.sort()
    predicates.sort()
    objects.sort()
    arr=[subjects,predicates,objects]

    err=0
    output=[""]*3
    for i in range(Len):
        try:
            recursive_gen(arr, 0, i, output)
        except:
            err=err+1
    return sentence    
        
subjects=["Mark", "Mary"]
predicates=["hates", "loves"]
objects=["apples", "bananas"]
 

Len = max(len(subjects),len(predicates),len(objects))
a = 0
sentence=""

sentence=generate_sentences(subjects,predicates,objects)
#generate_sentences_loop(subjects,predicates,objects)
print(sentence)

