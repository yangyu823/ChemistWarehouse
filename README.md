#   PriceTrackingHouse

- [ ]   __No.1    ChemistWarehouse__
    - [x]   Stage Zero  (Preparation & Design)

    - [x]   Stage One   (Basic back-end functionality)
    
        - [x] Database Design & Setup
        - [x] Check Individual Product price
        - [x] Store Product Info into DB with timestamp
    
    - [ ]   Stage Two   (Basic API functionality)
        - [ ] Flask/Django(lib) setup for API back-end
        - [ ] `[API_1]` single function with request link
            - [ ] 1.Link check to decide which website it is
            - [ ] 2.Search from database to decide output
            - [ ] 3.Return product basic information
            - [ ] 4.Return history product price dataset
    - [ ]   Stage Three   (Website and Database host on cloud)
        - [ ] Heroku Database setup
        - [ ] Basic Frontend portal
            - [ ] Design phase
        - [ ] Travis CI integration and auto deploy to Heroku
        
    - [ ]   Stage Four (Back-end Polish and Automation)
    
        - [ ] Price Check mechanism automation(Daily Price Check)
        - [ ] `[API_2]` for History low price
        - [ ] `[API_1]` Price dataset from All vendor
        
    - [ ]   Stage Five  (Front-end Polish and D3js)
        - [ ] Line graph to demo the price history
        - [ ] Front-end the product page
- [ ]   __No.2    Other website Price Add-on__
    - [ ]   Supplements website (Eg.MyChemist,PriceLine etc)
    - [ ]   Makeup website
    - [ ]   Supermarket (Eg.Coles, WoolWorth etc)
    - [ ]   To be continue

``python manage.py runserver 9999``

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

