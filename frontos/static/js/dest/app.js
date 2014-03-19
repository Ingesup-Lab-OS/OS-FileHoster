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
;(function () {
	"use strict";

var controllers = angular.module('frontos.controllers', ['angularFileUpload']);

controllers.controller('UserListCtrl', ['$scope', '$http',
	function ($scope, $http) {
		$http.get('http://127.0.0.1:8000/frontks').success(function(data) {
			$scope.users = data;
		});
	}]);

controllers.controller('UserLoginCtrl', ['$scope', '$http', 'UserService',
	function ($scope, $http, User) {
		$scope.credentials = {};
		$scope.user = User;
		$scope.auth_token = 'unkown';
		$scope.submit = function() {
			if (this.credentials) {
				$http.post('http://127.0.0.1:8000/frontks/user/login', this.credentials)
				.success(function(data, status, headers, config) {
					$scope.user.isLogged = data.authenticated;
					$scope.auth_token = data.auth_token;
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


controllers.controller('FileUploadCtrl', [ '$scope', '$upload',
	function($scope, $upload) {
		$scope.percentDone = 0;
		$scope.onFileSelect = function($files) {
			//$files: an array of files selected, each file has name, size, and type.
			for (var i = 0; i < $files.length; i++) {
				var file = $files[i];
				$scope.percentDone = 0;
				$scope.upload = $upload.upload({
					url: 'http://127.0.0.1:8000/frontks/files/new/', //upload.php script, node.js route, or servlet url
					method: 'POST',
					headers: { "Content-Type": file.type },
					// withCredential: true,
					data: {myObj: $scope.myModelObj},
					file: file,
					// file: $files, //upload multiple files, this feature only works in HTML5 FromData browsers
					/* set file formData name for 'Content-Desposition' header. Default: 'file' */
					//fileFormDataName: myFile, //OR for HTML5 multiple upload only a list: ['name1', 'name2', ...]
					/* customize how data is added to formData. See #40#issuecomment-28612000 for example */
					//formDataAppender: function(formData, key, val){}
				}).progress(function(ev) {
					$scope.percentDone = parseInt(100.0 * ev.loaded / ev.total);
					console.log('percent: ' + $scope.percentDone);
				}).success(function(data) {
					console.log('data :');
					console.log(data);
				}).error(function(data) {
						//error
				});
			}
		};
	}]);
})();
;(function() {
"use strict";

var directives = angular.module('frontos.directives', [
	'frontos.services'
]);
})();
;(function() {
"use strict";

var services = angular.module('frontos.services', []);

services.factory('UserService',
	function() {
		var current_user = {
			isLogged: false,
			username: ''
		};

		return current_user;
	});
})();
