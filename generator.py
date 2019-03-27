import json

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
resources=stack["Resources"]

bodytext='''
[
  {
  "resource_name":"Bucket01",
  "resource_type":"S3Bucket",    
  "Properties" : {
    "AccessControl" : "PublicRead",
    "BucketName" : "dfdfdfdfdf"
              
    }
  },
  {
  "resource_name":"User01",   
  "resource_type":"IAMUser",    
  "Properties" : {
    "UserName": "raghuram"          
    }
  }]


'''

body=json.loads(bodytext)


resourcetypes = { 
    "S3Bucket": s3_bucket_type, 
    "IAMUser": iam_user_type,
    "IAMGroup": iam_group_type
} 

def gettype(res_type):
  return resourcetypes.get(res_type,"nothing") 

for resource in body:
  resource_name=resource["resource_name"]
  print(resource_name)

  resource_type=gettype(resource["resource_type"])
  print(resource_type)
  subdict={"Properties":{}}
  subdict["Type"]=resource_type
  for property in resource["Properties"]:
    subdict["Properties"].update(
      {property:resource["Properties"][property]}## unsual jugaad but need to use it as I dont know the amount of properties that may come
      )  
    #print(property)
    #print(resource["Properties"][property])## unsual jugaad but need to use it as I dont know the amount of properties that may come
  print(subdict)
  resources.update({resource_name:subdict})
  
j = json.dumps(stack, indent=4)
print(j)
