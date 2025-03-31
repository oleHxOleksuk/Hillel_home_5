import string
import textwrap

#str_need_hashtag = 'Python, i. Community.!'
#str_need_hashtag = 'i like python community!'
str_need_hashtag = 'Should, I. subscribe? Yes!'

str_need_hashtag = str_need_hashtag.title().replace(' ', '')
for i in str_need_hashtag:
    if i in string.punctuation:
        str_need_hashtag = str_need_hashtag.replace(i, '')
str_need_hashtag = '#'+str_need_hashtag
str_hashtag = textwrap.shorten(str_need_hashtag, width=140, placeholder='')
print(str_hashtag)






