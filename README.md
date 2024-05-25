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

## Why did I create this?
Before this script, I had several prompts I was running to help streamline the processing of our weekly podcast. I created 
a 'cheat sheet' in Google Docs with all my prompts, and every Sunday morning, I'd run through them to help me process 
the podcast transcript.

While the previous process was functional, it had its share of challenges. The constant switching between my Google Doc 
and the AWS Bedrock playground was time-consuming and occasionally, I would get logged out of my AWS account, disrupting 
my workflow. This was not a major issue, but it was certainly not ideal.

So why did I bother with this simple Python script? Two reasons.

First, I wanted to learn more about how I could interact with Amazon Bedrock programmatically. While the script is basic, 
I learned some basics in a low-risk environment. This is always a great way to learn something new. Second, I significantly 
improved my previous workflow. Is it perfect? No, but making incremental improvements is always good.

## Future plans
I'm working on automating my process further by using S3 event notifications and Lambda so the entire process can be triggered
by uploading the transcript to an S3 bucket.

## Links
- [Talking Cloud](https://curiousorbit.com/podcast/)
