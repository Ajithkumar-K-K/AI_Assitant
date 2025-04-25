import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyDWUPt0OJzTOdqa1yUGYZoCjviOpAFO0Zo")

def get_recommendations(message):
    model = genai.GenerativeModel("gemini-1.5-flash")
    
    # Refined prompt to encourage deeper thinking
    refined_prompt = (
        f"{message}\n"
        "Generate the answer to the question after self-validating, if it is a multiple choice generate the choice only."
    )
    
    response = model.generate_content(refined_prompt)
    return response.text

if __name__ == "__main__":
    print(get_recommendations("Who are you?"))