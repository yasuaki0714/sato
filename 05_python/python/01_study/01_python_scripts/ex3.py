while True:
    n = input("正の値を入力してください")
    if(n == "end"):
        print(n,"終了します")
        break
    try:
        n = float(n)
    except ValueError:
        print(n,"は数値に変換できません")
        continue
    except:
        print("予期していないエラーです")
        exit()
    if(n<=0):
        print(n,"は正の数値ではありません")
        continue

    def square_root(x):
        rnew = x
        diff = rnew - rnew/x
        if(diff < 0):
            diff = -diff
        while(diff/x > 1.0E-12):
            r1 = rnew
            r2 = x/r1
            rnew = (r1 + r2)/2
            diff = r1 - r2
            if(diff < 0):
                diff = -diff
        return rnew

    v = n
    r = square_root(n)
    print("平方根は", r, "です")