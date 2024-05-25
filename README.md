I created this to streamline my current GenAI workflow for processing the transcript of our weekly podcast.

## Requirements
1. The script relies on several Python Libraries. Have a look at the requirements.txt file for a list.
2. You must access your AWS account using AWS Identity Center (SSO).
3. You must have a config.json file in the same folder as the script.
4. You must have a transcript.txt file in the same folder as the script.

## Configuration File
The script requires a configuration file (config.json) to be present in the same directory as the script.

Here's an example of the config.json file

```json
{
  "sso": [
    {
      "start_url": "<Identity Center SSO URL>",
      "region": "<Identity Center AWS region>",
      "role_name": "<Name of the IAM Role you will assume>"
    }
  ],
  "account": [
    {
      "name": "<AWS Account Name>",
      "id": "<AWS Account ID>",
      "region": "<AWS Region>"
    }
  ],
  "ai": [
    {
      "anthropic_version": "bedrock-2023-05-31",
      "max_tokens": 4000,
      "prompt_text": "Create show notes for my podcast episode. The show notes should include an engaging summary, key takeaways, episode highlights, memorable quotes, action steps for listeners, blog post ideas, and a call to action. In addition, create the following for the website - page slug, page description, and page title. Here's the transcript:",
      "model_id": "anthropic.claude-3-sonnet-20240229-v1:0"
    }
  ]
}
```

## Future plans
I'm working on automating my process further by using S3 event notifications.
