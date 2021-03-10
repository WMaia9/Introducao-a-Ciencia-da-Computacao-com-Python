segstr = input("Por favor, entre com o número de segundos que deseja converter: ")

segundos = int(segstr)

dias = segundos//86400
rdias = segundos % 86400
horas = rdias//3600
rhoras = rdias % 3600
minutos = rhoras // 60
segundos = rhoras % 60

print(dias,"dias,",horas,"horas,", minutos,"minutos e",segundos,"segundos")