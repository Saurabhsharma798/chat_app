

// const messages = [[]];
// let id = 0;

// const message = document.getElementById("message");


// const input_field = document.getElementById("username");


// function createNewChat(id) {
//     const history_container = document.getElementById("history-container");
//     const chatItem = document.createElement("div");
//     chatItem.className = "history-bar";
//     chatItem.innerText = `Chat ${id}`;
//     chatItem.onclick = function (){switchChat(id);};
//     history_container.appendChild(chatItem);
// }

// createNewChat(id);


// function switchChat(chatId) {
//     id=chatId;
//     renderMessages();
// }




// async function myfunc() {
//     // let mainBox = [];
//     const username = input_field.value;

//     messages[id].push({ role: 'user', text: username })

//     input_field.value = "";


//     try {
//         const response = await fetch("http://192.168.29.119:8000/chat", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify({ conversation_id:id,content: username })

//         });
//         console.log('here')

//         console.log('here also')
//         const data = await response.json();
//         messages[id].push({ role: 'ai', text: data.content })

//         console.log(messages);
//         renderMessages();
//         // messages[id].push(ma);
//     }

//     catch (error) {
//         console.log(error);
//     }
// }
// function renderMessages() {
//     const message = document.getElementById("message");
//     message.innerHTML = "";

//     messages[id].forEach(msg => {
//         const div = document.createElement("div");
//         div.className = msg.role === "user" ? "user-box" : "output";
//         div.textContent = msg.text;

//         message.appendChild(div);
//     });


//     message.scrollTop = message.scrollHeight;
// }

// input_field.addEventListener('keydown', function (event) {
//     if (event.key === 'Enter') {
//         myfunc()
//     }
// });

// function newChat() {
//     id++;
//     message.innerHTML = "";
//     messages[id] = [];
//     createNewChat(id);
//     renderMessages();

// }


// second


 
const messages = [[]];
let id = 0;
 
const message = document.getElementById("message");
 
 
const input_field = document.getElementById("username");
 
 
function createNewChat(id) {
    const history_container = document.getElementById("history-container");
    const chatItem = document.createElement("div");
    chatItem.className = "history-bar";
    chatItem.innerText = `Chat ${id}`;
    chatItem.onclick = function (){switchChat(id);};
    history_container.appendChild(chatItem);
}
 
createNewChat(id);
 
 
function switchChat(chatId) {
    id=chatId;
    loadChat(id);
    renderMessages();
}
 
 
 
async function loadChat(id) {
    try{    
        const response = await fetch("http://192.168.29.119:8000/chat_content",{
            method:"POST",
            headers:{
                "Content-Type":"application/json"
            },
            body:JSON.stringify({ conversation_id:id })
        })
        console.log("chat fetched")
        const data= await response.json()
        id=data.conversation_id
        for (const d in data.content){
            msg_role=d.role;
            msg_text=d.msg;
 
            messages[id].push({role:msg_role,text:msg_text})
            
        }
        console.log(messages)
        
    }
    catch (error){
        console.log(error);
    }
}
 
 
 
async function myfunc() {
    // let mainBox = [];
    const username = input_field.value;
 
    // messages[id].push({ role: 'user', text: username })
 
    input_field.value = "";
 
 
    try {
        const response = await fetch("http://192.168.29.119:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ conversation_id:id,content: username })
 
        });
        console.log('here')
 
        console.log('here also')
        const data = response.json();
        // messages[id].push({ role: 'ai', text: data.content })
 
        console.log(messages);
        renderMessages();
    }
 
    catch (error) {
        console.log(error);
    }
}
function renderMessages() {
    const message = document.getElementById("message");
    message.innerHTML = "";
 
    messages[id].forEach(msg => {
        const div = document.createElement("div");
        div.className = msg.role === "USER" ? "user-box" : "output";
        div.textContent = msg.text;
 
        message.appendChild(div);
    });
 
 
    message.scrollTop = message.scrollHeight;
}
 
input_field.addEventListener('keydown', function (event) {
    if (event.key === 'Enter') {
        myfunc()
    }
});
 
function newChat() {
    id++;
    message.innerHTML = "";
    messages[id] = [];
    createNewChat(id);
    renderMessages();
 
}

