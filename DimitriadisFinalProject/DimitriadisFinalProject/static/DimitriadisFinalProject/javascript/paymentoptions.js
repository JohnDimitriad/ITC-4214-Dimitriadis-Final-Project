function togglePaymentFields() {
    const method = document.querySelector("#payment_method").value;

    document.querySelector("#credit_card_fields").style.display = "none";
    document.querySelector("#paypal_fields").style.display = "none";
    document.querySelector("#cash_message").style.display = "none";

    if (method === "credit_card") {
        document.querySelector("#credit_card_fields").style.display = "block";
    } else if (method === "paypal") {
        document.querySelector("#paypal_fields").style.display = "block";
    } else if (method === "cash") {
        document.querySelector("#cash_message").style.display = "block";
    }
}