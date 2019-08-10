#   PriceTracker_Backend

- [ ]   __No.1    ChemistWarehouse__
    - [x]   Stage Zero  (Preparation & Design)

    - [x]   Stage One   (Basic back-end functionality)
    
        - [x] Database Design & Setup
        - [x] Check Individual Product price
        - [x] Store Product Info into DB with timestamp
        - [x] Function to return product info and price history
    
    - [x]   Stage Two   (Basic API functionality)
        - [x] <s>Flask</s>/Django(lib) setup for API back-end
        - [x] `[API_1]` single function with request link
            - [x] 1.Link check to decide which website it is
            - [x] 2.Search from database to decide output
            - [x] 3.Return product basic information
            - [x] 4.Return history product price dataset
    - [ ]   Stage Three   (Website and Database host on cloud)
        - [ ] Heroku Database setup
        - [x] Basic Frontend portal
            - [x] Design phase
        - [ ] AWS manual deploy 
            - [x] DNS , EC2 and Nginx setup
            - [ ] DB preparation
            - [ ] Backend Env & Code Setup
            - [ ] Frontend Env & Code Setup
            - [ ] HTTPS & Certificate setup
        - [x] <s> Travis CI integration and auto deploy to Heroku </s>
        
    - [ ]   Stage Four (Back-end Polish and Automation)
    
        - [ ] Price Check mechanism automation(Daily Price Check)
        - [ ] `[API_2]` for History low price
        - [ ] `[API_1]` Price dataset from All vendor
        
    - [ ]   Stage Five  (Front-end Polish and D3js)
        - [x] Line graph to demo the price history
        - [ ] Front-end the product page
- [ ]   __No.2    Other website Price Add-on__
    - [ ]   Supplements website (Eg.MyChemist,PriceLine etc)
    - [ ]   Makeup website
    - [ ]   Supermarket (Eg.Coles, WoolWorth etc)
    - [ ]   To be continue

``python manage.py runserver 9999``
Normal Run


``nohup python manage.py runserver 9999 &``
Run at background

Option:
Adding Firebase login with Company

####API address&port:
``http://127.0.0.1:9999/api/``  Main API

Passing URL to get product info and price history

``http://127.0.0.1:9999/testGet/`` Test Get API(Return ``Hello world``)

``http://127.0.0.1:9999/testPost/`` Test Post API(Return ``PostBody``)

``http://127.0.0.1:9999/update/`` (GET)Update database (Return ``UpdateList``)

***

### DataBase Structure:

###price_db.product_cat

| id   | product-id   | vendor  | name  | last_update  | link  | link_id  | prod_img  |
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |   
| INT  ­ ­ ­ ­  | INT  ­ ­ ­ ­  | VARCHAR(255)  ­ ­ ­ ­ ­  | VARCHAR(255)  ­ ­ ­ ­  | DATE  ­ ­ ­ ­ | VARCHAR(255)  ­ ­ ­ ­ | INT  ­ ­ ­ ­ | VARCHAR(255  ­ ­ ­ ­ | 

###price_db.product_history

| id   | product-id   | vendor  | name  | price  | date  | image  | 
| -------- | -------- | -------- | -------- | -------- | -------- | -------- | 
| INT  ­ ­ ­ ­  | INT  ­ ­ ­ ­  | VARCHAR(255)  ­ ­ ­ ­ ­  | VARCHAR(255)  ­ ­ ­ ­  | DOUBLE  ­ ­ ­ ­  | DATE  ­ ­ ­ ­  | LONGBLOB  ­ ­ ­ ­  | 


`imgae store as BLOB(binary). This is for price record evidence`

