import json
import watson_developer_cloud


data = json.load(open('secrets.json'))


assistant = watson_developer_cloud.AssistantV1(
    username=data['username'],
    password=data['password'],
    version=data['version']
)

text = 0
workSpaceId = 'e725815f-7f7e-40ca-a9eb-bff8ccafe47e'

while text != '1':
    print("To exit press 1")
    text = input("Q: ")
    response = assistant.message(
        workspace_id=workSpaceId,
        input={
            'text': text
        }
    )
    print(json.dumps(response, indent=2))

    if text == 1:
        print("while should exit")

