import mysql.connector
import getpass
password = getpass.getpass(prompt="Password please:  ")
try:
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=password,
        database="World_Bank_Data"
    )
    print("Connected")
except Exception as e:
    print("Can't connect to database", e)

# my_cursor = my_db.cursor()


# my_cursor.execute('''CREATE TABLE IF NOT EXISTS company
#                      (ticker CHAR(4) NOT NULL,
#                       name VARCHAR(255) NOT NULL,
#                      CONSTRAINT PK_company PRIMARY KEY (ticker) )
#                  ''')
# my_cursor.execute('''CREATE TABLE IF NOT EXISTS major_holders
#                     (company_ticker CHAR(4) NOT NULL,
#                     shares_held_by_all_insider VARCHAR(10),
#                     shares_held_by_institutions VARCHAR(10),
#                     float_held_by_institutions VARCHAR(10),
#                     no_of_institutions_holding_shares VARCHAR(255),
#                     CONSTRAINT FK_major_holders_company FOREIGN KEY(company_ticker)
#                     REFERENCES company(ticker)
#
#                     ON DELETE CASCADE ON UPDATE CASCADE )
#                 ''')
#

# my_cursor.execute('''CREATE TABLE IF NOT EXISTS top_institutional_holders
#                     ( company_ticker CHAR(4) NOT NULL,
#                       holder VARCHAR(255),
#                       shares VARCHAR(2048),
#                       date_reported VARCHAR(25),
#                       percentage_out VARCHAR(10),
#                       value VARCHAR(2048),
#                       CONSTRAINT FK_t_i_h_company FOREIGN KEY (company_ticker)
#                       REFERENCES company(ticker)
#                       ON DELETE CASCADE ON UPDATE CASCADE )
#                   ''')
#
# my_cursor.execute('''CREATE TABLE IF NOT EXISTS insider_roster
#                     ( company_ticker CHAR(4) NOT NULL,
#                       individual_or_entity CHAR(50),
#                       role CHAR(40),
#                       recent_transaction VARCHAR(255),
#                       date VARCHAR(25),
#                       shares_owned_as_of_transaction_date VARCHAR(255),
#                       CONSTRAINT FK_insider_roster_company FOREIGN KEY(company_ticker)
#                       REFERENCES company(ticker)
#                       ON DELETE CASCADE ON UPDATE CASCADE )
#                  ''')
# my_cursor.execute('''CREATE TABLE IF NOT EXISTS insider_transactions_last_6months
#                      ( company_ticker CHAR(4) NOT NULL,
#                        actions VARCHAR(50),
#                        shares VARCHAR(25),
#                        transactions VARCHAR(10),
#                        CONSTRAINT FK_transactions_6months_company FOREIGN KEY(company_ticker)
#                        REFERENCES company(ticker)
#                        ON DELETE CASCADE ON UPDATE CASCADE
#                      )
#                  ''')
# my_cursor.execute('''CREATE TABLE IF NOT EXISTS net_purchases_prior_to_latest_quarter
#                      ( company_ticker CHAR(4) NOT NULL,
#                        actions VARCHAR(50),
#                        shares VARCHAR(25),
#                        CONSTRAINT FK_net_purchases_quarter_company FOREIGN KEY(company_ticker)
#                        REFERENCES company(ticker)
#                        ON DELETE CASCADE ON UPDATE CASCADE
#                      )
#                  ''')