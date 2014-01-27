var frontosControllers = angular.module('frontosControllers', []);

frontosControllers.controller('UserListCtrl', ['$scope', '$http',
	function ($scope, $http) {
		$http.get('/frontks').success(function(data) {
			$scope.users = data;
		});
	}]);

frontosControllers.controller('UserShowCtrl', ['$scope', '$http' , "$routeParams",
	function ($scope, $http, $routeParams) {
		$http.get('/frontks/user', {method: 'GET', params: {user_id: $routeParams.id}}).
			success(function(data) {
				$scope.user = data;
			});
	}]);

