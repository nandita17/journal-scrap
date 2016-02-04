import urllib2
from bs4 import BeautifulSoup

def ieee_authors(link):

    authors = []
    try:
        page = urllib2.urlopen(link).read()
        soup = BeautifulSoup(page, 'html.parser')
        
        metas = soup.find_all("meta", attrs={"name": "citation_author"})

        for meta in metas:
            if meta['name'] == 'citation_author':
                authors.append(meta['content'])
    except:
        pass

    print "[DEBUG] ", authors
    return


def acm_authors(link):

    authors = []
    try:
        page = urllib2.urlopen(link).read()
        soup = BeautifulSoup(page, 'html.parser')
        
        metas = soup.find_all("meta", attrs={"name": "citation_authors"})

        for meta in metas:
            if meta['name'] == 'citation_authors':
                authors.append(meta['content'])
    except Exception,e:
        print "Error", str(e) 

    print "[DEBUG] ", authors
    return



def springer_authors(link):
     
    authors = []
    try:
        page = urllib2.urlopen(link).read()
        soup = BeautifulSoup(page, 'html.parser')
       
        metas = soup.find_all("meta", attrs={"name": "citation_author"})

        for meta in metas:
            authors.append(meta['content'])
    except :
        pass 

    print "[DEBUG] ", authors
    return


ieee_authors("http://ieeexplore.ieee.org/xpl/abstractAuthors.jsp?tp=&arnumber=6196220");
acm_authors("http://dl.acm.org/citation.cfm?id=1281239");
springer_authors("http://link.springer.com/article/10.1007/s11709-015-0311-0");

