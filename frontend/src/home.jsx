export default function Home() {
  const products = [
    { id: 1, nombre: "Poncho de lana artesanal", precio: 45000 },
    { id: 2, nombre: "Camisa gaucha blanca", precio: 28000 },
    { id: 3, nombre: "Bombacha de campo marrón", precio: 32000 }
  ];

  return (
    <div className="home">
      <h1>Llaqta — Ropa de campo</h1>
      <div className="grid">
        {products.map(p => (
          <div key={p.id} className="card">
            <h3>{p.nombre}</h3>
            <p>${p.precio}</p>
          </div>
        ))}
      </div>
    </div>
  );
}