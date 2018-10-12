class Hero:
    count=0
    def __init__(self,hp,attack,name):
        global count

        count+=1
        self.hp=hp
        self.attack=attack
        self.name=name
        print('玩家%s加入游戏，当前游戏人数为%d'%(self.name,self.count))

    def attackFun(self,player):
        player.hp-=self.attack
        print("玩家%s受到玩家%s的%d伤害，剩余hp为：%d"
              %(player.name,self.name,self.attack,player.hp))
