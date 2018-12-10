function SignUp()  {
  var name = $("input[name='name']").val()
  var email=  $("input[name='email']").val()
  var pattern = /^([a-z0-9_\.-])+@[a-z0-9-]+\.([a-z]{2,4}\.)?[a-z]{2,4}$/i;

  name_is_valid = name.length != 0 && !/[^a-z]/i.test(name)
  email_is_valid = pattern.test(email)
  if (name_is_valid && email_is_valid) {

    $.ajax({
                   type: 'GET',
                   async: true,
                   url: 'http://127.0.0.1:8000/timetable/SignUp',
                   data: {"lessons":$('#lessons').text(),
                          "day":$('#day').text(),
                          "time":$('#time').text(),
                          "name":name,
                          "email":email,},
                   success: function(data) {
                    alert($("input[name='name']").val());
                   },
                   dataType: 'json',
      });
  } else {
    element = $('#nameHelp')

      if (element != null ) {
          element.text("Please enter a real name");
        }
    element = $('#emaiHelp')
        if (element != null ) {
          element.text("Please enter a real emai") ;
            }

  }

  };(jQuery);

function ShowModal(time,group,day)  {
  element = document.getElementById('lessons')
  if (element != null) {
    element.innerHTML =group ;
      }
  element = document.getElementById('day')
      if (element != null) {
        element.innerHTML =day ;
          }
  element = document.getElementById('time')
        if (element != null) {
          element.innerHTML =time ;
                  }
          $("#myModal").modal('show');
  }
