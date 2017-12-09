$(document).ready(function () {
	// orderForm
	var orderForm = $('.order-form');

	orderForm.on('submit', function (e) {
		e.preventDefault();
		var count = $(this).find('#count').val();
		var submitBtn = $(this).find('#submit-btn');
		var itemId = submitBtn.data('item_id');
		var itemName = submitBtn.data('name');
		var itemPrice = submitBtn.data('price');
		console.log(itemId + ' ' + itemName + ' ' + itemPrice);
		
		
		var data = {};
		data.itemId = itemId;
		data.count = count;
		var csrf_token = $('#csrf [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;
		
		var url = orderForm.attr('action');
		
		console.log(data);
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			success: function (data) {
				console.log("OK");
				
				console.log(data['items_total_count']);
				if (data['items_total_count'] || data['items_total_count'] == 0) {
					$('#basket_total_count').text("(" + data['items_total_count'] + ")");
					$('.basket__ul').html("");
					$.each(data.items, function (k, v) {
						$('.basket__ul').append('<li class="basket__item">' + v.name + ' ' + v.count + ' ' + 'шт. ' + (v.price_per_item * v.count) + ' руб. '
							+ '<a class="delete-item" href="" data-item_id="' + v.id + '"><i class="mdl-icon">clear</i></a>' + '</li>');
					});
					
				}
			},
			error: function () {
				console.log("error")
			}
		});
		
		
	});
	
	
	$('.basket__text').on('click', function (e) {
		e.preventDefault();
		$('.basket').toggleClass('hidden');
	});
	
	$(document).on('click', '.delete-item', function (e) {
		e.preventDefault();
		itemId = $(this).data("item_id");
		console.log("itemId = " + itemId);
		count = 0;
		var data = {};
		data.itemId = itemId;
		data.count = count;
		var csrf_token = $('#csrf [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;
		
		data["is_delete"] = true;
		
		var url = $('#csrf').attr("action");
		
		console.log(data);
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			success: function (data) {
				console.log("OK");
				
				console.log(data['items_total_count']);
				if (data['items_total_count'] || data['items_total_count'] == 0) {
					$('#basket_total_count').text("(" + data['items_total_count'] + ")");
					$('.basket__ul').html("");
					$.each(data.items, function (k, v) {
						$('.basket__ul').append('<li class="basket__item">' + v.name + ' ' + v.count + ' ' + 'шт. ' + (v.price_per_item * v.count) + ' руб. '
							+ '<a class="delete-item" href="" data-item_id="' + v.id + '"><i class="mdl-icon">clear</i></a>' + '</li>');
					});
					
				}
				
			},
			error: function () {
				console.log("error")
			}
		});
	});

	$(document).on('click', '.delete-item-checkout', function (e) {
		e.preventDefault();
		itemId = $(this).data("item_id");
		console.log("itemId = " + itemId);
		count = 0;
		var data = {};
		data.itemId = itemId;
		data.count = count;
		var csrf_token = $('#csrf [name="csrfmiddlewaretoken"]').val();
		data["csrfmiddlewaretoken"] = csrf_token;

		data["is_delete"] = true;

		var url = $('#csrf').attr("action");

		console.log(data);
		$.ajax({
			url: url,
			type: 'POST',
			data: data,
			cache: true,
			success: function (data) {
				console.log("OK");

				console.log(data['items_total_count']);
				if (data['items_total_count'] || data['items_total_count'] == 0) {
					location.reload();
				}

			},
			error: function () {
				console.log("error")
			}
		});
	});



	var dialog = document.querySelector('dialog');

	if (dialog) {
		var showModalButton = document.querySelector('.show-modal');
		if (!dialog.showModal) {
			dialogPolyfill.registerDialog(dialog);
		}
		showModalButton.addEventListener('click', function () {
			dialog.showModal();
		});
		dialog.querySelector('.close').addEventListener('click', function () {
			dialog.close();
		});
	}


	
	function calcBasketAmount() {
		var total_order_amount = 0;
		$('.total_item_in_basket_amount').each(function () {
			total_order_amount += parseInt($(this).text());
		});
		$('#basket_total_amount').text(total_order_amount);
	}

	$(document).on('change', '.item-in-basket-count', function () {
		var currentCount = $(this).val();
		var currentTr = $(this).closest('tr');
		var currentPrice = parseInt(currentTr.find('.item-price').text());
		var totalAmount = currentPrice * currentCount;
		currentTr.find('.total_item_in_basket_amount').text(totalAmount);

		calcBasketAmount();


	});

	calcBasketAmount();


});
