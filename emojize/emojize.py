import emoji
input = input('Input: ').strip('_')
emojized_text = emoji.emojize(input, language='alias')
print('output:', emojized_text)
