angular.module('SiteApp.services', [])
.factory('APIService', function($http) {
    var API = {};

    API.get = function(section) {
        return $http({
            method:'get',
            url:'/api/' + escape(section) + '/',
        });
    };

    return API;
});

angular.module('SiteApp.controllers', [])
.controller('siteController', function($scope, APIService) {
    $scope.user = {};

    APIService.get('user').success(function(data) { $scope.user = data; });
});

var siteApp = angular.module('SiteApp', [
    'SiteApp.services',
    'SiteApp.controllers']);
