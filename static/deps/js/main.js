// main.js

document.addEventListener("DOMContentLoaded", function () {
    var quantityInput = document.getElementById('quantity');
    var addToCartBtn = document.getElementById('addToCartBtn');
    var continueShoppingBtn = document.getElementById('continueShoppingBtn');
    var checkoutBtn = document.getElementById('checkoutBtn');
    var additionalButtons = document.querySelector('.additional-buttons');

    // Отримання імені товару через атрибут data
    var productName = document.getElementById('productCard').getAttribute('data-product-name');

    // Функція відображення модального вікна
    function showModal(message) {
        var modal = document.getElementById('myModal');
        var modalMessage = document.getElementById('modal-message');

        modalMessage.innerText = message;

        modal.style.display = 'block';

        // Закриття модального вікна при натисканні на "x"
        var closeBtn = document.getElementsByClassName('close')[0];
        closeBtn.addEventListener('click', function () {
            modal.style.display = 'none';
        });

        // Закриття модального вікна при кліканні поза вікном
        window.addEventListener('click', function (event) {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        });
    }

    // Обробник події для кнопки "Додати до кошика"
    addToCartBtn.addEventListener('click', function () {
        var quantity = parseInt(quantityInput.value);
        // Логіка для додавання товару до кошика

        // Відображення модального вікна
        showModal(productName + ' додано до корзини.');

        // Відображення додаткових кнопок
        additionalButtons.style.display = 'flex';
    });

    // Обробник події для кнопки "Продовжити покупки"
    continueShoppingBtn.addEventListener('click', function () {
        // Логіка для продовження покупок
        showModal('Продовжуйте свої покупки.');
    });

    // Обробник події для кнопки "Оформити замовлення"
    checkoutBtn.addEventListener('click', function () {
        // Логіка для оформлення замовлення
        showModal('Оформте своє замовлення.');
    });

});
