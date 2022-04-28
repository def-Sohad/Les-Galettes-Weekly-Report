print("\t\t\tLes Galettes Weekly Report")

# Opening an Excel file to store our data.
with open("LGWR.csv","w") as file:
    file.write("Days,Manoushes Number,Bread Number,Date")
    
# Geting the date data from the user.
    year = int(input('the current year: '))
    month = int(input('the number of the current month: '))
    day = int(input('Enter the day number of only thursday: '))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
# Setting the day date for the rest of week.
    month_lst = [1,3,5,7,8,10,12]
    month_lst1 = [2,4,6,9,11]
    day1 = day + 1
    day2 = day + 2
    day3 = day + 3
    day4 = day + 4
    day5 = day + 5
    day6 = day + 6
    
    month1 = month
    month2 = month
    month2 = month
    month4 = month 
    month5 = month
    month6 = month
    
    date = str(month)+'/'+str(day)+'/'+str(year)
    date1 = str(month)+'/'+str(day1)+'/'+str(year)
    date2 = str(month)+'/'+str(day2)+'/'+str(year)
    date3 = str(month)+'/'+str(day3)+'/'+str(year)
    date4 = str(month)+'/'+str(day4)+'/'+str(year)
    date5 = str(month)+'/'+str(day5)+'/'+str(year)
    date6 = str(month)+'/'+str(day6)+'/'+str(year)
    
    if month == 2 and day == 28:
        month1 = month + 1 
        day1=1;day2=2;day3=3;day4=4;day5=5;day6=6
        date1 = str(month1)+'/'+str(day1)+'/'+str(year)
        date2 = str(month1)+'/'+str(day2)+'/'+str(year)
        date3 = str(month1)+'/'+str(day3)+'/'+str(year)
        date4 = str(month1)+'/'+str(day4)+'/'+str(year)
        date5 = str(month1)+'/'+str(day5)+'/'+str(year)
        date6 = str(month1)+'/'+str(day6)+'/'+str(year)
    elif month in month_lst and day == 31:
        month1 = month + 1
        day1=1;day2=2;day3=3;day4=4;day5=5;day6=6
        date1 = str(month1)+'/'+str(day1)+'/'+str(year)
        date2 = str(month1)+'/'+str(day2)+'/'+str(year)
        date3 = str(month1)+'/'+str(day3)+'/'+str(year)
        date4 = str(month1)+'/'+str(day4)+'/'+str(year)
        date5 = str(month1)+'/'+str(day5)+'/'+str(year)
        date6 = str(month1)+'/'+str(day6)+'/'+str(year)
    elif month in month_lst1 and day == 30:
        month1 = month + 1
        day1=1;day2=2;day3=3;day4=4;day5=5;day6=6
        date1 = str(month1)+'/'+str(day1)+'/'+str(year)
        date2 = str(month1)+'/'+str(day2)+'/'+str(year)
        date3 = str(month1)+'/'+str(day3)+'/'+str(year)
        date4 = str(month1)+'/'+str(day4)+'/'+str(year)
        date5 = str(month1)+'/'+str(day5)+'/'+str(year)
        date6 = str(month1)+'/'+str(day6)+'/'+str(year)
        
    elif month == 2 and day1 == 28:
        month2 = month + 1
        day2=1;day3=2;day4=3;day5=4;day6=5
        date2 = str(month2)+'/'+str(day2)+'/'+str(year)
        date3 = str(month2)+'/'+str(day3)+'/'+str(year)
        date4 = str(month2)+'/'+str(day4)+'/'+str(year)
        date5 = str(month2)+'/'+str(day5)+'/'+str(year)
        date6 = str(month2)+'/'+str(day6)+'/'+str(year)
    elif month in month_lst and day1 == 31:
        month2 = month + 1
        day2=1;day3=2;day4=3;day5=4;day6=5
        date2 = str(month2)+'/'+str(day2)+'/'+str(year)
        date3 = str(month2)+'/'+str(day3)+'/'+str(year)
        date4 = str(month2)+'/'+str(day4)+'/'+str(year)
        date5 = str(month2)+'/'+str(day5)+'/'+str(year)
        date6 = str(month2)+'/'+str(day6)+'/'+str(year)
    elif month in month_lst1 and day1 == 30:
        month2 = month + 1
        day2=1;day3=2;day4=3;day5=4;day6=5
        date2 = str(month2)+'/'+str(day2)+'/'+str(year)
        date3 = str(month2)+'/'+str(day3)+'/'+str(year)
        date4 = str(month2)+'/'+str(day4)+'/'+str(year)
        date5 = str(month2)+'/'+str(day5)+'/'+str(year)
        date6 = str(month2)+'/'+str(day6)+'/'+str(year)
        
    elif month == 2 and day2 == 28:
        month3 = month + 1
        day3=1;day4=2;day5=3;day6=4
        date3 = str(month3)+'/'+str(day3)+'/'+str(year)
        date4 = str(month3)+'/'+str(day4)+'/'+str(year)
        date5 = str(month3)+'/'+str(day5)+'/'+str(year)
        date6 = str(month3)+'/'+str(day6)+'/'+str(year)
    elif month in month_lst and day2 == 31:
        month3 = month + 1
        day3=1;day4=2;day5=3;day6=4
        date3 = str(month3)+'/'+str(day3)+'/'+str(year)
        date4 = str(month3)+'/'+str(day4)+'/'+str(year)
        date5 = str(month3)+'/'+str(day5)+'/'+str(year)
        date6 = str(month3)+'/'+str(day6)+'/'+str(year)
    elif month in month_lst1 and day2 == 30:
        month3 = month + 1
        day3=1;day4=2;day5=3;day6=4
        date3 = str(month3)+'/'+str(day3)+'/'+str(year)
        date4 = str(month3)+'/'+str(day4)+'/'+str(year)
        date5 = str(month3)+'/'+str(day5)+'/'+str(year)
        date6 = str(month3)+'/'+str(day6)+'/'+str(year)
        
    elif month == 2 and day3 == 28:
        month4 = month + 1
        day4=1;day5=2;day6=3
        date4 = str(month4)+'/'+str(day4)+'/'+str(year)
        date5 = str(month4)+'/'+str(day5)+'/'+str(year)
        date6 = str(month4)+'/'+str(day6)+'/'+str(year)
    elif month in month_lst and day3 == 31:
        month4 = month + 1
        day4=1;day5=2;day6=3
        date4 = str(month4)+'/'+str(day4)+'/'+str(year)
        date5 = str(month4)+'/'+str(day5)+'/'+str(year)
        date6 = str(month4)+'/'+str(day6)+'/'+str(year)
    elif month in month_lst1 and day3 == 30:
        month4 = month + 1
        day4=1;day5=2;day6=3
        date4 = str(month4)+'/'+str(day4)+'/'+str(year)
        date5 = str(month4)+'/'+str(day5)+'/'+str(year)
        date6 = str(month4)+'/'+str(day6)+'/'+str(year)
        
    elif month == 2 and day4 == 28:
        month5 = month + 1
        day5=1;day6=2
        date5 = str(month5)+'/'+str(day5)+'/'+str(year)
        date6 = str(month5)+'/'+str(day6)+'/'+str(year)
    elif month in month_lst and day4 == 31:
        month5 = month + 1
        day5=1;day6=2
        date5 = str(month5)+'/'+str(day5)+'/'+str(year)
        date6 = str(month5)+'/'+str(day6)+'/'+str(year)
    elif month in month_lst1 and day4 == 30:
        month5 = month + 1
        day5=1;day6=2
        date5 = str(month5)+'/'+str(day5)+'/'+str(year)
        date6 = str(month5)+'/'+str(day6)+'/'+str(year)
        
    elif month == 2 and day5 == 28:
        month6 = month + 1
        day6=1
        date6 = str(month6)+'/'+str(day6)+'/'+str(year)
    elif month in month_lst and day5 == 31:
        month6 = month + 1
        day6=1
        date6 = str(month6)+'/'+str(day6)+'/'+str(year)
    elif month in month_lst1 and day5 == 30:
        month6 = month + 1
        day6=1
        date6 = str(month6)+'/'+str(day6)+'/'+str(year)

        
#Geting the number of Manoushes day by the other.
    th = int(input('the Manoushes number of Thursday: '))
    f = int(input('the Manoushes number of Friday: '))
    sa = int(input('the Manoushes number of Saturday: '))
    su = int(input('the Manoushes number of Sunday: '))
    m = int(input('the Manoushes number of Monday: '))
    tu = int(input('the Manoushes number of Tuesday: '))
    w = int(input('the Manoushes number of Wednsday: '))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~')

#Geting the number of Bread day by the other.
    thb = int(input('the Bread number of Thursday: '))
    fb = int(input('the Bread number of Friday: '))
    sab = int(input('the Bread number of Saturday: '))
    sub = int(input('the Bread number of Sunday: '))
    mb = int(input('the Bread number of Monday: '))
    tub = int(input('the Bread number of Tuesday: '))
    wb = int(input('the Bread number of Wednsday: '))
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
    
#Write the number of the (Manoushe and Bread) and the date to the Excel file.
    file.write('\nThursday,{},{},{}\nFriday,{},{},{}\nSaturday,{},{},{}\nSunday,{},{},{}\nMonday,{},{},{}\nTuesday,{},{},{}\nWednsday,{},{},{}'.format(th,thb,date,f,fb,date1,sa,sab,date2,su,sub,date3,m,mb,date4,tu,tub,date5,w,wb,date6))
    
#Write the sum of the Manoushes number and the sum of the Bread number to the Excel file.
    sum_m = th+f+sa+su+m+tu+w
    sum_b = thb+fb+sab+sub+mb+tub+wb
    file.write('\nSum,{},{}'.format(sum_m,sum_b))
    
# Setting the price of  Manoushes and bread and multiply it with the numbers.
    one_m_price = float(input('the price of one Manoushe: '))
    one_b_price = float(input('the price of one bread: '))
    m_price = one_m_price * sum_m
    b_price = one_b_price * sum_b
    file.write('\nPrice of One,  {} LB,  {} LB\nTotal Price,  {} LB,  {} LB'.format(one_m_price,one_b_price,m_price,b_price))
    
#write the final total price to the Excel file.
    tot = m_price + b_price
    file.write('\n\nFinal Total,{} LB\n\nSignture,Samiha Chaar'.format(tot))
    
# Just an Ending
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('\t\t\tThank you for your time\n\t\t\t\tYour Report is Ready')
    input('Hit the Enter button please')
    
    