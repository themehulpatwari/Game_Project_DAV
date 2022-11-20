import mysql.connector as sqltor

def username_pass_check(username_dict):
   print('\nExisting Login Page')
   username = input("What's your username ")
   if username in username_dict:
      password = int(input('Give the pin '))
      if password == username_dict[username]:
         print('Login Successful.')
         return True
      else:
         print('Wrong Pin')
         return False
   else:
      print('Invalid Username')

def profile_pass_main():
   con = sqltor.connect(host = 'localhost', user = 'root', passwd = '', database = 'game_data')
   cur = con.cursor()
   query="SELECT * FROM login_data"
   cur.execute(query)
   username_dict = {}
   for i,j in cur:
      username_dict[i] = j

   return username_pass_check(username_dict)


if __name__ == '__main__':
   profile_pass_main()
