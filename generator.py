
### importing the required python packages
import json
import boto3


def lambda_handler(event, context):
  '''
  This function will be used to create a CFN template based on the input recieved
  '''
  
  ######## BLANK template to be used to fill data into 
  template='''{
    "AWSTemplateFormatVersion" : "2010-09-09",

  "Description" : "AWS CloudFormation Template Description",



  "Resources" : {
    
  }
  }'''
  
  cfn=boto3.client('cloudformation')    ## initialized the Cloudformation boto object
  
  ### storing the CFN resource types in variables
  
  s3_bucket_type="AWS::S3::Bucket"
  iam_user_type="AWS::IAM::User"
  iam_group_type="AWS::IAM::Group"

  ### load the template defined above as json 
  stack=json.loads(template)
  resources=stack["Resources"]
  ## load the body of the request in vatiable body
  body=json.loads(str(event["body"]))

######## create dictonary of resource types for mapping later
  resourcetypes = { 
    "S3Bucket": s3_bucket_type, 
    "IAMUser": iam_user_type,
    "IAMGroup": iam_group_type
  } 

  def gettype(res_type):
    '''
    This function is used just to map the resource types.
    '''
    return resourcetypes.get(res_type,"nothing") 

  for resource in body:
    resource_name=resource["resource_name"]## get the resource name
    print(resource_name)

    resource_type=gettype(resource["resource_type"]) ## get the resource type string using the get type function 
    print(resource_type)
    subdict={"Properties":{}} ### define an empty dict
    subdict["Type"]=resource_type
    for property in resource["Properties"]:
      subdict["Properties"].update(
      {property:resource["Properties"][property]}## unsual jugaad but need to use it as I dont know the amount of properties that may come
      )  
      #print(property)
      #print(resource["Properties"][property])## unsual jugaad but need to use it as I dont know the amount of properties that may come
    print(subdict)
    resources.update({resource_name:subdict})
  
  j = json.dumps(stack, indent=4) ############ load everything in the json object which will be used as template body for stack deploy

  
  ## code for deploying the stack
  cfn.create_stack(
    StackName="test",
    TemplateBody=str(j),
    
    OnFailure='ROLLBACK',
    EnableTerminationProtection=True,
    Capabilities=[
        'CAPABILITY_NAMED_IAM'
    ]
  )
    
  return {
        'statusCode': 200,
        'body': j
  }
