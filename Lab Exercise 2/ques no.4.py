#If temperature is greater than 30,its hot day other wise if it is less than 10; its a cold day
# otherwise its neither hot nor cold day
temperature=int(input("enter the value of temperature"))
if temperature>30:
    print('Temperature is hot')
elif temperature<10:
    print('Its a cold day')
else:
    print(f"Its neither hot nor cold")