"""
Sorting Acronym
Author: Woramat Ngamkham
"""


def acronym(txts):
    acronym_word = []
    for i in range(len(txts)):
        words = txts[i].split()
        upper_first_word = list(filter(lambda ch: ch[0].isupper(), words))
        if len(upper_first_word) > 0:
            short_word = ''.join(map(lambda w: w[0], upper_first_word))
            acronym_word.append(short_word)
    return acronym_word


if __name__ == "__main__":
    amount = int(input())
    txts = [input() for _ in range(amount)]
    print(*sorted(sorted(acronym(txts)), reverse=True, key=len), sep='\n')
