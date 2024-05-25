import boto3
from aws_sso_lib import get_boto3_session
import json


def main():
    # Open the config JSON file and grab all the items we need
    with open('./config.json') as config:
        data = json.load(config)

        # Get the AWS SSO config data
        for sso_item in data['sso']:
            sso_start_url = sso_item['start_url']
            sso_region = sso_item['region']
            sso_role_name = sso_item['role_name']

        # Get the account info from the config data
        for account_item in data['account']:
            account_name = account_item['name']
            account_id = account_item['id']
            account_region = account_item['region']

        # Get the other info from the config data
        for ai_item in data['ai']:
            anthropic_version = ai_item['anthropic_version'],
            max_tokens = ai_item['max_tokens'],
            prompt_text = ai_item['prompt_text']
            model_id = ai_item['model_id']

    # Open the file that contains the podcast transcript
    with open('transcript.txt', 'r') as f:
        transcript = f.read()

    # Create a Boto3 session with AWS SSO
    boto3_sso_session = get_boto3_session(sso_start_url, sso_region, account_id, sso_role_name, region=account_region,
                                          login=True)

    # Create a Boto3 client with the Bedrock Runtime service
    client = boto3_sso_session.client('bedrock-runtime')

    # Invoke the Anthropic model
    try:
        response = client.invoke_model(
            body=json.dumps({
                "anthropic_version": anthropic_version[0],
                "max_tokens": max_tokens[0],
                "messages": [{
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": prompt_text
                        },
                        {
                            "type": "text",
                            "text": transcript
                        }
                    ]
                }]
            }),
            modelId=model_id
        )
        result = json.loads(response['body'].read())
        print(result['content'][0]['text'])
    except Exception as e:
        print(e)

    # Close the client connection
    client.close()


main()
