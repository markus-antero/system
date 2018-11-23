Main
====

The site meta-model visualized
	
How is the site linked together

	Graph / tree
		Linked based on 
			relation parent:child, 
			strength, 
			association.
				
		Classified based on domain
			External 
			Internal

	Taxonomy		
		People: 
			Linked-in
			* Who is visiting
				
		Terms: 
			Wikipedia
			Link to referred content in the site.
	
Who is visiting 
---------------
		
classify based on the association

* Linked site
* Linked person
* Visitor
	
Plot on a map, Based on 

* location: country, town, address.
* coordinates: Latitude, longlitude
			
Contains: provider info.io§

* Name
* Type: private individual / public entity
* Location: address
* Provider: Internet
* Linked to	
			
Technical implementation
========================	

Tier 1 
------
		
1. Goal: 	 			Refine the process, use minimal viable focus on producing the UI
2. Product: 			Semi-automated website extension. Provided as a subdomain.					
3. Time to implement:   1 Week (setup). Contains initial meeting / requirement analysis / data / legal agreement
4. Business Model: 		Platform as a Service
5. Subscription:		1 / 6 / 12 month(s) 
6. Client base: 		New and existing customers

Implementation:
	User interface:

	* Django 			(Python, javascript / ajax and html)
	* Dash/Plotly   	(Python)
					
	Database:
	
	* PostgreSQL		(Relational Database / SQL)
	* SQL Alchemy 		(Python)
					
	Data-modelling
	
	* Orange Canvas 	(Python)
					
	Data-mapping:
	
	* JSON / App  		(Python)
	* JSON / RDF 		(Ontology engine)
					
	External Tools
	
	* ArcGIS			(Python)
					
	Possible platform providers:
		
	* Amazon AWS
	* Digital Ocean
	* Google			
				
Tier 2
------

1. Goal:			 	Refine the UI, utilize virtual reality and 3D 
2. Product:				Independent application, requiring high level graphics card and PC, VR Helmet and tools, and place
3. Implementation:		1 month
4. Business Model:		Licence to a product
5. Client base:			existing customers; requires tier 1
			
Implementation:

* 3D engine
* Process defined in tier 1
				
Possible platform providers:

* Google 