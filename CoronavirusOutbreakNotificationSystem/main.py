from plyer import notification
import requests
from bs4 import BeautifulSoup


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=10,
        app_icon=None
    )


def getData(url):
    return requests.get(url).text  # get data from url and return it


if __name__ == "__main__":
    #notifyMe("Vishakha", "Lets stop the spread of the virus")
    myHtmlData = getData("https://www.mohfw.gov.in/")
    # print(myHtmlData)
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    soup.prettify()
    tableData = str(soup.find_all('table')[0]).split("\n")
    newdata = ""
    for i in tableData:
        if i == '<!--<tbody>':
            # print(tableData.index(i))
            tableData.remove(i)
            tableData.insert(14, "<tbody>")
    tableData2 = tableData[16:]
    str2 = ""
    for i in tableData2:
        str2 += i
    str3 = str2.replace("<td>", "").replace("</td>", "").replace("</tr>", "").replace("<tr>", "")
    States = ["Andhra Pradesh", "Delhi"]  #need notifications only for these states
    for z in (str3.split("		"))[0:62]:
        if States[0] in z:    #only for Andra Pradesh
            notificationTitle = "Cases of covid 19"
            notificationText = f"{States[0]}: {z[-3]}"
            notifyMe(notificationTitle, notificationText)
        #print(z.strip())

