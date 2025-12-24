import ChatBox from "./components/ChatBox";
import Home from "../Home";
import { useState } from "react";

export default function App() {
  const [open, setOpen] = useState(false);

  return (
    <>
      <Home />

      <div className="chat-bubble" onClick={() => setOpen(!open)}>
        💬
      </div>

      {open && <ChatBox />}
    </>
  );
}