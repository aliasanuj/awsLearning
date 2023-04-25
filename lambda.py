import json
import uuid 
get_raw_path = "/getPerson"
create_raw_path = "/postPerson"
def lambda_handler(event, context):
    print(type(event))
    print("event is ",event)
    
    print(type(context))
    print("context is ",context)
    
    if event['rawPath'] == get_raw_path:
        print("dkbchsd")
        ####getperson path - call database
        print("start request for getPerson")
        variable1 = event['queryStringParameters']['key1']
        print("variable1 will be ", variable1)
        print("received request with personId = ",variable1)
        return  {"firstName":"narendra","lastname":"modi","country":"india"}
    
    elif event['rawPath'] == "/postPerson":
          ###create person path -- Write to database
          print("start request for create person. . . ")
          decodeBody = json.loads(event["body"])
          print("decodeBody is ", decodeBody)
          firstName = decodeBody['firstName']
          print('received request with firstName = ',firstName)
          ###call DB
          return {"personId" : str(uuid.uuid1())}
          
          
          
          
    
    
    # # TODO implement
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps('Hello from Lambda!')
    # }
    # return "200"
    