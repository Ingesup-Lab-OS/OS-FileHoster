"use strict";

var frontosServices = angular.module('frontosServices', []);

frontosServices.factory('UserService', function() {
	var current_user = {
		isLogged: false,
		username: ''
	};

	return current_user;
})