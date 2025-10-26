inicio = int(input().split()[1])
h, m, s = map(int, input().split(" : "))
fim = int(input().split()[1])
hf, mf, sf = map(int, input().split(" : "))
inicio_total = (inicio * 86400) + (h * 3600) + (m * 60) + s
fim_total = (fim * 86400) + (hf * 3600) + (mf * 60) + sf

duracao = fim_total - inicio_total

diastotais = duracao // 86400
resto = duracao % 86400
horastotais = resto // 3600
resto = resto % 3600
minutostotais = resto // 60
resto = resto % 60
segundostotais = resto

print(f"{diastotais} dia(s)")
print(f"{horastotais} hora(s)")
print(f"{minutostotais} minuto(s)")
print(f"{segundostotais} segundo(s)")