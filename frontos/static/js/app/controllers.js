"use strict";

var frontosControllers = angular.module('frontosControllers', []);

frontosControllers.controller('UserListCtrl', ['$scope', '$http',
	function ($scope, $http) {
		$http.get('/frontks').success(function(data) {
			$scope.users = data;
		});
	}]);

frontosControllers.controller('UserLoginCtrl', ['$scope', '$http', 'UserService',
	function ($scope, $http, User) {
		$scope.credentials = {};
		$scope.auth = User.isLogged;
		$scope.submit = function() {
			if (this.credentials) {
				$http.post('/frontks/user/login', this.credentials)
				.success(function(data, status, headers, config) {
					User.isLogged = data.authenticated;
					$scope.auth = data.authenticated;
					User.username = 'admin';
				})
				.error(function(data) {
					User.isLogged = false;
				});
			}
		};
	}]);

frontosControllers.controller('UserShowCtrl', ['$scope', '$http' , "$routeParams",
	function ($scope, $http, $routeParams) {
		$http.get('/frontks/user', {params: {user_id: $routeParams.id}})
		.success(function(data) {
			$scope.user = data;
		});
	}]);

