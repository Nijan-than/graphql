import json
import os
import sys
import asyncio
import pprint
from gql import Client,gql
from gql.dsl import DSLSchema, DSLMutation, dsl_gql
from gql.dsl import *
from gql.transport.requests import RequestsHTTPTransport
from boto3 import Session
from requests_aws4auth import AWS4Auth



# Uncomment the following lines to enable debug output
# import logging
# logging.basicConfig(level=logging.DEBUG)


def lambda_handler(event, context):
    # accept mentioning here is that input type will be accept as json and content type we are using is json hence we mentioning the 
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        }

    aws = Session(aws_access_key_id=os.getenv('ACCESS_KEY_ID'),
                     aws_secret_access_key=os.getenv('SECRET_ACCESS_KEY'),
                     region_name=os.getenv('REGION_NAME'))
    
    credentials = aws.get_credentials().get_frozen_credentials()

    auth = AWS4Auth(
        credentials.access_key,
        credentials.secret_key,
        aws.region_name,
        'appsync',
        )
    
    url1="https://********************.appsync-api.ap-south-1.amazonaws.com/graphql"
    #sync Transport -------- > RequestsHTTPTransport
    transport = RequestsHTTPTransport(url=url1,headers=headers,auth=auth)
    print(transport)
    client=Client(transport=transport,fetch_schema_from_transport=True)
    
    
    query = gql(
        """
            mutation createWeather1 ($channelid:String,$devstatus:String,$epi_timestamp:String,$intensity:String){
            createWeather1(channelid:$channelid,devstatus:$devstatus,epi_timestamp:$epi_timestamp,intensity:$intensity) {
            id
            channelid
            devstatus
            epi_timestamp
            intensity
            }
        }"""
    )
        
    params = {
        "channelid":"kid424234",
        "devstatus":"nijan325546",
        "epi_timestamp":"bala3552",
        "intensity":"gih326"}
    resp = client.execute(query,variable_values=params)
    #print(result)
    return (resp)

#_________________________________ query
