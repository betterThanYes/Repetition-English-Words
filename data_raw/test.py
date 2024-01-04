import inflect
p = inflect.engine()
plural_word = ""
singular_word = p.singular_noun(plural_word)
if singular_word:
    print("OKE")
    print(singular_word)
else:
    print(plural_word)