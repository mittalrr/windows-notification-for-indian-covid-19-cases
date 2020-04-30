from plyer import notification 
import requests
from bs4 import BeautifulSoup
import time



def notifyMe(title, message):
	notification.notify(
		title = title,
		message = message,
		app_icon = "C://Covid//icon_ico.ico", 
		# app_icon = None,
		timeout = 5
		)

def getDatafrom(url):
	r = requests.get(url)
	return r.text


if __name__ == "__main__":
	while True:
		# notifyMe("Mittal", "Lets stop the spread of this virus together")
		myHtmlData = getDatafrom("https://www.mohfw.gov.in/")
		# print(myHtmlData)
		soup = BeautifulSoup(myHtmlData, 'html.parser')
		# print(soup.prettify())
		myDatastr = ""
		for tr in soup.find_all('tbody')[0].find_all('tr'):
			myDatastr += tr.get_text()
			# print(myDatastr)
			# print(table)
			# print(tr.get_text())
			# http://example.com/elsie
			# http://example.com/lacie
			# http://example.com/tillie
		# print(myDatastr.split("\n\n"))	
		myDatastr = myDatastr[1:]
		itemlist = myDatastr.split("\n\n")

		states = ['Maharashtra', 'Gujarat', 'Chandigarh', 'Telengana', 'Uttar Pradesh']

		for item in itemlist[0:33]:
			# print(item.split("\n"))
			dataList = item.split("\n")
			# print(dataList)
			# print(len(dataList))
			if dataList[1] in states:
				print(dataList)
				ntitle = 'Cases of Covid-19'
				# ntext = f"STATE: {dataList[1]}: Indian_cases: {dataList[2]} \nForeign: {dataList[3]} \nCured: {dataList[4]} \nDeaths: {dataList[5]}"
				ntext = f"State : {dataList[1]} \nConfirmed : {dataList[2]} \nCured : {dataList[3]} \nDeaths : {dataList[4]}"
				notifyMe(ntitle, ntext)
				time.sleep(2) #sleep time for intra notifications i.e between consecutive notification within a cycle
		time.sleep(10)  # sleep time for inter notifications i.e between one notification cycle & another