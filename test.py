from openai import OpenAI
import streamlit as st

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "NVIDIA_API_KEY"
)

# completion = client.chat.completions.create(
#   model="nvidia/llama-3.1-nemotron-70b-instruct",
#   messages=[{"role":"user","content":"How many r in strawberry? "}],
#   temperature=0.5,
#   top_p=1,
#   max_tokens=1024,
#   stream=True
# )

# for chunk in completion:
#   if chunk.choices[0].delta.content is not None:
#     print(chunk.choices[0].delta.content, end="")
#     import streamlit as st

def main():
        st.title("Nvidia AI Chat")
        
        user_input = st.text_input("Enter your question:")
        
        if st.button("Generate Response"):
            completion = client.chat.completions.create(
                model="nvidia/llama-3.1-nemotron-70b-instruct",
                messages=[{"role": "user", "content": user_input}],
                temperature=0.5,
                top_p=1,
                max_tokens=1024,
                stream=True
            )
            
            response = ""
            response_container = st.empty()
            for chunk in completion:
                if chunk.choices[0].delta.content is not None:
                    response += chunk.choices[0].delta.content
                    response_container.markdown(response)

if __name__ == "__main__":
    main()

