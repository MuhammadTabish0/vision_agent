# Import the classes you need from the VisionAgent package
import os
from vision_agent.agent import VisionAgentCoderV2
from vision_agent.models import AgentMessage
from enviroment_variable import myclass
myclass.run_enviromentvariable()
# Enable verbose output 
agent = VisionAgentCoderV2(verbose=True)

# Add your prompt (content) and image file (media)
code_context = agent.generate_code(
    [
        AgentMessage(
            role="user",
            content="The picture has cans. Count the no of cans and make a red dot in the center of the cans.",
            media=["images.jpeg"]
        )
    ]
)

# Write the output to a file
with open("generated_code.py", "w") as f:
    f.write(code_context.code + "\n" + code_context.test)