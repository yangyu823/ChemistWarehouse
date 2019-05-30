#   PriceTrackingHouse

- [ ]   **Project No.1    ChemistWarehouse**
    - [x]   Stage Zero  (Preparation & Design)

    - [ ]   Stage One   (Basic functionality)
    
        - [x] Database Design & Setup
        - [ ] Check Individual Product price
        - [ ] Store Product Info into DB with timestamp
        - [ ] Separate API to check Price base on request link
    
    - [ ]   Stage Two   (Website and Database host on cloud)
    
        - [ ] Heroku Database setup
        - [ ] Basic Frontend portal
        
            - [ ] Design phase
            
        - [ ] Travis CI integration and auto deploy to Heroku
        
    - [ ]   Stage Three (Back-end Polish and Automation)
    
        - [ ] Price Check mechanism automation(Daily Price Check)
        - [ ] To be continue
        
    - [ ]   Stage Four  (Front-end Polish and D3js)


- [ ]   __Project No.2    Formula Price Add-on__
    - [ ]   To be continue



***

### DataBase Structure:

####price_db.product_cat
| id   | vendor  | name  | last_update  |
| -------- | -------- | -------- | -------- | 
| cell 1  ­ ­ ­ ­  | cell 2  ­ ­ ­ ­ ­  | cell 3  ­ ­ ­ ­  | cell 4  ­ ­ ­ ­ |  
####price_db.price_history
| id   | vendor  | name  | price  | time  | image  | 
| -------- | -------- | -------- | -------- | -------- | -------- | 
| cell 1  ­ ­ ­ ­  | cell 2  ­ ­ ­ ­ ­  | cell 3  ­ ­ ­ ­  | cell 4  ­ ­ ­ ­  | cell 5  ­ ­ ­ ­  | cell 6  ­ ­ ­ ­  | 

`imgae store as BLOB(binary). This is for price record evidence`

