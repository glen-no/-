from path_of_story import *
player_name = input('назови его:')
print(f'''Вы-{player_name} великий пьяница ваша цель всего одна напится до лошадей в голове.
      Недалеко проходит турнир пьяниц и вы желаете сразится в алкагольной дуэли с другими пьяницами ''')
NAME = player_name
n = 1 

while n==1:
      
       print(f'ваше здоровье-{info_player["hp"]}')
       choise2= input('''sleep-1 or driking-2: ''')
       if choise2=='1':
            print('you sleep and feels a little healthy')
            info_player['hp']= 1000
       elif choise2=='2':
            play()
            choise = input('''            хотите продолжить играть? 
            (да=Y нет=N):  ''')
            if choise=='Y':
                  n +=0
            elif choise =='N':
                  n-=1
