import requests
from bs4 import BeautifulSoup  


url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
rq = requests.get(url)

r_html = rq.text

print(r_html)
soup = BeautifulSoup(r_html)

#<p class="paywall">The main reason I had agreed to participate in the program was not to rehash or revise the story line of Interngate but to try to shift the focus to meaningful issues. Many troubling political and judicial questions had been brought to light by the investigation and impeachment of President Bill Clinton. But the most egregious had been generally ignored. People seemed indifferent to the deeper matters at hand, such as the erosion of private life in the public sphere, the balance of power and gender inequality in politics and media, and the erosion of legal protections to ensure that neither a parent nor a child should ever have to testify against each other.</p>
#<p class="Paragraph_text-SqIsdNjh0t0- paywall" data-component="paragraph">Izzy Englander’s Millennium Management set up there recently and now has a staff of more than 70, according to a person familiar with the matter, who asked not to be identified discussing non-public information.</p>

long_test = soup.find_all('p', {'class' : 'paywall'})

print(long_test)

#with open('text.txt', 'w') as new_file:
#    new_file.write("long_test")










