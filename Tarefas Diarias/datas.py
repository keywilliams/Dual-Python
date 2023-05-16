from datetime import datetime

diaDoAno = "2013-12-25"

print(type(diaDoAno))

diaDeNatal = datetime.strptime(diaDoAno, "%Y-%m-%d")

print(type(diaDeNatal))


print("Ano:", diaDeNatal.year)
print("Mês:", diaDeNatal.month)
print("Dia:", diaDeNatal.day)
