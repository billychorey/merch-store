function ProductCard({ product }) {
  return (
    <div className="border rounded-xl p-4 shadow-md bg-white">
      <h2 className="text-xl font-semibold mb-2">{product.title}</h2>
      <p className="text-gray-700">${product.price.toFixed(2)}</p>
    </div>
  );
}

export default ProductCard;
