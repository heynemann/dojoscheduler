$.fn.scheduler = function(options){
  $.each(this, function() {
     $element = $(this);
     applyEvents($element);
  });
  
  function applyEvents($element) {
      $element.click(function() {
          if (! $.isAuthenticated()){
              alert('You must be authenticated before scheduling a new dojo.');
              return false;
          }
          if (options) {
              options.dialogCallback(function(data){
                  $.post('/dojo/create', data);
              });
          }
          return false;
      });
  }
};