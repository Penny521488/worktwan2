from character import Character

player1 = Character("Toose", 185, 50, 5)
player2 = Character("Volodya", 200, 30, 30)
player3 = Character("Bulka barabulka" , 300 , 50 ,1)
player1.print_stats()
player2.print_stats()
player3.print_stats()

def battle(player1, player2):
    while player1.health > 0 and player2.health > 0:
        player1.attack(player2)
        if player2.health == 0:
            print(f"{player2.name} програв раунд в Realisics!")
            break
        player2.attack(player1)
        if player1.health == 0:
            print(f"{player1.name} програв раунд в Realisics!")
            break

battle(player1, player2)
