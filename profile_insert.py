import mysql.connector as sqltor

def special_char(string):
   for i in string:
      if i.isalpha() or i.isdigit():
         return True
      else:
         return False
         break

def name_pass(username_list):
   print("""
1. Username must not exceed 10 charecters
2. Username must not contain special charecters""")

   while True:
      username = input('New Username ')
      if len(username) <= 10 and username not in username_list and special_char(username):
         break
      else:
         if len(username) > 10:
            print('Invalid Username, more than 10 charecters')
         elif username in username_list:
            print('Username already exists')
         elif special_char(username) == False:
            print('Invalid username, special charecters must not be used')
   print("Password must be a 4 digit pin")

   while True:
      password = input('Enter a 4 digit pin ')
      if len(password) == 4 and password.isdigit():
         password = int(password)
         break
      else:
         print('Invalid password, try again')
   return (username, password)

def profile_insert_main():
   connection = sqltor.connect(host = 'localhost', user = 'root', passwd = '', database = 'game_data')
   cur = connection.cursor()
   query="SELECT * FROM login_data"
   cur.execute(query)
   username = [row[0] for row in cur]
   uname,password = name_pass(username)
   query = f'insert into login_data values("{uname}",{password})'
   cur.execute(query)
   connection.commit()
   print('An account has been made.')
   connection.close()

if __name__ == '__main__':
   profile_insert_main()
