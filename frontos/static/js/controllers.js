var frontosControllers = angular.module('frontosControllers', []);

frontosControllers.controller('UserListCtrl', ['$scope', '$http',
	function ($scope, $http) {
		$http.get('static/users.json').success(function(data) {
			$scope.users = data;
		});
	}
]);
