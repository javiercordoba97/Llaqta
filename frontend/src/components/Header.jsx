import { Link } from "react-router-dom";
import fondo3 from "../assets/img/fondo3.jpg";

export default function Header() {
  return (
    <header className="header">
      <Link to="/" className="logo">La Tranquera</Link>

      <input
        type="text"
        placeholder="Buscar productos..."
        className="search-input"
      />

      <div></div>
    </header>
  );
}