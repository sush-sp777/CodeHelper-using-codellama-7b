import requests
import json
import gradio as gr

url="http://localhost:11434/api/chat"

headers={
    'Content-Type':'application/json'
}

history=[]

def generate_response(prompt):
    history.append({"role": "user", "content": prompt})
    
    data={
        "model":"CodeHelper",
        "messages":history,
        "stream":False
    }

    response=requests.post(url,headers=headers,json=data)
    
    if response.status_code == 200:
        data = response.json()
        bot_reply = data["message"]["content"]

        # Add bot reply to history
        history.append({"role": "assistant", "content": bot_reply})

        best_answer = f"""🤖 CodeHelper Response:
---

{bot_reply}

---

💡 Tip: You can ask follow-up questions anytime!
"""

        return best_answer
    else:
        return "Error: " + response.text

interface=gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(lines=2,placeholder="Enter your Question"),
    outputs=gr.Textbox(lines=20,placeholder="Response",interactive=False),
    title="Code Helper - Codellama:7b"
)
    
interface.launch()
  
