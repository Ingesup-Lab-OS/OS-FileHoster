(function () {
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
