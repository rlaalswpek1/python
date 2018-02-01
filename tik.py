from urllib.request import urlopen
from bs4 import BeautifulSoup

url = 'http://movie.daum.net/moviedb/grade?movieId=94074&type=netizen&page=1'

webpage = urlopen(url)

source = BeautifulSoup(webpage, 'html5lib')
reviews = source.find_all('p', {"class":"desc_review"})

for review in reviews :
	print(review.get_text().strip())