# Familiarize with basic prompt & message
import camel
from camel.prompts import TextPrompt

print('------------ TextPropt inherits from String class & allows for formatting/concat/add/join -------')
prompt = TextPrompt("Please enter your name: {name} age: {age}")

print(prompt)
print(prompt.key_words)
formatted_prompt = prompt.format(name='Das Vader', age=99)
print(formatted_prompt)
half_formatted_prompt = prompt.format(name='Das Vader')
print(half_formatted_prompt)

prompt1 = TextPrompt("\n Good day, {name}!")
# Concatenation
prompt2 = prompt + prompt1
print(prompt2)
print(isinstance(prompt2, TextPrompt))

prompt3 = TextPrompt(' ').join([prompt, prompt1])
print(prompt3)
print(isinstance(prompt3, TextPrompt))

print(prompt3.key_words)
formatted_prompt3 = prompt3.format(name='Das Vader', age=99)
print(formatted_prompt3)

prompt4 = prompt3.upper()
print(prompt4)
print(isinstance(prompt4, TextPrompt))

print(prompt4.key_words)

print('\n')

from camel.prompts import CodePrompt
code_prompt = CodePrompt("a = 100 + 2", code_type='python')
print(code_prompt)
print(code_prompt.code_type)

code_prompt = CodePrompt("a = 100 + 2")
print(code_prompt.code_type)
code_prompt.set_code_type('python')
print(code_prompt.code_type)

print('Code Prompt can be Executed')
import numpy as np
code_prompt = CodePrompt("b = 2 + 4\na = b*100+3\nprint(a)", code_type='python')

output, intepreter = code_prompt.execute()
print(output)
print(intepreter.state['a'])
print(intepreter.state['b'])

code_prompt = CodePrompt("import numpy\na = numpy.zeros(30)\nprint(a)", code_type='python')
traceback, _ = code_prompt.execute()
print(traceback)
