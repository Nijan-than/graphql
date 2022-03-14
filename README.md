# graphql
mutation process using python from lambda to Dynamodb via Graphql

Summary: This is about mutation- create operation in lambda using python to dynamodb via Graphql.

Requirements: gql==3.0.0 ,requests , requests-aws4auth ==1.1.1 ,requests-toolbelt ==0.9.1 , updated version of aws-sam-cli (current updated version - 1.40.1)

Error 1 : Invalid or incomplete introspection result . Ensure that you are passing the data attribute of introspection response and no errors were returned alongside

solution :
Create IAM roles to connect with Appsync from lambda.
  Roles that we need are given detailed below .
  
      Role 1: Services: Appsync ,Access level write : Graphql Resource -> Any in this account for domain or specific function we can also mention if we want .
      Role 2: Lambda : InvokeFunction available in roles
      Role 3: AWSLambdaBasicExecutionrole
  These 3 above roles are mandatory and if we face any issue create new role with Appsync service and give all access level finally attach it in roles for the Lambda
  function.

Try to create different authorization mode in Appsync.
Appsync -> Appsync_api( we have created ) -> settings-> Additional Authorization Provides -> New -> Aws Identity and Access Management ( AWS IAM ) -> save .

Error 2: 

solution :could not satisfy the requirements boto3 or could not satisfy the requirements requests

Close Vs code and Remove Dependency libraries from requirements.txt and run the sam build command again re-enter the required libraries in requirements.txt

Error 3: TransportQueryError :

{
  "path": [
    "createweather1"
  ],
  "data": none,
    "errorType": "Unauthorized",
    "errorInfo": none,
  "locations": [
  {
    "line": 2,
    "column": 3,
    "sourceName": none
  }
    ],
    "message": "Not Authorized to access createClient on type Client"
  }

Solution: 

step1: Change authorization provides into IAM in APpsync Api -> Queries -> Change from default API to IAM .

step2: Make sure you have created the IAM with role that have mentioned in solution of Error 1.

step3: In Appsync ->Schema -> Add @aws_iam in mutation type and weather1 Type.
