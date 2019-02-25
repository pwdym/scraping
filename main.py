import requests
from bs4 import BeautifulSoup
def main():
    list1=[]
    list2=[]
    print("Input the word you want to search->")
    word=input()
#test word skriapl
#Nikolai Glushkov
    url1='https://www.google.co.jp/search'
    url2='https://www.bing.com/search'
    req = requests.get(url1, params={'q': word})
    req1 =requests.get(url2, params={'q': word})
    url3=req.url
    url4=req1.url

    response = requests.get(url3)
    response.encoding = response.apparent_encoding

    response1=requests.get(url4)
    response1.encoding = response1.apparent_encoding

    bs = BeautifulSoup(response.text, 'html.parser')
    bs1 = BeautifulSoup(response1.text, 'html.parser')

    print("\nCase for Google\n")
    list1 = [i.getText() for i in bs.select("cite")]
    """for i in bs.select("cite"):
        list1.append(i.getText())
        #print(i.getText())
    """
    list1_in=[s for s in list1 if '/' in s and '.' in s or 'www' in s and not 'videos' in s and not 'images' in s]
#print(list1_in)
    for i in range(len(list1_in)):
        print("".join(list1_in[i]))
        print('\n')


    print("\n\nCase for Bing\n")
    list2 = [i.getText() for i in bs1.select("cite")]
    """for i in bs1.select("cite"):
    list2.append(i.getText())
    #print(i.getText())
    """
    print('\n')
    list2_in=[t for t in list2 if (('/' in t and '.' in t) or 'www'in t )  and not ('videos' in t and not 'images' in t)]
    for i in range(len(list2_in)):
        print("".join(list2_in[i]))
        print('\n')
#print(list2_in)


    list3=list1_in+list2_in
    print("\n\n")

#list_uni=list(set(list3))
    list_uni = set(list3)
    list_uni = list(list_uni)

    for i in range(len(list_uni)):
        print("".join(list_uni[i]))
        print('\n')
        """list3=list1+list2
        list4=set(list3)
        print(list4)
        """

if __name__ == "__main__":
    main()
