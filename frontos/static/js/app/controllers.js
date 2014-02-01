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

controllers.controller('FileUploadCtrl', ['$scope',
	function($scope) {
	      $scope.progress = function(percentDone) {
	            console.log("progress: " + percentDone + "%");
	      };

	      $scope.done = function(files, data) {
	            console.log("upload complete");
	            console.log("data: " + JSON.stringify(data));
	            writeFiles(files);
	      };

	      $scope.getData = function(files) {
	            //this data will be sent to the server with the files
	            return {msg: "from the client", date: new Date()};
	      };

	      $scope.error = function(files, type, msg) {
	            console.log("Upload error: " + msg);
	            console.log("Error type:" + type);
	            writeFiles(files);
	      }

	      function writeFiles(files)
	      {
	            console.log('Files')
	            for (var i = 0; i < files.length; i++) {
	                  console.log('\t' + files[i].name);
	            }
	      }
	}]);
})();
