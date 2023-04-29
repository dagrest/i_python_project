import json
import boto3
from handler import datetime_converter
import pandas

session = boto3.session.Session()

# filename = regions.t
def readFile(filename):
    regions = []
    txtFile = open(filename, "r")
    contentList = txtFile.readlines()
    for line in contentList:
        splitLine = line.split(',')
        for region in splitLine:
            regions.append(region.strip())   
    return regions


def getEc2PerRegion(region):
    ec2list = []
    ec2 = session.client(
        service_name = 'ec2',
        aws_access_key_id = 'xxx',
        aws_secret_access_key = 'xxx',
        endpoint_url = 'http://host.docker.internal:4000', # can be defined as env var
        region_name = region
    )
    response = ec2.describe_instances()
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            ec2list.append((instance['InstanceId'], datetime_converter(instance['LaunchTime'])))
    return ec2list


def main():
    regions = readFile('regions.txt')
    for region in regions:
        ec2list = getEc2PerRegion(region)
        sorted_df = pandas.DataFrame(ec2list, columns=['InstanceId', 'LaunchTime']).sort_values(['InstanceId', 'LaunchTime'])
        sorted_dict = sorted_df.sort_values(by=['LaunchTime'])
        #print(sorted_dict)
        sorted_dict.to_json(r"{}.json".format(region), orient='values')

main()
