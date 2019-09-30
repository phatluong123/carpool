# carpool

## General info
The user can carpool with others based on several factors given by the back end system such as similarity of route and traffic conditions. Using the app, a driver can enter his start and endpoints, or choose to ride with and the existing route which is most convenient for them.

	
## Technologies
Project is created with:\
bcrypt==3.1.7\
Django==1.10\
geocoder==1.38.1\
smartystreets-python-sdk==4.3.0

## Development
   	# Clone the repository
	
	# Install Django Virtual Environment
		virtualenv -p python3 djangoPy3Env
		
	# Activate Django Virtual Environment
		source djangoPy3Env/bin/activate
		
	# Install Django 
		pip install Django==1.10
		
    	# Change into project directory
    		cd <project_name>
    
    	# Make virtual environment
    		mkvirtualenv <project_name>
    
    	# Install requirements
    		pip install -r requirements.txt
    
    	# Start the development server
    		python manage.py runserver
    
## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.
