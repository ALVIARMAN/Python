def fun():
    #formate specifier  print(f"{placeholder}) {variable:formate specifier}
    var1 = 3.8987
    var2 = -6.84344
    var3 = 44056.55

    print(f"var1 is{var1:.2f}")
    print(f"var2 is{var2:010.1f}") #alocate space/0 at front {var2:10}
    #print(f"var3 is {var3:<10}") #alocate space after value
    print(f"var3 is {var3:+,}") #1000 separate (,)

if __name__=="__main__":
    fun()