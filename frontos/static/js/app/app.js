(function() {
"use strict";

var frontosApp = angular.module('frontos', [
	'ngRoute',
	'frontos.controllers',
	'frontos.services',
	'frontos.directives'
]);

frontosApp.constant('urls', {
	user_login: 'static/partials/user/login.html',
	user_list: 'static/partials/user/list.html',
	file_new: 'static/partials/file/new.html',
	user_show: 'static/partials/user/show.html'
});

frontosApp.config(['$httpProvider', '$locationProvider', '$routeProvider', 'urls',
	function($httpProvider, $locationProvider, $routeProvider, urls) {
		$httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
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
			when('/file/new', {
				templateUrl: urls.file_new,
				controller: 'FileUploadCtrl'
			}).
			otherwise({
				redirectTo: '/'
			});
	}]);
})();
