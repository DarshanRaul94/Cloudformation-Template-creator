

import json
#####################Sample Template Anatomy##################
template='''{
    "AWSTemplateFormatVersion" : "2010-09-09",
  
    "Description" : "AWS CloudFormation Template",
  
   
  
    "Resources" : {
        
    }
  }'''
  
########################  
s3type="AWS::S3::Bucket"
stack=json.loads(template)
resources=stack["Resources"] 
s3bucket={}
s3bucket.update({"Type" : s3type})

s3bucket.update({
   "Properties" :{
        "AccessControl" : "PublicRead",
       "BucketName" : "dfdfdfdfdfgguyigu"  
   }
})
#s3bucketproperties={}

#s3bucketproperties["AccessControl"]="PublicRead"
#s3bucketproperties["BucketName"]="skfgfhskh"
#s3bucket["Properties"]=s3bucketproperties
resources["HelloWorld"]=s3bucket

#print(stack)
j = json.dumps(stack, indent=4)
print(j)
