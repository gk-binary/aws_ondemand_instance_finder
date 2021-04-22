import pandas as pd
region=["us-east-1","us-east-2",
        "us-west-1","us-west-2",
        "ap-south-1",
        "ap-northeast-3","ap-northeast-2","ap-southeast-1","ap-southeast-2","ap-northeast-1",
        "ca-central-1",
        "eu-central-1","eu-west-1","eu-west-2","eu-west-3","eu-north-1",
        "sa-east-1"]

def printProper(head,content):
    for x in head:
        print(x,end ="\t \t \t \t")
    print("\n")
    for c in content:
        for d in c:
            print(d, end="\t \t \t")
        print("\n")

def Sort(sub_li):
    sub_li.sort(key=lambda x: x[2])
    return sub_li
def find_bestInstance(cpu,ram,current_region,current_instance_type):
    result=[]
    current_price=0
    for reg in region:
        data=pd.read_csv("aws_price/ec2_ondemand/{}.csv".format(reg))
        for d in range (len(data)):
            cData=data.iloc[d]
            if current_region and current_instance_type:
                if current_region == reg and current_instance_type == cData.type:
                    current_price=float(cData.price.split(" ")[0][1:])
            if (cData.cpu == cpu and str(cData.ram.split(" ")[0]) == str(ram)):
                if current_region and not current_instance_type:
                    if reg==current_region:
                        result.append([
                            reg,
                            cData.type,
                            float(cData.price.split(" ")[0][1:]),
                            round(float(cData.price.split(" ")[0][1:]) * 24 * 30, 2)
                        ])
                else:
                    result.append([
                        reg,
                        cData.type,
                        float(cData.price.split(" ")[0][1:]),
                        round(float(cData.price.split(" ")[0][1:])*24*30,2)
                    ])
    suggestion=[]
    if current_region and current_instance_type:
        for r in result:
            if r[2]<current_price:
                r.append(current_price - r[2])
                r.append((current_price - r[2])*24*30)
                suggestion.append(r)


    sortedReults=Sort(result)
    print("ram : ",ram,"cpus : ",cpu)
    printProper(["region","type","hr_price","month_price"],sortedReults)
if __name__ == '__main__':
    find_bestInstance(cpu=4,ram=8,current_region="ap-south-1",current_instance_type=None)