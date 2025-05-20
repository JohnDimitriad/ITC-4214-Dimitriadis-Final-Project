document.addEventListener("DOMContentLoaded", function () {
    const currentUser = document.body.getAttribute('data-username') || '';

    if (!currentUser) {
        // If user not logged in, you can choose to:
        // - Show empty cart or a message
        // - Or use a generic 'cart_guest' key if you want guest carts
        // For now, just stop:
        console.log("No user logged in, no cart shown.");
        return;
    }

    const cartKey = `cart_${currentUser}`;
    let cart = JSON.parse(localStorage.getItem(cartKey)) || [];

    function saveCart() {
        localStorage.setItem(cartKey, JSON.stringify(cart));
    }

    const lastUser = localStorage.getItem('lastUser');
        if (lastUser !== currentUser) {
            // User changed, clear cart display and reset
            cart = [];
            saveCart();
        }
    localStorage.setItem('lastUser', currentUser);
    

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
                <p><strong>${item.title}</strong> - $${item.price} x ${item.quantity}</p>
                <button class="btn btn-sm btn-danger remove-item" data-index="${index}">Remove</button>
            `;
            cartContainer.appendChild(itemElement);
            total += item.price * item.quantity;  // Multiply by quantity to get total price
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
            const quantity = parseInt(document.querySelector("#quantity").value);  // Get quantity from input field

            const movie = {
                title: movieTitle,
                price: moviePrice,
                quantity: quantity,  // Use quantity from input field
            };

            cart.push(movie);
            saveCart();
            alert(`${movieTitle} has been added to your cart with quantity: ${quantity}!`);
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

            cartContainer.innerHTML = "<p>Thank you for your order! The movie files have been sent to you via email.</p>";
            cartTotalContainer.textContent = "Total: $0.00";
        });
    }

    renderCartItems();
});