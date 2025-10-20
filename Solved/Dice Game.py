ga1, gb1, ga2, gb2 = map(int, input().split())
ea1, eb1, ea2, eb2 = map(int, input().split())
Emean = ((ea1 + eb1) / 2 ) + ((ea2 + eb2) / 2 )
Gmean = ((ga1 + gb1) / 2 ) + ((ga2 + gb2) / 2 )

if Emean > Gmean:
    print("Emma")
elif Gmean > Emean:
    print("Gunnar")
else:
    print("Tie")