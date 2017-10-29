# tornado_pyDBlite

A JSON API using tornado API. PyDBlite was used to create database purely on Python.
In order to install Tornado JSON:

    pip install Tornado-JSON

Then install pyDBlite

    pip install pydblite
    
Now you need to run the tornado server after cloning the file (helloworld.py file)

    python helloworld.py
    
Once the server is running, you will see the following data on the terminal

<img src=https://github.com/irtiq7/tornado_pyDBlite/blob/master/screenshot1.png>

Now on your web browser add url to access your database. Initially, the database will be empty so it would
not show anything.

    localhost:8888/getting_data/
    
 Enter the following command to add data into the database
 
    curl -v -H "Content-Type: application/json" -X POST -d "{ \"body\": \"Usama\",\"guid\": \"abc123\" }" http://localhost:8888/api/post_data/
    
Now refresh the browser to see the data

<img src=https://github.com/irtiq7/tornado_pyDBlite/blob/master/screenshot_2.png>

Now to delete a specific record from the database then use the record identifier to select and delete the specific record

    curl -v -H "Content-Type: application/json" -X POST -d "{ \"id\": 5 }" http://localhost:8888/api/delete_record/
