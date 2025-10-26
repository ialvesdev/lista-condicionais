hi, mi, hf, mf = map(int, input().split())
inicio = hi * 60 + mi
fim = hf * 60 + mf

if fim <= inicio:
    fim += 24 * 60

duracao = fim - inicio
horas = duracao // 60
minutos = duracao % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
