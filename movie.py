from urllib.request import urlopen
from bs4 import BeautifulSoup

base_url = 'http://movie.daum.net/moviedb/grade?movieId=2725&type=netizen&page={}'

for n in range (77) :
	url = base_url.format(n+1)
	webpage = urlopen(url)
	source = BeautifulSoup(webpage, 'html5lib')
	reviews = source.find_all('p', {'class':'desc_review'})

	for reviews in reviews :
		print(reviews.get_text().strip())

review_list = []

...
...
...

for review in reviews :
	review_list.append(review.get_text().strip())

file = open('data1.txt', 'w', encoding = 'utf-8')

for review in review_list :
	file.write(review + '\n')

file.close()