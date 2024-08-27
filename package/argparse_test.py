import argparse
parser = argparse.ArgumentParser(description='A simple argument parser')
parser.add_argument("--host","-H",type=str,default="localhost",help="Host name or IP address")
parser.add_argument("--port","-p",type=int,default=5432,help="Port number")
parser.add_argument("--database","-d",type=str,default="test",help="Database name")
parser.add_argument("--user","-u",type=str,default="test",help="User name")
parser.add_argument("--password","-pw",type=str,default="<PASSWORD>",help="Password")
args = parser.parse_args()
def GetSQL(host:str,port:int,database:str,user:str,password:str):
    print("Connecting to database...")
    print(host,port,database,user,password)
if __name__=="__main__":
    GetSQL(args.host,args.port,args.database,args.user,args.password)