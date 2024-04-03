# Use this code to test openAI key for using ChatGPT.
A basic script to make sure if the key is valid.

## Tool installation
Since the code uses old features, installer an older version of opanAI.
`pip install openai==0.28`

## Usage
1. Save the openAI key in a file `key.txt` in the same directory.
2. Use `python main.py` to run the script.
3. If the script is running successfully, you should see a joke produced by chatGPT.

## Customizing the Prompt
To change the prompt used for text generation, edit the messages parameter in the openai.ChatCompletion.create call within the script. Replace "Tell me a joke." with your desired prompt.
