import json

def lambda_handler(event, context):
    # TODO implement
    template='''{
    "AWSTemplateFormatVersion" : "2010-09-09",
  
    "Description" : "AWS CloudFormation Template Description",
  
   
  
    "Resources" : {
        
    }
    }'''


    s3_bucket_type="AWS::S3::Bucket"
    iam_user_type="AWS::IAM::User"
    iam_group_type="AWS::IAM::Group"


    stack=json.loads(template)


    
    body=json.loads(str(event["body"]))
    properties=body["Properties"]
    
    resources=stack["Resources"] 
    s3bucket={}
    s3bucket.update({"Type" : s3_bucket_type,"Properties":{}})
    
    for property in body["Properties"]:
        s3bucket["Properties"].update(
         {property:body["Properties"][property]}## unsual jugaad but need to use it as I dont know the amount of properties that may come
        )
    #####for local testing
    """bodytext='''{
    "Properties" : {
       "AccessControl" : "PublicRead",
       "BucketName" : "dfdfdfdfdf",
       "hello":"adfdfdf"           
    }
    }'''

    body=json.loads(bodytext)"""

    


    resources.update({"HelloWorld":s3bucket})


    #print(stack)
    j = json.dumps(stack, indent=4)
    print(j)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
