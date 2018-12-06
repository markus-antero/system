'''
The package
    Contains event triggered program fragments for spiders
    Each moddule is executed based on the order defind in settings.py
    Modules in this package contain either spider specific or general fragments
'''

hostname = 'localhost'
username = 'markus'
password = 'markus' 
database = 'webScraping'

inserIntoURLTable = '''insert into public.\"domainLocation\" 
                    (url, title, classifier, \"domain\", classifiertxt, parenturl) 
                    values(%s,%s,%s,%s,%s,%s)'''
                    
inserIntoWikiTable = '''insert into taxonomy
                        (terminology, wikiarticlename, wikiarticleurl) 
                        values(%s,%s,%s)'''

inserIntoInitTable = '''insert into service
                        (project, spider, servername, urlname, datetime) 
                        values(%s,%s,%s,%s,%s)'''

inserIntoOrgTable = '''INSERT INTO public.organization
                       ("domain", ip, organization, country, city, region, "location")
                       VALUES(%s,%s,%s,%s,%s,%s,%s);'''

inserIntoBlogTable = '''insert into blog
                        (headline, published, author, url)
                        values(%s,%s,%s,%s)
                     '''