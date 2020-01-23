total_segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segundos1 = int(total_segundos)
a = total_segundos1 // 86400
b = (total_segundos1 % 86400) // 3600
c = ((total_segundos1 % 86400) % 3600) // 60
d = ((total_segundos1 % 86400) % 3600) % 60
print(a,"dias,",b,"horas,",c,"minutos e",d,"segundos.")
