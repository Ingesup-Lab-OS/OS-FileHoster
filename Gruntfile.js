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
				tasks: ['concat:angular'],
			},
			html: {
				files: ['frontos/static/partials/*.html', 'frontos/static/partials/**/*.html', 'frontos/templates/*.html', 'frontos/templates/**/*.html'],
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
			lib:{
				files: {
					'frontos/static/js/dest/lib.js': [
						'frontos/static/js/lib/angular/angular.js',
						'frontos/static/js/lib/angular-resource/angular-resource.js',
						'frontos/static/js/lib/angular-route/angular-route.js',
						'frontos/static/js/lib/jquery/jquery.js',
					]
				}
			}
		},
		uglify: {
			minify: {
				files: {
					'frontos/static/js/dest/app.min.js': ['frontos/static/js/dest/app.js', 'frontos/static/js/dest/lib.js']
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
