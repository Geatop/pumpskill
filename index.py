from pprint import pprint
from dataset import users, countries

# #point 1
users_wrong_password = []
# pprint(users)
for user in users:
    for passwords in user:
        if 'password' in passwords:
            try:
                password = int(user['password'])
                if type(password) == int:
                    info = {}
                    info['name'] = user['name']
                    info['mail'] = user['mail']
                    users_wrong_password.append(info)
                else:
                    pass              
            except Exception as e:
                pass
        else:
          pass
# pprint (users_wrong_password)

#point 2
girls_drivers = []

# pprint (users)
for friends in users:
   for friend in friends:
        try:
            if friend in 'friends':
               for fri in friends['friends']:
                    if 'cars' in fri and fri['sex'] == 'F':
                        girls_drivers.append(fri['name'])
#                      # if fri['sex'] == 'F':
#                      #    for cars in friends['friends']:
#                      #       for car in cars:
#                      #          if 'cars' in car:
                           
#                      #             girls_drivers.append(fri['name'])
#                      #          else:
#                      #             pass
#                      # else:
#                      #    pass
                    else:
                        pass
            else:
               pass
                     
        except Exception as q:
            pass
# pprint (girls_drivers)

#point 3

best_occupation = {'occupation': 'безработный', 'salary': 0}
# pprint (users)

for user in users:
   for friends in user:
      if 'friends' in friends:
         for friends_job in user['friends']:
            for salary in friends_job['job']:##############################
               a = friends_job.get('job')
               b = a.get('salary')
               if b > best_occupation.get('salary'):
                  best_occupation = a
               # if 'job' in salary:
               #    for job in friends_job['job']:   
               #       try:   
               #          if 'salary' == job:
               #             if friends_job['salary'] > best_occupation['salary']:
               #                best_occupation = friends_job['job']
               #             else:
               #                pass
               #          else:
               #             pass
               #       except Exception as k:
               #          pass# best_occupation = friends_job['job']
               #    else:
               #       pass
# print (best_occupation)

# # point 4
# pprint (users)
vip_user = 0
salary_friends = 0
max_value = 0 
for user in users:
    friends = user.get('friends', [])
    salary_friends = 0
    for joblist in friends:
        job = joblist.get('job',[])
        salary = job.get('salary',[])
        salary_friends += salary
        if max_value < salary_friends:
            max_value = salary_friends
            vip_user = user.get('name',[])       

    # if friends:
        # for friends in user:      
        #     if 'friends' in friends:
        #         z = c
        #         c = 0
        #         for friend in user['friends']:
        #             a = friend.get('job')
        #             b = a.get('salary')
        #             c += b
        #             if c > z:
        #                 vip_user = user.get('name')
# print (vip_user)

# point 5
# pprint(users)
travelers = 0
val_flights = 0

for user in users:
    friends = user.get('friends', [])
    for friends_with_cars in friends:
        cars = friends_with_cars.get('cars', [])
        if cars:
            travelers += 1
            val_flights += len(friends_with_cars.get('flights', []))
avg_flights =  round((val_flights/travelers),5)

# print(avg_flights)

            
        



# for user in users:
#     friends = user.get('friends')
#     try:
#         for friend in friends:
#             cars = friend.get('cars')
#             flights = friend.get('flights')
#             if cars != None and flights != None:
#                 travelers += 1
#                 val_flights += len(flights)

#     except Exception as p:
#         pass
# avg_flights = val_flights/travelers
# print (round(avg_flights, 5))
    # for friends in user:
    #     if friends == 'friends':
    #         if 'cars' in friends and 'flights' in friends:
    #             pass

# point 6

# pprint (users)
userscopy = users[:]

for user in userscopy:
    friends = user.get('friends')
    if friends:
        for fly in friends:
            flights = fly.get('flights')
            if flights:
                for strana in flights:
                    country = strana.get('country')
                    if country in countries:
                        try:
                            users.remove(user)
                            break
                        except Exception as c:
                            continue                    
    else:
        continue
    continue
        # # # for friends in user:
        # # #     if 'friends' == friends:
        # # #         friend = user.get('friends')
        # # #         try:
        # # #             for fly in friend:
        # # #                 flights = fly.get('flights')
        # # #                 if flights != None:
        # # #                     for flight in flights:
        # # #                         country = flight.get('country')
        # # #                         if country in countries:
        # # #                             users.remove(user)
        # # #                             flights = None
        # # #                             flight = None
        # # #                             user = 0
        # # #                             print ('===================================')
        # # #                             pprint(users)
        # # #                             continue
        # # #                 else:
        # # #                     pass
        # # #         except Exception as o:
        # # #             pass
        # # #     else:
        # # #         continue

# pprint (users)


