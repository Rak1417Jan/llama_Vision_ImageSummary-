import streamlit as st
from groq import Groq
import os

# Set up your Groq client with API key
client = Groq(api_key=os.getenv('AWS_Groq'))

# Streamlit app layout
st.title("Image Description using Groq LLaVA Model")
st.write("Input an image URL, and get the model's description.")

# Input field for image URL
image_url = st.text_input("Enter Image URL", "")

if image_url:
    st.image(image_url, caption="Input Image", use_column_width=True)

    # Generate description using Groq LLaVA model
    if st.button("Generate Description"):
        with st.spinner('Generating description...'):
            try:
                chat_completion = client.chat.completions.create(
                    messages=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "text", "text": "Explain me what you see in the image"},
                                {
                                    "type": "image_url",
                                    "image_url": {
                                        "url": image_url,
                                    },
                                },
                            ],
                        }
                    ],
                    model="llava-v1.5-7b-4096-preview",
                )

                # Output the generated description
                description = chat_completion.choices[0].message.content
                st.success("Generated Description:")
                st.write(description)

            except Exception as e:
                st.error(f"Error generating description: {e}")
