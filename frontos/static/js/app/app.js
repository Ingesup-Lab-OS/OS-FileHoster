var phonecatApp = angular.module('frontos', [
	'ngRoute',
	'frontosControllers'
]);

phonecatApp.constant('urls', {
	user_list: 'static/partials/user/list.html',
	user_show: 'static/partials/user/show.html'
});



phonecatApp.config(['$httpProvider', '$locationProvider', '$routeProvider', 'urls',
	function($httpProvider, $locationProvider, $routeProvider, urls) {
		$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
		// $locationProvider.html5Mode(true).hashPrefix('!');
		$routeProvider.
			when('/users', {
				templateUrl: urls.user_list,
				controller: 'UserListCtrl'
			}).
			when('/user/:id', {
				templateUrl: urls.user_show,
				controller: 'UserShowCtrl'
			}).

			otherwise({
				redirectTo: '/'
			});
	}]);

