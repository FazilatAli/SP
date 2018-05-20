import requests
from bs4 import BeautifulSoup
def data(a,s):
	
	div_tag_list = []
	status1 = requests.get(a)
	if(status1.status_code == 200):
		parser_object = BeautifulSoup(status1.content,"html.parser")
		div_tag_list1 = list(parser_object.find_all('p'))
	
		for data in div_tag_list1:
                	data_find = data.text
			if s in data_find:
				print a
		
		
def getCategories(URL,s):
    if(URL != ""):
	try:
            status = requests.get(URL)

            if(status.status_code == 200):
               parser_object = BeautifulSoup(status.content,"html.parser")
               div_tag_list = parser_object.find('div',{'class':'full-div'})
	       div_tag_list1 = parser_object.find_all('div',{'class':'pp-new-thumb'})
	       
               for div in div_tag_list:
                   a_tag = div.find_all('a')
		   
                   for a in a_tag:
			link1 = (a['href'])
			data(link1,s)
			
	       count=0
	       for div in div_tag_list1:
                   a_tag = div.find_all('a')
		   
		   count = count+1
		   if count<=3:
		           for a in a_tag:
				link1 = (a['href'])
				data(link1,s)
				
	except requests.ConnectionError:
            print("ERROR OCCURED!!")
        


#___________________________#
def main():
    URL = "https://propakistani.pk/category/sports/"

    getCategories(URL,"The Pakistan Cricket Board ")
    


#___________________________#
if __name__ == "__main__":
    main()

