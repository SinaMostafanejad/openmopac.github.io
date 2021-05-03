# Crawl the list of keywords on the MOPAC website [http://openmopac.net/manual/allkeys.html]
import requests
import re
import pypandoc

# download the text of the MOPAC keyword website
mopac_path = 'http://openmopac.net/manual/'
keywords_html = requests.get(mopac_path+'allkeys.html').text

# get keyword blocks split by <TR> or <tr>
keywords_split = re.split(r'<tr>', keywords_html, flags=re.IGNORECASE)
keywords_split.pop(0)

# identify the name, nickname, address, & description for each keyword
keywords_list = []
for keyword_line in keywords_split:
    keyword_split = re.split(r'<TD[ a-zA-Z0-9:=%"]*>', keyword_line)
    keyword = keyword_split[1]
    description = keyword_split[2]
    for string in re.split(r'"',keyword):
        if re.search(r'html', string):
            address = string
    if re.search(r'DEBUG PULAY', keyword):
        keyword = 'DEBUGPULAY' # the space in this keyword is erroneous
    if re.search(r'pKa', keyword):
        keyword = 'PKA' # the capitalization of this keyword is erroneous
    keyword = re.sub(r'[\n\t\r]|<[ a-zA-Z0-9:;/=.,%_\#\-"\']*>', '', keyword)
    description = re.sub(r'[\n\t\r]|<[ a-zA-Z0-9:;/=.,%_\#\-"\']*>', '', description)
    nickname = re.split(r'[ ,=\(]', keyword)[0]
    keywords_list.append([nickname, address, description])

# alphabetize keywords (they are slightly out of order)
keywords_list.sort()

# post-sorting keyword swaps to avoid filename problems
for i in range(len(keywords_list)):
    keywords_list[i][0] = re.sub(r'\*', 'star', keywords_list[i][0])
    keywords_list[i][0] = re.sub(r'\+', 'plus', keywords_list[i][0])
    keywords_list[i][0] = re.sub(r'&amp;', 'ampersand', keywords_list[i][0])
    keywords_list[i][0] = re.sub(r'\.', 'dot', keywords_list[i][0])

# add keywords to the glossary
glossary = open('../source/glossary.txt', 'w')
nickname_length = 0
description_length = 0
for (nickname, address, description) in keywords_list:
    nickname_length = max(nickname_length, len(nickname))
    description_length = max(description_length, len(description))

glossary.write(('='*(nickname_length+7))+'  '+('='*description_length)+'\n')
for (nickname, address, description) in keywords_list:
    glossary.write(f':ref:`{nickname}`')
    glossary.write(' '*(2 + nickname_length - len(nickname)))
    glossary.write(description+'\n')
glossary.write(('='*(nickname_length+7))+'  '+('='*description_length)+'\n')
glossary.close()

# add keywords to pages associated with their first character
letters = ['num', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
j = 0
for i in range(27):
    letter_file = open(f'../source/keywords/list_{letters[i]}.rst', 'w')
    if letters[i] != 'num':
        letter_file.write(letters[i])
    else:
        letter_file.write('#')
    letter_file.write('\n-\n\n.. toctree::\n\n')
    while j < len(keywords_list) and ((i == 0 and keywords_list[j][0][0] != 'A') or keywords_list[j][0][0] == letters[i]):
        letter_file.write(f'  {keywords_list[j][0]}\n')
        j += 1
    letter_file.close()

# convert each keyword webage to an rst file & add a reference to the top
for (nickname, address, description) in keywords_list:
    keyword_file = open(f'../source/keywords/{nickname}.rst', 'w')
    keyword_html = requests.get(mopac_path+address).text
    keyword_rst = pypandoc.convert_text(keyword_html, 'rst', format='html')
    keyword_file.write(f'.. _{nickname}:\n\n')
    keyword_file.write(keyword_rst)
    keyword_file.close()
