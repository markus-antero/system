Main
====

Use the google or Amzon platform For the project:

1. Buid Link collector to formulate a tree for child-parent view and use classifier and inspect to collect the information.	
2. Store the records into pandas dataframe and then into SQL Server. utilize the item class to build the pandas dataframes.
3. Build a second spider to collect utility information.
4. Expand the search to surrounding domains. Look into:
	* linked-in 
	* Twitter 
	* wikipedia 

Steps 1 and 2 are needed first, steps 3 and 4 requires documentation
				
Key reason to backend solution is state.

Network for site
	Website title (ID)
		Nedlaw
		
	Domain 
		nedlaw.eu

	Internal websites
	External websites
	Menu linked websites
	
Owner for domain
----------------

* Name
* Email
* phone
* Linked-in - search name + company, email, phone 
* Twitter - phone or email

Wikipedia API
-------------

Terminology for domain
	Keyword
		Taxonomy
		'banking (3 items)',
        'business (2 items)',
        'cheat-sheet (3 items)',
        'climate (4 items)',
        'corruption (6 items)',
        'economics (11 items)',
        'election (6 items)',
        'law (16 items)',
        'media (10 items)',
        'politics (33 items)',
        'post-truth (8 items)',
        'programming (3 items)',
        'system (2 items)',
        'war (4 items)']  
			

Collectting Data
----------------

Brief collection of the libraries needed to provide a product.

Processing the meta-model for websites.  
			
"Scrapy is a fast high-level web crawling and web scraping framework, used to crawl websites and extract structured data from their pages. 
It can be used for a wide range of purposes, from data mining to monitoring and automated testing.".	
		
Scrapy
	https://scrapy.org/
				
		https://doc.scrapy.org/en/latest/topics/stats.html
		https://doc.scrapy.org/en/1.0/topics/spider-middleware.html
					

The first part of the problem is to collect the specific details in a relativly automated way and put the resuults in a database.
This stage might have more than one iteration.
The task has difficulty due to the relative unstructured nature of websites.
			
scrapy shell at nedlaw 
			
	Main menu items			 : response.xpath("//div[contains (@class, 'hs-menu')]/ul/li/a").extract()
				
		* Out[18]: 
		* ['<a href="https://www.nedlaw.eu/#hs-about-us-section">About</a>',
		* '<a href="https://www.nedlaw.eu/#hs-portfolio-section">Editorial</a>',
		* '<a href="https://www.nedlaw.eu/#hs-service-post-section">Identity</a>',
		* '<a href="https://www.nedlaw.eu/#hs-blog-section">Archive</a>',
		* '<a href="https://www.nedlaw.eu/#hs-contact-section">Contact</a>',
		* '<a href="https://www.nedlaw.eu/blog/">Blog</a>',
		* '<a href="https://www.nedlaw.eu/entrepreneurship/">Business</a>',
		* '<a href="https://nedlaw.eu/map/">Map</a>']

				
	Main menu, sub menu items: response.xpath("//div[contains (@class, 'hs-menu')]/ul/li[contains (@class, 'menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-2526')]/ul/li/a").extract()
					
		* Out[25]: 
		* ['<a href="https://www.nedlaw.eu/plan-of-business/">Plan of Business</a>',
		* '<a href=https://www.nedlaw.eu/theory-of-funnel/">Theory of Funnel</a>',
		* '<a href="https://www.nedlaw.eu/daily-operations/">Daily Operations</a>',
		* '<a href="https://www.nedlaw.eu/working-capital/">Working Capital</a>',
		* '<a href="https://www.nedlaw.eu/profiling/">Profiling</a>',
		* '<a href="https://www.nedlaw.eu/values/">Values</a>',
		* '<a href="https://www.nedlaw.eu/external-resources/">External Resources</a>']
					 
	Sub section response.xpath("//div[contains (@class, 'hs-service-excerpt')]/h6/a").extract()

		* Out[3]: 
		* ['<a href="https://www.nedlaw.eu/development/">Development</a>',
		* '<a href="https://www.nedlaw.eu/politics/">Political views</a>',
		* '<a href="https://www.nedlaw.eu/systems/">Systems</a>',
		* '<a href="https://www.nedlaw.eu/intelligence/">“Superior Intelligence”</a>',
		* '<a href="https://www.nedlaw.eu/idea-for-business/">Idea for Business</a>']
				 
	
Visualization
-------------

If collecting the data is the first problem, then the second problem is producing the information in visual-form.
This stage doesn't, however, address the issue of the method of producing the information.
			
This is dictated by the type of the visualization type.
Thus, it is the problem of chicken and egg.
Dash is light python based python platform for web based vizualization.
		
Dash py Plotly - https://plot.ly/products/dash/
			
	Tutorial tree
		* https://dash.plot.ly/
				
	Tree based visualization
		* https://github.com/plotly/dash-network
		* https://beta.observablehq.com/@mbostock/d3-force-directed-graph
					
	Dash Boiler-plate - ?
		* https://github.com/plotly/dash-component-boilerplate
					
					
Web-platform
		
	To mediate the visualization requires a platform.

	Dash and Django:

		* https://www.youtube.com/watch?v=QWZXJlhjgrs
	
	Django 
					
		Main documentation
				
			* https://www.djangoproject.com/
				
		Google
				
			Google Python-platform
				* https://cloud.google.com/python/docs/
						
			Getting Started With Django
				* https://cloud.google.com/python/django/
						
			Python Bookshelf App
				* https://cloud.google.com/python/getting-started/tutorial-app

	Django is a web-platform with the internel mechanics of defining a model.
	The model contains named variables.
			
The relationship is information produced is mirror the data-model for scrapy and Dash.
	Embed the Dash visualizations within Django.
	And use the modelling capabilities of Django to gather the information needed for each visualization.
				


Geo location Python
-------------------

* http://ipinfo.io/json

