// Когда html документ готов (прорисован)
$(document).ready(function () {
    let successMessage = $("#jq-notification");

    $(document).on("click", ".add-to-cart", function (e) {
        e.preventDefault();

        let goodsInCartCount = $("#goods-in-cart-count");
        let cartCount = parseInt(goodsInCartCount.text() || 0);
        let product_id = $(this).data("product-id");
        let add_to_cart_url = $(this).attr("href");

        $.ajax({
            type: "POST",
            url: add_to_cart_url,
            data: {
                product_id: product_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);

                cartCount++;
                goodsInCartCount.text(cartCount);

                let cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);
            },

            error: function (data) {
                console.log("Ошибка при добавлении товара в корзину");
            },
        });
    });

    $(document).on("click", ".remove-from-cart", function (e) {
        e.preventDefault();

        let goodsInCartCount = $("#goods-in-cart-count");
        let cartCount = parseInt(goodsInCartCount.text() || 0);

        let cart_id = $(this).data("cart-id");
        let remove_from_cart = $(this).attr("href");

        $.ajax({
            type: "POST",
            url: remove_from_cart,
            data: {
                cart_id: cart_id,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },
            success: function (data) {
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);

                cartCount -= data.quantity_deleted;
                goodsInCartCount.text(cartCount);

                let cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);
            },

            error: function (data) {
                console.log("Помилка при додаванні до корзини");
            },
        });
    });

    $(document).on("click", ".decrement", function () {
        let url = $(this).data("cart-change-url");
        let cartID = $(this).data("cart-id");
        let $input = $(this).closest('.input-group').find('.number');
        let currentValue = parseInt($input.val());
        if (currentValue > 1) {
            $input.val(currentValue - 1);
            updateCart(cartID, currentValue - 1, -1, url);
        }
    });

    $(document).on("click", ".increment", function () {
        let url = $(this).data("cart-change-url");
        let cartID = $(this).data("cart-id");
        let $input = $(this).closest('.input-group').find('.number');
        let currentValue = parseInt($input.val());

        $input.val(currentValue + 1);

        updateCart(cartID, currentValue + 1, 1, url);
    });

    function updateCart(cartID, quantity, change, url) {
        $.ajax({
            type: "POST",
            url: url,
            data: {
                cart_id: cartID,
                quantity: quantity,
                csrfmiddlewaretoken: $("[name=csrfmiddlewaretoken]").val(),
            },

            success: function (data) {
                successMessage.html(data.message);
                successMessage.fadeIn(400);
                setTimeout(function () {
                    successMessage.fadeOut(400);
                }, 7000);

                let goodsInCartCount = $("#goods-in-cart-count");
                let cartCount = parseInt(goodsInCartCount.text() || 0);
                cartCount += change;
                goodsInCartCount.text(cartCount);

                let cartItemsContainer = $("#cart-items-container");
                cartItemsContainer.html(data.cart_items_html);
            },
            error: function (data) {
                console.log("Помилка при додаванні товара до корзини");
            },
        });
    }

    let notification = $('#notification');
    if (notification.length > 0) {
        setTimeout(function () {
            notification.alert('close');
        }, 7000);
    }

    $('#modalButton').click(function () {
        $('#exampleModal').appendTo('body');
        $('#exampleModal').modal('show');
    });

    $('#exampleModal .btn-close').click(function () {
        $('#exampleModal').modal('hide');
    });

    $("input[name='requires_delivery']").change(function() {
        let selectedValue = $(this).val();
    });

   const paymentOptions = document.querySelectorAll('.payment-option');

    function changeActiveOption() {
        paymentOptions.forEach(option => {
            option.classList.remove('active');
        });
        this.classList.add('active');
        const radioButton = this.querySelector('input[type="radio"]');
        radioButton.checked = true;
    }

    paymentOptions.forEach(option => {
        option.addEventListener('click', changeActiveOption);
    });

});
