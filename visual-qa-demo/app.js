const state = { count: 0 };

const badge = document.getElementById("cart-count");
const toast = document.getElementById("toast");
const sheet = document.getElementById("sheet");

let hideTimer = null;

function flash(message) {
  toast.textContent = message;
  toast.hidden = false;
  clearTimeout(hideTimer);
  hideTimer = setTimeout(() => { toast.hidden = true; }, 2200);
}

function addToCart() {
  state.count += 1;
  badge.textContent = String(state.count);
  flash("Added to cart");
}

document.getElementById("add").addEventListener("click", addToCart);
document.getElementById("details").addEventListener("click", () => sheet.showModal());
document.getElementById("close-sheet").addEventListener("click", () => sheet.close());
document.getElementById("cart").addEventListener("click", () => {
  flash(state.count ? `${state.count} item(s) in your cart` : "Your cart is empty");
});
