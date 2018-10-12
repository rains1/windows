from hero import Hero

def main():
    h1=Hero(200,5,"Tom")
    h2 = Hero(150, 10, "Lucy")
    h1.attackFun(h2)
    h2.attackFun(h1)

if __name__=="__main__":
    main()