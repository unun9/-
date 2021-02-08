state={
    "1":" "

}
wins = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
def bot():
    player_numbers=[]
    for k in state:
        if[str(k)]=='x':
            player_numbers.append(int(k))
    print(player_numbers)
    xod_set={}
    for j in wins:
        set_player=set(set_player)
        xod_set =j-set_player
        print(xod_set)
        if len(xod_set)==1:
            xod_list=list(xod_set)
            print(xod_list[0])
            return xod_list[0]

    print(xod_set)

    player_numbers2 = []
    for k in state:
        if [str(k)] == 'o':
            player_numbers2.append(int(k))
    print(player_numbers2)
    xod_set = {}
    for j in wins:
        set_player = set(set_player)
        xod_set = j - set_player
        print(xod_set)
        if len(xod_set) == 1:
            xod_list = list(xod_set)
            print(xod_list[0])
            return xod_list[0]

    print(xod_set)


bot()