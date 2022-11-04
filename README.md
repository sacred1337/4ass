# 4ass
# NFT Aggregator
**NFT Aggregator** - with the usage of our database, allow people to find the information about NFT, and if there is no information in the db, it will search it in the Solana web service
The information is sent to the database using an API request of SolanaAPI and then the information is displayed on the site. 
The program itself runs in Python. Connecting to a Postgres database (Pg admin4). We also use html, css, bootstrap for the site.

### Installation
- Python: Install the current version of Python: VSCode
- Version: 2022.2.3 Assembly: 222.4345.23 October 16, 2022
- Postgres: Pg Admin 4
- Version 6.1 (4280.88)
- install postgress and open nft_db
- Terminal in VSCode:

	- pip install psycopg2
	- pip install flask
	- pip install requests
	- pip install flask-request

### In PgAdmin4:
1. Open the PostgreSQL 13 and CREATE NEW DATABASE and CALL IT "nft_db"".
2. Open the PyProject_db database >>> Schemas >>> Tables >> right mouse button and click Query Tool >>> Query Editor.
3. Paste following: 

CREATE TABLE users (
  id serial PRIMARY KEY,
	mail VARCHAR ( 100 ) NOT NULL,
	username VARCHAR ( 50 ) NOT NULL,
  pass1 VARCHAR ( 255 ) NOT NULL)
  
  AND 
  
  CREATE TABLE nft (
  address  VARCHAR ( 2000 ) NOT NULL,
  info  VARCHAR ( 2000 ) NOT NULL,)

### Usage
Spec It API Documentation:

url = f'https://solana-gateway.moralis.io/nft/mainnet/' + address + '/metadata'
headers = {"accept": "application/json",
           "X-API-Key": "u8emWI08OHGRqpKRzmO3Y3gW4OhbTdOdVRuJobooGeSvYRGjep6bmjuIDVu8RqEI"}
response = requests.get(url, headers=headers)

### Example:

#### Input:2FE7HdBq9F8LtUsoq8r2hpEAGa2Uz6Dd5XoKscewFg8y 
#### Output: infp: {"mint":"2FE7HdBq9F8LtUsoq8r2hpEAGa2Uz6Dd5XoKscewFg8y","standard":"metaplex","name":"y00ts: mint t00b #13806","symbol":"t00b","metaplex":{"metadataUri":"https://metadata.y00ts.com/t/13806.json","updateAuthority":"yootn8Kf22CQczC732psp7qEqxwPGSDQCFZHkzoXp25","sellerFeeBasisPoints":0,"primarySaleHappened":0,"owners":[{"address":"yootn8Kf22CQczC732psp7qEqxwPGSDQCFZHkzoXp25","verified":1,"share":100}],"isMutable":true,"masterEdition":false}}

### Examples for use:
Run main_app.py.
Click localhost in terminal, and and the program will open your browser. First of all, you will need to log in. If you
do not authorised in this website, you will have to register. And then only you can search NFTs.
After you logged in, you need to insert link of the chosen NFT and then click "Search".
After clicking on the site, information about your NFT that you have chosen earlier will be displayed.

### Team of the project:
*Yevgeniy Smagin*
*Satybaldiyev Emir*

