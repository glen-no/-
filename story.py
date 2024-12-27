from path_of_story import *
player_name = input('назови его:')
print(f'''Вы-{player_name} великий пьяница ваша цель всего одна напится до лошадей в голове.
      Недалеко проходит турнир пьяниц и вы желаете сразится в алкагольной дуэли с другими пьяницами ''')
NAME = player_name
n = 1 

while n==1:
      
       print(NAME)
       print(f'ваше здоровье-{info_player["hp"]}')
       print(f'опыт:{info_player["exp"]}/{max["max"]} уровень-{info_player["lvl"]}')
      
       choise2= input('''
sleep-1 
driking-2
gym-3
inventory-4
menu-5: ''')
       if choise2=='1':
            print('you sleep and feels a little healthy')
            print()
            info_player['hp']= 1000
       elif choise2=='2':
            play()
       elif choise2== '3':
             print('biba') 
             sleep(10)   
             print()
       elif choise2=='4':
             print('biba')  
             sleep(10) 
             print()       
       elif choise2=='5':     
            choise = input('''            хотите продолжить играть? 
            (да=Y нет=N):  ''')
            if choise=='Y':
                  n +=0
            elif choise =='N':
                  n-=1
