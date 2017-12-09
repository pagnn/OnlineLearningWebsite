 function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
 $(document).ready(function(){
        var dataurl=$('.load-comments').attr('data-url')
        $('.load-comments').after("<div class='form-container'></div>")
        var isUser=false
        var authUsername;
        getComments(dataurl)
        function renderCommentLine(object){
          var authorImage="<div class='media-left'>"+"<img class='c-user-image media-object' src='"+object.image+"' alt='...'></div>"
          var author = ""
          if(object.user){
            author="<small> via "+object.user.username+"</small>"
            if(authUsername == object.user.username){
              edithtml='<a class="edit-button btn btn-link" href="#">Edit</a>'
            }
          }
          var timestamp=new Date(object.timestamp).toLocaleString()
          var contentHTML=authorImage+'<div class="media-body">'+'<p class="content-holder" data-id="'+object.id+'">'+object.content+'</p>'+author+'<small> on '+timestamp+'</small></div>'
          
          if(authUsername == object.user.username){
            contentHTML+='<a class="edit" href="#">Edit</a>'
          }
          var html_='<div class="c-media media">'+contentHTML+'</div>'
          return html_
        }
        function getComments(requestUrl){
          isUser=getCookie('isUser')
          authUsername=getCookie('authUsername')
        $.ajax({
          method:'GET',
          url:"http://127.0.0.1:8000/api/comments/",
          data:{
            url:dataurl,
          },
          success:function(data){
            if (data.length > 0 ){
              $('.load-comments').html("<h3>Comments</h3>")
              $.each(data,function(index,object){
                $('.load-comments').append(renderCommentLine(object))

              })               
            }

            var formHtml=generateForm()
            $('.form-container').html(formHtml)


          },
          error:function(data){
            console.log('error')
          }
        })
        }

        function generateForm(){
          var formHtml="<form class='comment-form' method='POST' ><textarea class='form-control my-3' name='content' placeholder='Comment...'></textarea>"
          +"<input class='btn btn-default' type='submit' value='Comment'></form>"
          if(isUser){
            return formHtml 
          }else{
            return '<div class="text-center my-3">Login Required to Comment.</div>'
          }
               
        }
        function formErrorMsg(jsonResponse){
          var msg=""
          $.each(jsonResponse,function(key,value){
            if(key == 'detail'){
              msg+=value+'<br/>'
            }else{
              msg+=key+":"+value+'<br/>'
            } 
          })
          var formattedMsg="<div class='srvup-alert-error alert alert-danger alert-dismissible'>"+
          "<button type='button' class='close' data-dismiss='alert' aria-label='Close'><span aria-hidden='true'>&times;</span></button>"+
          msg +
          "</div>"
          return formattedMsg
        }
        function handleForm(formData){
          $.ajax({
            method:'POST',
            url:"http://127.0.0.1:8000/api/comments/create/",
            data:formData+"&url="+dataurl,
            success:function(data){
              $('.load-comments').append(renderCommentLine(data))
            var formHtml=generateForm()
            $('.form-container').html(formHtml)              

            },
            error:function(data){
              var formErrorExists=$('.srvup-alert-error')
              if(formErrorExists.length > 0){
                formErrorExists.remove()
              }
              var msg=formErrorMsg(data.responseJSON)
              $('.comment-form textarea').before(msg)
            }
          })
        }
        $(document).on('submit','.comment-form',function(e){
          e.preventDefault()
          var formData=$(this).serialize()
          handleForm(formData)
        })
        $(document).on('click','.edit',function(e){
          e.preventDefault()
          $(this).fadeOut()
          var contentHolder=$(this).parent().find('.media-body').find('.content-holder')
          var contentTxt=contentHolder.text()
          var objectId=contentHolder.attr('data-id')
          formHtml=generateEditForm(objectId,contentTxt)
          $(this).parent().after(formHtml)
        })
        $(document).on('submit','.edit-form',function(e){
          e.preventDefault()
          var formData=$(this).serialize()
          var objectId=$(this).attr('data-id')

          handleEditForm(formData,objectId)
        })
        $(document).on('click','.cancel-button',function(e){
          e.preventDefault()
          $(this).parent().remove()
          $(this).parent().parent().find('.edit').fadeIn()
        })
        $(document).on('click','.delete-button',function(e){
          e.preventDefault()
          var objectId=$(this).parent().attr('data-id')
          $.ajax({
            method:'DELETE',
            url:"http://127.0.0.1:8000/api/comments/"+objectId+"/",
            success:function(data){
              getComments(dataurl)
            },
            error:function(data){
              cons
            }
          })
        })
        function generateEditForm(objectId,content){
          var formHtml="<form class='edit-form' method='POST' data-id='"+objectId+"'><textarea class='form-control my-3' name='content' placeholder='Comment...'>"+content+"</textarea>"
          +"<input class='btn btn-primary' type='submit' value='Save Edit'><button class='btn btn-default cancel-button'>Cancel</button><button class='btn btn-danger delete-button'>Delete</button></form>"
          return formHtml 
               
        }        
        function handleEditForm(formData,objectId){
          $.ajax({
            method:'PUT',
            url:"http://127.0.0.1:8000/api/comments/"+objectId+"/",
            data:formData,
            success:function(data){
              getComments(dataurl)             

            },
            error:function(data){
              var formErrorExists=$('.srvup-alert-error')
              var msg=formErrorMsg(data.responseJSON)
              $('[data-id="'+objectId+'"] textarea').before(msg)
            }
          })
        }
      })