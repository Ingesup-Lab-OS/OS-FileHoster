"use strict";

var frontosApp = angular.module('frontos', [
	'ngRoute',
	'frontosControllers',
	'frontosServices',
	'frontosDirectives'
]);

frontosApp.constant('urls', {
	user_login: 'static/partials/user/login.html',
	user_list: 'static/partials/user/list.html',
	user_show: 'static/partials/user/show.html'
});

frontosApp.config(['$httpProvider', '$locationProvider', '$routeProvider', 'urls',
	function($httpProvider, $locationProvider, $routeProvider, urls) {
		$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
		$httpProvider.defaults.xsrfCookieName = 'csrftoken';
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
		// $locationProvider.html5Mode(true).hashPrefix('!');
		$routeProvider.
			when('/login', {
				templateUrl: urls.user_login,
				controller: 'UserLoginCtrl'
			}).
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

