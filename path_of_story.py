import random
from time import sleep
info_player = {'hp':1000,'lvl':1,'сила печени': 5,'exp':0,'atack':5,'strench':10,'armor':25,'luck':10}
player_fight = {}
enemies = ([{'name':'Дядя_вася' ,'hp':100,'script':'Слабоват ты молокосос','scriptlose':'ЙК нало бутеть как то повторить','count':10}
            ,{'name':'Трудовик', 'hp':250,'script':'Слабовата твоя печень','scriptlose':'Ух неплохо покутили','count':10}
            ,{'name':'Отец','hp':1000,'script':'Тебе меня никогда не перепить','scriptlose':' Йк Невозможно Йк','count':10}])
drinks = [{'name':'Пиво','hp':50},{'name':'Джин','hp':100},{'name':'Водка','hp':200}]
snacks = [{'name':'чипсы','health':10},
          {'name':'сухарики','health':10},
          {'name':'рыба','health':100},
          {'name':'маринованые огурцы','health':100 },
          {'name':'оливье','health':500},
          {'name':'крабовый салат','health':500},
          {'name':'сыр','health':50},
          {'name':'картошка фри','health':50},
          {'name':'жареная курочка','health':150},
          {'name':'сырой картофель','health':-50}]
fight_enemies = [{'name':'nerd','hp':100,'atack':5,'strench':10,'armor':25,'luck':10,},
                 {'name':'normal','hp':250,'atack':10,'strench':20,'armor':50,'luck':10},
                 {'name':'bully','hp':500,'atack':15,'strench':30,'armor':75,'luck':10}]
max={'max':10}

def play():
    n = random.randint(0 , len(enemies)-1)
    n1 = random.randint(0, len(drinks)-1)
    n2 = random.randint(0, len(snacks)-1)
    n3 = random.randint(0, len(fight_enemies)-1)
    fun = random.choice(['pain','food'])
    info_enemy = (enemies[n])
    info_drink = (drinks[n1])
    fight = (fight_enemies[n3])
    snack = (snacks[n2])
    
    event = random.randint(0,11)
    

    enemies[0]["hp"]=100
    enemies[1]["hp"]=250
    enemies[2]["hp"]=1000

    if info_player['exp']==max['max']:
            info_player['lvl']+=1
            max['max']+=10
            info_player['сила печени'] = info_player['сила печени']*info_player['lvl']


    while (info_enemy['hp']>0) and (info_player['hp']>0):
        print(f'Собутыльник-{info_enemy["name"]},Напиток-{info_drink["name"]},(сила печени))-{info_player["сила печени"]}')
        

        info_enemy['hp'] -=info_drink['hp']
        info_player ['hp'] -=(info_drink['hp']-info_player['сила печени'])
        print(f'''      урон от напитка-{info_drink["hp"]} 
        Ваше HP-({info_player["hp"]}),HP противника-({info_enemy["hp"]})''')
        sleep(0.5)
        print()
    if (info_enemy['hp']<=info_player['hp']):
        print(f'''            you win
     {info_enemy["name"]}-({info_enemy["scriptlose"]})''')
        info_player['exp']+=1
        info_enemy['count']-=1
    else:
        print(f'''           you lose
     {info_enemy["name"]}-({info_enemy["script"]})''')
        
    if event <=5:
     print('''СЛУЧАЙНОЕ СОБЫТИЕ ''')
     if fun =='food':
      print(f'you ate {snack["name"]}')
      info_player['hp'] += snack['health']
     elif fun=='pain':
      print('На вас напали')
      while info_player['hp'] and fight['hp']>=0:
         print(f'ваше здоровье-{info_player["hp"]},здоровье({fight["name"]})-{fight["hp"]}')
         info_player['hp']-= (fight['atack']*fight['strench'])-info_player['armor']*0.1
         fight['hp']-= (info_player['atack']*info_player['strench'])-fight['armor']*0.1
         if info_player['hp']<=0:
           print('you lose')
         elif fight['hp']<=0:
          print('you win')

   
    
