# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:49:21 2015

@author: jrayner
"""
import yaml as ya

class run(ya.YAMLObject):
    yaml_tag= u'!run'
    def __init__(self,name,system,workflow):
        self.name = name
        self.system= system
        self.workflow=workflow
    def __repr__(self):
        return "%s(name=%r, system=%r, workflow=%r)" % (self.__class__.__name__,self.name, self.system,self.workflow)
        
class system(ya.YAMLObject):
    yaml_tag= u'!system'
    def __init__(self,ip,cpu,disk,mem):
        self.ip=ip
        self.cpu=cpu
        self.disk=disk
        self.mem=mem
    def __repr__(self):
        return "%s(ip=%r,cpu=%r,disk=%r,mem=%r)" % (self.__class__.__name__,self.ip,self.cpu,self.disk,self.mem)
        
class workflow(ya.YAMLObject):
    yaml_tag= u'!workflow'
    def __init__(self,name,version,runType,inputFormat,lane):
        self.name=name
        self.version=version
        self.runType=runType
        self.inputFormat=inputFormat
        self.lane=lane
    def __repr__(self):
        "%s(name=%r,version=%r,runType=%r,inputFormat=%r,lane=%r)" % (self.__class__.__name__,self.name,self.version,self.runType,self.inputFormat,self.lanelane)
        
class cpu(ya.YAMLObject):
    yaml_tag=u'CPU'
    def __init__(self,model,sockets,cores,threads,GHz):
        self.model =model
        self.sockets=sockets
        self.cores=cores
        self.threads=threads
        self.GHz=GHz
    def __repr__(self):
        "%s(model=%r,sockets=%r,cores=%r,threads=%r,GHz=%r)" % (self.__class__.__name__,self.model,self.sockets,self.cores,self.threads,self.GHz)

class disk(ya.YAMLObject):
    yaml_tag=u'disk'
    def __init__(self,number,size,raidLevel,raidType):
        self.number=number
        self.size=size
        self.raidLevel=raidLevel
        self.raidType=raidType
    def __repr__(self):
        "%s(number=%r,size=%r,raidLevel=%r,raidType=%r)" % (self.__class__.__name__,self.number,self.size,self.raidLevel,self.raidType)
#workflows

W1 = workflow("HAS","2.5.55.1311.HAS","GenerateFASTQ","bcl","1-8")
W2 = workflow("HAS","2.5.55.1311.HAS","Alignment","FASTQ","4")
W3 = workflow("Isis","2.5.55.16.NorthStar","Resequence","bcl","1")
W4 = workflow("Isis","2.6.17.5.NorthStar","Resequence","bcl","1")
W5 = workflow("Isis", "2.5.55.16.NorthStar","Tumor normal","bcl","1-4")
W6 = workflow("Isis", "2.6.17.6.NorthStar","Tumor normal","bcl","1-4")
W7 = workflow("Isis", "2.5.55.16.NorthStar","GenerateFASTQ&Resequence","bcl","4")
W8 = workflow("Isis", "2.6.17.6.NorthStar","GenerateFASTQ&Resequence","bcl","4")
W9 = workflow("Isis", "2.5.55.16.NorthStar","GenerateFASTQ&Resequence","bcl","8")
W10 = workflow("Isis", "2.6.17.6.NorthStar","GenerateFASTQ&Resequence","bcl","8")
W11 = workflow("Isis", "2.5.55.16.NorthStar","Resequence", "blc", "4")
W12 = workflow("Isis", "2.6.17.6.NorthStar","Resequence", "blc", "4")
W13 = workflow("Isis", "2.5.55.16.NorthStar","Resequence","bcl","8")
W14 = workflow("Isis", "2.6.17.6.NorthStar","Resequence","bcl","8")
W15 = workflow("isaac","iSAACv3","align","bcl","4")
W16 = workflow("isaac","iSAACv3","align","bcl","8")
W17 = workflow("Isis", "2.6.17.6.NorthStar","Resequence", "blc with Reads in samplesheet", "4")
W18 = workflow("Isis", "2.6.17.11.NorthStar","Resequence","bcl", "4")
W19 = workflow("Isis", "2.6.17.11.NorthStar","GenerateFASTQ&Resequence","bcl", "4")
W20 = workflow("Isis", "2.6.17.11.NorthStar","Tumor normal","bcl","1-4")

cpu1=cpu("Intel(R) Xeon(R) CPU E5-2680 v2",2,10,40,2.80)
cpu2=cpu("Intel(R) Xeon(R) CPU E5-2680 v3",2,12,48,2.50)
cpu3=cpu("Intel(R) Xeon(R) CPU D-1540",1,8,16,2.00)
cpu4=cpu("Intel(R) Xeon(R) CPU E5-2687W v3",2,10,40,3.10)

disk1 = disk(6,5.5,0,"SW")
disk2 = disk(6,14,0,"HW")
disk3 = disk(1,1.8,"NA","NA")
disk4 = disk(6,7.3,0,"SW")
disk5 = disk(9,5.5,0,"SW")
disk6 = disk(6,14,5,"HW")
disk7 = disk(6,14,0,"SW")

S1= system("10.46.32.224",cpu1,disk1,132)
S2= system("10.46.30.46",cpu2,disk2,132)
S3= system("10.46.30.52",cpu3,disk3,66)
S4= system("10.46.30.55",cpu4,disk4,132)
S5= system("10.46.30.224",cpu1,disk5,132)
S6= system("10.46.30.46",cpu2,disk6,132)
S7= system("10.46.30.46",cpu2,disk7,132)




run1 = run("S1W3",S1,W3)
run2 = run("S1W5",S1,W5)
run3 = run("S1W1",S1,W1)
run4 = run("S1W2",S1,W2)
run5 = run("S1W4",S1,W4)
run6 = run("S1W6",S1,W6)
run7 = run("S2W3",S2,W3)
run8 = run("S2W5",S2,W5)
run9 = run("S2W1",S2,W1)
run10 = run("S2W2",S2,W2)
run11 = run("S2W6",S2,W6)
run12 = run("S3W3",S3,W3)
run13 = run("S3W5",S3,W5)
run14 = run("S3W1",S3,W1)
run15 = run("S3W2",S3,W2)
run16 = run("S3W4",S3,W4)
run17 = run("S3W6",S3,W6)
run18 = run("S4W3",S4,W3)
run19 = run("S4W5",S4,W5)
run20 = run("S4W1",S4,W1)
run21 = run("S4W2",S4,W2)
run22 = run("S4W4",S4,W4)
run23 = run("S4W6",S4,W6)
run24 = run("S2W4",S2,W4)

#run7
workflows = {"W1":W1,"W2":W2,"W3":W3,"W4":W4,"W5":W5,"W6":W6,"W7":W7,"W8":W8,"W9":W9,"W10":W10,"W11":W11,"W12":W12,"W13":W13,"W14":W14,"W15":W15,"W16":W16,"W17":W17,"W18":W18,"W19":W19,"W20":W20}

systems = {"S1":S1,"S2":S2,"S3":S3,"S4":S4}
#print 
#systemsfile = open("systems.yaml","w")
#workflowfile = open("workflows.yaml","w")
#(ya.dump(systems,systemsfile,default_flow_style=False))
#(ya.dump(workflows,workflowfile,default_flow_style=False))
#systemsfile.close()
#workflowfile.close()