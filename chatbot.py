print('1.Hva heter jeg')
print('2.Hvor gammel er jeg')
print('3.Hobbyer')
print('4.Tekoologier jeg har jobbet med')
print('5.Exit')
valg = 0
while valg == 0:
    valg = int(input('Hva vil du vite om meg? '))


    if valg ==1:
        print('Jeg heter Jakub')
        valg = 0
    elif valg ==2:
        print('Jeg er 18')
        vlag = 0
    elif valg ==3:
        print('Spill og programmering ')
        valg = 0
    elif valg ==4:
        print('Python, c#, unity, PHP, mysql')
        valg = 0
    elif valg == 5:
        exit()