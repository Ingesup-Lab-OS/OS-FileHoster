(function () {
"use strict";

var controllers = angular.module('frontos.controllers', []);

controllers.controller('UserListCtrl', ['$scope', '$http',
	function ($scope, $http) {
		$http.get('/frontks').success(function(data) {
			$scope.users = data;
		});
	}]);

controllers.controller('UserLoginCtrl', ['$scope', '$http', 'UserService',
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

controllers.controller('UserShowCtrl', ['$scope', '$http' , "$routeParams",
	function ($scope, $http, $routeParams) {
		$http.get('/frontks/user', {params: {user_id: $routeParams.id}})
		.success(function(data) {
			$scope.user = data;
		});
	}]);

controllers.controller('FileUploadCtrl',
	['$scope', '$rootScope', 'uploadManager',
	function ($scope, $rootScope, uploadManager) {
		$scope.files = [];
		$scope.percentage = 0;

		$scope.upload = function () {
			uploadManager.upload();
			$scope.files = [];
		};

		$rootScope.$on('fileAdded', function (e, call) {
			$scope.files.push(call);
			$scope.$apply();
		});

		$rootScope.$on('uploadProgress', function (e, call) {
			$scope.percentage = call;
			$scope.$apply();
		});
	}]);
})();
