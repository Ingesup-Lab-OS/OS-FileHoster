(function() {
"use strict";

var frontosApp = angular.module('frontos', [
	'ngRoute',
	'frontos.controllers',
	'frontos.services',
	'frontos.directives'
]);

frontosApp.constant('urls', {
	user_login: 'partials/user/login.html',
	user_list: 'partials/user/list.html',
	file_new: 'partials/file/new.html',
	user_show: 'partials/user/show.html'
});

frontosApp.config(['$httpProvider', '$locationProvider', '$routeProvider', 'urls',
	function($httpProvider, $locationProvider, $routeProvider, urls) {
		delete $httpProvider.defaults.headers.common['X-Requested-With'];
		$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
		$httpProvider.defaults.xsrfCookieName = 'csrftoken';
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
			when('/uploader', {
				templateUrl: urls.file_new,
				controller: 'FileUploadCtrl'
			}).
			otherwise({
				redirectTo: '/'
			});
	}]);
})();
