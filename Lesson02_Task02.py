"""
Lesson02 Task02.

The English language has five vowels: A, E, I, O, and U
Please count each vowel occurence in text bellow
( sum of lower and capital cases)
and write output as table smth like this
-----------------
| vowel | count |
-----------------
|   a   |  11   |
|   e   |  23   |
  ...
-----------------

then modify text where each vowel replaced with
A->À;  a->à ; E-> É ; e->é; I->Í , i->í ; O->Ó ; o->ó; U->Ú; u->ú
ex. "Í wàndéréd lónély...."   and print it
"""

poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

vowels = {
    'a': 'à',
    'e': 'é',
    'i': 'í',
    'o': 'ó',
    'u': 'ú',
}

sep_num = 17
print('-' * sep_num)
print(f"| {'vowel | count':^5} |")
print('-' * sep_num)

for val1, val2 in vowels.items():
    print(f'| {val1:^5} | {poem_text.lower().count(val1):^5} |')
    poem_text = poem_text.replace(val1, val2)
    poem_text = poem_text.replace(val1.upper(), val2.upper())
print('-' * sep_num)
print(f'Poem Text:\n{poem_text}')
