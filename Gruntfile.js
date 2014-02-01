module.exports = function(grunt) {

	// Project configuration.
	grunt.initConfig({
		pkg: grunt.file.readJSON('package.json'),
		watch: {
			options: {
				livereload: true
			},
			js: {
				files: ['frontos/static/js/app/*.js'],
				tasks: ['concat'],
			},
			html: {
				files: [
					'frontos/static/partials/*.html',
				 	'frontos/static/partials/**/*.html',
				 	'frontos/templates/*.html',
				 	'frontos/templates/**/*.html'
				 ],
				tasks: [],
			}
		},
		concat: {
			options: {
				separator: ';'
			},
			angular: {
				files: {
					'frontos/static/js/dest/app.js': [
						'frontos/static/js/app/*.js',
					]
				}
			},
			libs:{
				files: {
					'frontos/static/js/dest/libs.js': [
						'frontos/static/vendors/angular/angular.min.js',
						'frontos/static/vendors/angular-resource/angular-resource.min.js',
						'frontos/static/vendors/angular-route/angular-route.min.js',
						'frontos/static/vendors/ng-file-upload/angular-file-upload-shim.min.js',
						'frontos/static/vendors/ng-file-upload/angular-file-upload.min.js',
					]
				}
			}
		},
		uglify: {
			minify: {
				files: {
					'frontos/static/js/dest/app.min.js': [
						'frontos/static/js/dest/app.js',
						'frontos/static/js/dest/ang-lib.js',
						'frontos/static/js/dest/jquery-lib.js'
					]
				}
			}
		}
	});

	// Load plugins
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.loadNpmTasks('grunt-contrib-concat');
	grunt.loadNpmTasks('grunt-contrib-uglify');

	// Default task(s).
	grunt.registerTask('default', ['watch']);

};
