item, qntd = map(int, input().split())
valor = 0.0
match item:
    case 1:
        valor = 4.00
    case 2:
        valor = 4.50
    case 3:
        valor = 5.00
    case 4:
        valor = 2.00
    case 5:
        valor = 1.50
    
total = valor * qntd
print(f"Total: R$ {total:.2f}")
        