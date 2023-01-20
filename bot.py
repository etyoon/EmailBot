from datetime import date

def numOfdays(date1, date2):
    return(date1-date2).days

def update():
    pd = []

    with open(r'C:\\Users\\17735\Desktop\\Projects\\EmailBot\\main_info.txt', 'r') as f:
        last = f.readlines()

    year = int(last[0][:-1])
    month = int(last[1][:-1])
    day = int(last[2][:-1])
    code = float(last[3][:-1])

    ppl = {1: ['aman', 'adit'], -1: ['ethan', 'jai']}

    today = str(date.today())
    wyear = str(today[0:4])
    wmonth = str(today[5:7])
    wday = str(today[8:])
    if numOfdays(date.today(), date(year, month, day)) >= 2:
        lst = ppl[code]
        for people in lst:
            string = "C:\\Users\\17735\\Desktop\\Projects\\EmailBot\\People\\" + str(people) + ".txt"
            with open(string) as f:
                task = f.read()
            f.close()
            if task[0] == 'D':
                task = 'T'
            elif task[0] == 'T':
                task = 'D'
            with open(string, 'w') as w:
                w.write(task)
                w.close()
            pd.append((people, task))
        with open(r'C:\Users\17735\Desktop\Projects\EmailBot\main_info.txt', 'w') as w:
            w.write(wyear + '\n' + wmonth + '\n' + wday + '\n' + str(-code))
            w.close()
        return(pd)
