$(function() {
    $('.new-dojo').scheduler({
        dialogCallback: function(schedulerCallback) {
            schedulerCallback({
                title:'Some Dojo'
            });
        }
    });
});