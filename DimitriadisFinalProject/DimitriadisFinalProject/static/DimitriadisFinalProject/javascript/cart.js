document.addEventListener("DOMContentLoaded", function () {
    let cart = JSON.parse(localStorage.getItem("cart")) || [];

    function saveCart() {
        localStorage.setItem("cart", JSON.stringify(cart));
    }

    function renderCartItems() {
        const cartContainer = document.querySelector("#cart-items");
        const cartTotalContainer = document.querySelector("#cart-total");

        if (!cartContainer) return;

        cartContainer.innerHTML = "";
        let total = 0;

        if (cart.length === 0) {
            cartContainer.innerHTML = "<p>Your cart is empty!</p>";
            cartTotalContainer.textContent = "Total: $0.00";
            return;
        }

        cart.forEach((item, index) => {
            const itemElement = document.createElement("div");
            itemElement.className = "cart-item";
            itemElement.innerHTML = `
                <p><strong>${item.title}</strong> - $${item.price}</p>
                <button class="btn btn-sm btn-danger remove-item" data-index="${index}">Remove</button>
            `;
            cartContainer.appendChild(itemElement);
            total += item.price;
        });

        cartTotalContainer.textContent = `Total: $${total.toFixed(2)}`;

        document.querySelectorAll(".remove-item").forEach(button => {
            button.addEventListener("click", function () {
                const index = this.dataset.index;
                cart.splice(index, 1);
                saveCart();
                renderCartItems();
            });
        });
    }

    const addToCartButton = document.querySelector("#add-to-cart");
    if (addToCartButton) {
        addToCartButton.addEventListener("click", function () {
            const movieTitle = this.dataset.title;
            const moviePrice = parseFloat(this.dataset.price);

            const movie = {
                title: movieTitle,
                price: moviePrice,
            };

            cart.push(movie);
            saveCart();
            alert(`${movieTitle} has been added to your cart!`);
        });
    }

    const placeOrderButton = document.querySelector("#place-order");
    if (placeOrderButton) {
        placeOrderButton.addEventListener("click", function (e) {
            e.preventDefault();

            cart = [];
            saveCart();

            const cartContainer = document.querySelector("#cart-items");
            const cartTotalContainer = document.querySelector("#cart-total");

            cartContainer.innerHTML = "<p>Thank you for your order! The movie files have been sent to you via email</p>";
            cartTotalContainer.textContent = "Total: $0.00";
        });
    }

    renderCartItems();
});
