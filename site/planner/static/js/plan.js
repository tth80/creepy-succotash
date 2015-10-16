siteApp.controller('planController', function($scope, APIService, $http) {
    $scope.plans = function() {
        return $http({method:'get', url:'api/plans/'});
    };

    $scope.plan = function(id) {
        return $http({method:'get', url:'api/plan/' + escape(id) + '/'});
    };

    $scope.active_project = null;
    $scope.activate_project = function(id) {
        $scope.plan(id).success(function(obj) {
            $scope.active_project = obj;
        });
    };

    $scope.activate_task = function(task) {
        $scope.active_task = task;
        console.log('active task changed');
        console.log(task);
    };

    $scope.plans().success(function(obj) {
        $scope.projects = obj.plans;
        $scope.activate_project($scope.projects[0].id);
    });

});

