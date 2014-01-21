var phonecatApp = angular.module('frontos', [
	'ngRoute',
	'frontosControllers'
]);

phonecatApp.config(['$routeProvider',
	function($routeProvider) {
		$routeProvider.
			when('/users', {
				templateUrl: 'static/partials/user-list.html',
				controller: 'UserListCtrl'
			}).
			otherwise({
				redirectTo: '/'
			});
	}
]);
