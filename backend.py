import openai 
openai.api_key = "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"


def call_openai(prompt, max_tokens=1200):


    
    response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            # stop=["<h"]
        )

    return response.get("choices")[0]['text']


def get_details(text):
    prompt = """As a discerning reader, carefully extract the employee's name, organization, manager, and evaluator
from the performance review document. The employee's name appears prominently at the top, before the year. Present
this crucial information as bullet points, separated by line breaks:
- Employee name:
- Organization:
- Manager:
- Evaluator:"""
    response = call_openai(f"{text}\n\n{prompt}")

    return response 



def recommend_courses(text):
    prompt = """As an experienced career counselor, analyze the employee's performance review with a keen eye, and recommend top-tier 
courses that will help them unlock their full potential. Present these invaluable course recommendations as bullet points, 
separated by line breaks:
- Course 1
- Course 2
- Course 3"""
    response = call_openai(f"{text}\n\n{prompt}")
    return_response = ''
  
    temp_list = response.split('•')
    for item in temp_list:
        if item != '':
            return_response += f"* {item}"

    
    return return_response

def industry_trends(text):

    prompt = """Drawing from your expertise as a career counselor, study the employee's performance review and 
determine the most rewarding career paths for them, considering their unique skills, interests, and experience. 
Conduct comprehensive research on available options, elucidate job market trends across various industries, and 
advise on the qualifications essential for pursuing specific fields.Deliver an insightful analysis and well-informed recommendations"""

    response = call_openai(f"{text}\n\n{prompt}")

    return response


def highlight_action_items(text):
    prompt = """As a seasoned manager and analyzing the employee's performance review with a keen eye, pinpoint strategic action items that will ensure the team achieves its ambitious goals and objectives. Describe the measures you would take to create a high-performance
    environment, such as setting clear expectations, providing guidance and support, establishing feedback systems, and encouraging
    collaboration. Recommend action items for the next year and present them in an ordered list:
    1. Action item 1
    2. Action item 2
    3. Action item 3"""


    response = call_openai(f"{text}\n\n{prompt}")

    return response

    
def personal_branding(text):
    prompt = """I want you to act as a career counselor. I will provide you the employee's performance analysis, and Provide tips and best practices for employees to build and maintain their personal brand, including online presence, networking, and showcasing achievements. The results should be stated pointwise. should be in an ordered list"""

    response = call_openai(f"{text}\n\n{prompt}")
    return_response = ''
    temp_list = response.split('•')
    if len(temp_list) > 2:
        for item in temp_list:
            if item != '':
                return_response += f"* {item}"
        return return_response


    return response 

def soft_skills(text):

    prompt = """I want you to act as a career counselor. I will provide you the employee's performance analysis, and Provide tips and best practices for employees to devlope their soft skills, including  communication skills and time management. The results should be stated pointwise. should be in an ordered list"""

    response = call_openai(f"{text}\n\n{prompt}")
    return_response = ''
    temp_list = response.split('•')
    if len(temp_list) > 2:
        for item in temp_list:
            if item != '':
                return_response += f"* {item}"
        return return_response

    return response 

def career_dev_ops(text):
    prompt = """As a career counselor analyzing the employee's performance review with a keen eye, pinpoint career developement opputunities that the elmployee has.
    1. Opportunity 1
    2. Opportunity 2
    3. Opportunity 3"""

    response = call_openai(f"{text} \n {prompt}")

    return response
