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
        endpoint_url = 'http://127.0.0.1:4000',
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
        #sortedEc2List = dict(sort_values(ec2list.items()))
        #sorted_dict = {k: v for k, v in sorted(ec2list.items(), key=lambda item: item[1])}
        sorted_df = pandas.DataFrame(ec2list, columns=['InstanceId', 'LaunchTime']).sort_values(['InstanceId', 'LaunchTime'])
        sorted_dict = sorted_df.sort_values(by=['LaunchTime'])
        print(sorted_dict)
        sorted_dict.to_json(r'my_data.json', orient='values')

        #with open(region+".txt", 'w') as f:
        #    json.dump(sorted_dict, f)

main()
