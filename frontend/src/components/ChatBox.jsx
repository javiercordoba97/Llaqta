import { useState, useEffect } from "react";
import { sendMessage } from "../services/api";
import Message from "./Message";
import InputBox from "./InputBox";

export default function ChatBox() {
  const [messages, setMessages] = useState([]);

  // Saludo inicial del bot
useEffect(() => {
  setMessages([
    { from: "bot", text: "Hola, soy LlaqtaBot ¿en qué te puedo ayudar? 😊" }
  ]);
}, []);
  const handleSend = async (text) => {
    // Mostrar mensaje del usuario
    setMessages((prev) => [...prev, { from: "user", text }]);

    // Llamar al backend
    const response = await sendMessage(text);

    let botText = "";

    // Caso 1: nutrición
    if (response.type === "nutrition") {
      botText = JSON.stringify(response.data, null, 2);
    }

    // Caso 2: general
    else if (response.type === "general") {
      botText = response.data;
    }

    // Caso 3: error
    else {
      botText = "Hubo un error interpretando la respuesta del modelo.";
    }

    // Mostrar mensaje del bot
    setMessages((prev) => [...prev, { from: "bot", text: botText }]);
  };

  return (
    <div className="chatbox">
      {messages.map((msg, i) => (
        <Message key={i} from={msg.from} text={msg.text} />
      ))}

      <InputBox onSend={handleSend} />
    </div>
  );
}