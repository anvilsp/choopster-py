# Using cohost.py - https://github.com/valknight/Cohost.py

from cohost.models.user import User
from cohost.models.block import AttachmentBlock, MarkdownBlock
from dotenv import load_dotenv
from os import environ as env
import requests

load_dotenv()
user = User.login(env['COHOST_LOGIN'], env['COHOST_PASS'])

# Request Poopster
response = requests.get(env['PARSE_URL'])

# Get json
stage = response.json()

# Tags
context1 = stage['first_stage'] + " (" + stage['first_context'] + ")"
context2 = stage['second_stage'] + " (" + stage['second_context'] + ")"
seed = stage['seed']

project = user.getProject(env['COHOST_PAGE']) # will retrieve the page I have edit writes for with handle @vallerie

blocks = [
   # MarkdownBlock('**Hello from Python!**') # Example of markdown / text block
]
newPost = project.post(stage['stagename'], blocks, tags=[context1, context2, 'poopster', 'The Cohost Bot feed', seed])
print(stage['stagename'] + ' | Post created')

#print('Check out your post at {}'.format(newPost.url))
