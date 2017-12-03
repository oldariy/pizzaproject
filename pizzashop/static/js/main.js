window.onload = function () {
	'use strict';

	let orderForm = document.querySelector('#order-form');
	orderForm.addEventListener('submit', function(e) {
        e.preventDefault();
        let count = document.querySelector('#count');
        console.log(count);
        let itemName = document.querySelector('#submit-btn').getAttribute('data-name');
        console.log(itemName);
	});
	
};
