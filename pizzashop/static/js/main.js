$(document).ready(function () {
    // orderForm
	let orderForm = $('#order-form');
	orderForm.on('submit', function (e) {
        e.preventDefault();
        let count = $('#count').val();
        let submitBtn = $('#submit-btn');
        let itemId = submitBtn.data('item_id');
        let itemName = submitBtn.data('name');
        let itemPrice = submitBtn.data('price');
        console.log(itemId + ' ' + itemName + ' ' + itemPrice);

        $('.basket__ul').append('<li class="basket__item">' + itemName + ' ' + count + ' ' + 'шт. ' + (itemPrice *  count) + ' руб.</li>');

    });

	$('.basket__text').on('click', function (e) {
        e.preventDefault();
        $('.basket').toggleClass('hidden');
    });
});
