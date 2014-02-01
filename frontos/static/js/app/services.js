(function() {
"use strict";

var services = angular.module('frontos.services', []);

services.factory('UserService',
	function() {
		var current_user = {
			isLogged: false,
			username: ''
		};

		return current_user;
	});
})();
