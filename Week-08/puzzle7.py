sentence = "IF YOU COPY THIS SENTENCE TWO AND REMOVE ALL WORDS WITH LETTER IN IT WHAT WILL THOUSANDTH WORD BY WORD "

full_sentence = sentence * 200

split_full_sentence = full_sentence.split()

print(split_full_sentence[999] + split_full_sentence[99])