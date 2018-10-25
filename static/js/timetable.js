
(function($){
$(document).ready(function(){
 $("#ajax-text-me").click(function() {
  $.ajax({
                 type: 'GET',
                 async: true,
                 url: 'http://localhost:8000/timetable/ajax/',
                 data: "",
                 success: function(data) {
                     $("#more-text-here1").append(data['first-text']);
                     $("#more-text-here2").append(data['second-text']);

                 },
                 dataType: 'json',

    });


});

});})(jQuery);
