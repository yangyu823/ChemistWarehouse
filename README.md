#   PriceTrackingHouse

- [ ]   __No.1    ChemistWarehouse__
    - [x]   Stage Zero  (Preparation & Design)

    - [ ]   Stage One   (Basic back-end functionality)
    
        - [x] Database Design & Setup
        - [ ] Check Individual Product price
        - [ ] Store Product Info into DB with timestamp
    
    - [ ]   Stage Two   (Basic API functionality)
        - [ ] Flask(lib) setup for API back-end
        - [ ] API single function with request link
            - [ ] Return product price history
    - [ ]   Stage Three   (Website and Database host on cloud)
        - [ ] Heroku Database setup
        - [ ] Basic Frontend portal
            - [ ] Design phase
        - [ ] Travis CI integration and auto deploy to Heroku
        
    - [ ]   Stage Four (Back-end Polish and Automation)
    
        - [ ] Price Check mechanism automation(Daily Price Check)
        - [ ] To be continue
        
    - [ ]   Stage Five  (Front-end Polish and D3js)
- [ ]   __No.2    Formula Price Add-on__
    - [ ]   To be continue



***

### DataBase Structure:

###price_db.product_cat

| id   | vendor  | name  | last_update  | link  |
| -------- | -------- | -------- | -------- | -------- |  
| cell 1  ­ ­ ­ ­  | cell 2  ­ ­ ­ ­ ­  | cell 3  ­ ­ ­ ­  | cell 4  ­ ­ ­ ­ | cell 5  ­ ­ ­ ­ |    

###price_db.price_history

| id   | vendor  | name  | price  | time  | image  | 
| -------- | -------- | -------- | -------- | -------- | -------- | 
| cell 1  ­ ­ ­ ­  | cell 2  ­ ­ ­ ­ ­  | cell 3  ­ ­ ­ ­  | cell 4  ­ ­ ­ ­  | cell 5  ­ ­ ­ ­  | cell 6  ­ ­ ­ ­  | 

`imgae store as BLOB(binary). This is for price record evidence`

