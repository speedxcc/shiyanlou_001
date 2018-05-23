#!/usr/bin/env python3
import sys
import csv
class Args(object):
    def __init__(self):
        self.agrs = sys.argv[1:]
        if len(self.agrs)  == 6:
            try:
                index_config = self.agrs.index('-c')
                self.configfile = self.agrs[index_config + 1]
                index_user = self.agrs.index('-d')
                self.userfile = self.agrs[index_user + 1]
                index_out = self.agrs.index('-o')
                self.outfile = self.agrs[index_out + 1]
                print(self.configfile,self.userfile,self.outfile)
            except ValueError:
                print("parameter Error")
                sys.exit() 
        else:
            print("parameter Error")

class Config(object):
    def __init__(self):
        self.config = self._read_config()
        print(self.config)
    def _read_config(self):
        config = {}
        try:
            with open(args.configfile) as file:
                for line in file:
                    line = line.strip()
                    name, rate = line.split('=')
                    name = name.strip()
                    config[name] = float(rate)
        except ValueError:
            print("csg file Error!")
            sys.exit()
        return config

class UserData(object):
    def __init__(self):
        self.userdata = self._read_users_data()
    def _read_users_data(self):
        userdata = []
        try:
            with open(args.userfile) as file:
                for line in file:
                    line.strip()
                    number, gongzi = line.split(',')
                    gongzi = int(gongzi)
                    person = (number, gongzi)
                    print(person)
                    userdata.append(person) 
        except ValueError:
            print("user file Error!")
            sys.exit()
        return userdata

class IncomeTaxCalculator(object):
    
    def calc_for_all_userdata(self):
        result = []
        rate = 0
        for name, v in config.config.items():
            if name not in ['JiShuL' ,'JiShuH']:
                rate += v
               
        for person in userdata.userdata:
            
            number = person[0]
            salary = person[1]
            l = config.config['JiShuL']
            h = config.config['JiShuH']
            if salary < l:
                found = l * rate
            elif salary > h:
                found = h * rate
            else:
                found = salary * rate
            tax = salary - found - 3500
        
            if tax <= 0:
                tax_out = 0
                money = salary - tax_out - found 
            elif tax <= 1500:
                tax_out = tax * 0.03
                money = salary - tax_out - found 
            elif tax <= 4500:
                tax_out = tax * 0.1 - 105
                money = salary - tax_out - found 
            elif tax <= 9000:
                tax_out = tax * 0.2 - 555
                money = salary - tax_out - found 
            elif tax <= 35000:
                tax_out = tax * 0.25 - 1005
                money = salary - tax_out - found 
            elif tax <= 55000:
                tax_out = tax * 0.3 - 2755
                money = salary - tax_out - found 
            elif tax <= 80000:
                tax_out = tax * 0.35 - 5505
                money = salary - tax_out - found 
            else:
                tax_out = tax * 0.45 - 13505
                money = salary - tax_out - found 
            data = [number,salary,'{:.2f}'.format(found),'{:.2f}'.format(tax_out),'{:.2f}'.format(money)]               
            #data = number + ',{},{:.2f},{:.2f},{:.2f}'.format(salary,found,tax_out,money)  
            print(data)
            result.append(data)
        print(result)
        return result

    def export(self, default='csv'):
        out = self.calc_for_all_userdata()
     #   test = [['1111','1222'],'2','3']
        with open(args.outfile,'w+') as f:
            writer = csv.writer(f)
            writer.writerows(out)

if __name__ == "__main__":
    args = Args()
    config = Config()
    userdata = UserData()
    cal = IncomeTaxCalculator()
    cal.export()
