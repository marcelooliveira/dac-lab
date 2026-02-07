from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS

with Diagram("Simple AWS Diagram", show=False):
    lb = ELB("load balancer")
    ec2 = EC2("web server")
    db = RDS("database")

    lb >> ec2 >> db
