import streamlit as st
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Adjusted title to move it a bit higher
st.markdown(
    """
    <div style='text-align: center; margin-bottom: -20px;'>
        <h1 style='font-size: 24px; margin-bottom: 5px;'>
            SalesSensei - Your AI-Powered Sales Analyst
        </h1>
        <h2 style='font-size: 18px; margin-top: -10px;'>
            Chat Interface
        </h2>
    </div>
    """,
    unsafe_allow_html=True,
)

# HTML for adjusted chat interface
chat_html = """
<div class="chat-container">
  <div class="chat-messages" id="chat-messages"></div>
  <div class="chat-input-container">
    <div class="chat-input">
      <textarea id="user-input" placeholder="Type your message..."></textarea>
      <label for="file-upload" class="file-upload-label">📎</label>
      <input type="file" id="file-upload" class="file-upload-input">
      <button onclick="sendMessage()">➤</button>
    </div>
  </div>
</div>

<style>
  body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    background-color: #f4f4f4;
  }

  .chat-container {
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    height: 480px; /* Slightly reduced height */
    width: 400px;  /* Fixed width */
    border: 1px solid #ccc;
    border-radius: 10px;
    background-color: #ffffff;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  }

  .chat-messages {
    flex-grow: 1;
    overflow-y: auto; /* Scrollable messages */
    padding: 10px;
    background-color: #f9f9f9;
    border-bottom: 1px solid #ccc;
  }

  .chat-message {
    display: flex;
    margin-bottom: 10px;
    align-items: center;
  }

  .user-message {
    justify-content: flex-end;
  }

  .assistant-message {
    justify-content: flex-start;
  }

  .message-bubble {
    padding: 10px 15px;
    border-radius: 15px;
    max-width: 75%;
    font-size: 14px;
    line-height: 1.4;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .user-bubble {
    background-color: #dcf8c6;
    color: #000;
  }

  .assistant-bubble {
    background-color: #eaeaea;
    color: #000;
  }

  .chat-input-container {
    border-top: 1px solid #ccc;
    background-color: #fff;
    padding: 10px;
  }

  .chat-input {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .chat-input textarea {
    flex-grow: 1;
    resize: none;
    border: 1px solid #ccc;
    outline: none;
    font-size: 14px;
    line-height: 1.4;
    padding: 10px;
    border-radius: 5px;
    height: 40px; /* Fixed height for input */
  }

  .chat-input button {
    border: none;
    background-color: #007bff;
    color: white;
    padding: 10px 15px;
    border-radius: 5px;
    cursor: pointer;
    font-size: 16px;
  }

  .chat-input button:hover {
    background-color: #0056b3;
  }

  .file-upload-label {
    cursor: pointer;
    font-size: 20px;
    color: #007bff;
  }

  .file-upload-input {
    display: none;
  }
</style>

<script>
  function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const fileInput = document.getElementById("file-upload").files[0];
    const chatMessages = document.getElementById("chat-messages");

    if (userInput) {
      // Append user's message to the chat
      const userMessage = document.createElement("div");
      userMessage.className = "chat-message user-message";
      userMessage.innerHTML = `<div class="message-bubble user-bubble">${userInput}</div>`;
      chatMessages.appendChild(userMessage);
    }

    // Simulate chatbot response
    setTimeout(() => {
      const botMessage = document.createElement("div");
      botMessage.className = "chat-message assistant-message";
      botMessage.innerHTML = `<div class="message-bubble assistant-bubble">I received your message: "${userInput}"</div>`;
      chatMessages.appendChild(botMessage);

      // Scroll to the bottom of the chat
      chatMessages.scrollTop = chatMessages.scrollHeight;
    }, 1000);

    // Clear input fields
    document.getElementById("user-input").value = "";
    document.getElementById("file-upload").value = "";
  }
</script>
"""

# Render the chat interface
st.components.v1.html(chat_html, height=600)
