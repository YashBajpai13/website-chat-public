<h1>Website Chat</h1>
Website Chat is a project hosted on Streamlit that utilizes OpenAI's API to generate embeddings for inputted websites. These embeddings are then stored in an FAISS vector store for efficient similarity search. 
The project uses Groq for faster inferencing and the ability to use Open Source LLMs.
<br>
⚠️ This repository is a public version of my private repository (as it contains a private key) which has been used for hosting on streamlit (https://website-chat.streamlit.app/). 
<b>⚠️⚠️PLEASE NOTE: THE WEBSITE https://website-chat.streamlit.app/ USES MY API KEY AS IT IS FREE TO USE AT THE MOMENT BUT YOU WILL HAVE TO CREATE YOUR OWN OPENAI API KEY AND ADD CREDITS TO IT</b>
<h3>Usage</h3>

<h3>Project Structure</h3>
<ul>
<li>app.py: The main Streamlit application file.</li>
<li>.env: Configuration file where API keys for OpenAI and Groq are stored. Users need to replace the placeholder with their own API keys.</li>
<li>requirements.txt: List of dependencies required to run the project.</li>
</ul>

<b>To use the app hosted on streamlit cloud:</b>
<ol>
<li> Create an OpenAI API key (It is a paid only api key). </li>
<li> Open https://website-chat.streamlit.app/ , and enter the API key here. </li>
<li> Input the website link and press enter. </li>
<li> Input your prompt and with for the response. </li>
</ol>
<b>To use Website Chat locally, follow these steps:</b>
<ol>
<li> Clone the repository to your local machine. </li>
<li> Install the necessary dependencies listed in requirements.txt. </li>
<li> Obtain the API keys for OpenAI(paid) and Groq(free as of 22/04/24). </li>
<li>Replace the placeholders for the API keys in the .env file with your own keys.</li>
<li>Run the Streamlit application using streamlit run app.py.</li>
<li>Enter the URL of the website you want to chat with.</li>
<li>Explore the website's content with prompts.</li>

<h5> Current Limitations: </h5>
<ul>
<li> The website doesn't remember previous prompts. </li>
<li> There is no persistance of previous chats.</li>
</ul>
