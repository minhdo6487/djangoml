$(document).ready(function(){

    $("#infocontent").hide();
    $("#infocontent div").hide();


    $('#linkwrapper a[id]').click(function(){

        var vsubmen = this.id +"content";

        if( $("#infocontent").is(":visible") == false ) {
            $("#" + vsubmen).show('fast',function() {
                $("#infocontent").slideDown();

            });
        } else if ( $("#" + vsubmen).is(":visible") == false ) {
            $("#infocontent").slideUp('slow',function(){
                $("#infocontent div").hide();
                $("#" + vsubmen).show();
                $("#infocontent").slideDown('slow');
            });
        } else {
            $("#infocontent").slideUp('slow',function(){
                $("#infocontent div").hide();
            });
        }
        return false;
    });

    });

    // $(document).ready(function(){
    //     $("submitButtonID").click(function(){
    //     var formData = {
    //      url_img_link : $('#urlimg').val(),
    //       };
    //         $.ajax({
    //             type: 'POST',
    //             url: "/blog/class_dog_cat/",
    //             dataType: 'text',
    //             data: formData,
    //             cache: false,
    //             success: function (data) {
    //                 alert(url_img_link);

    //             },
    //             error: function (data) {
    //                 //error
    //                 alert(url_img_link);
    //             }
    //         });
    //     });
    // });

    $(document).ready(function()
    {
        //khai báo nút submit form
        var submit   = $("button[type='submit']");

        //khi thực hiện kích vào nút Login
        submit.click(function()
        {
            //khai báo các biến
            // remove all in li
            $('#reslist').empty();
            var url_string = $("input[name='url_image']").val(); //lấy giá trị input

            if(url_image == ''){
                alert('Vui lòng nhập tài khoản');
                return false;
            } else {
              console.log(url_string);
              $("#lbType").html(url_string)

              $('#img_input').attr({
              'src': url_string,
              'alt': 'image'
              });
            }

            //lay tat ca du lieu trong form login
            var data = $('form#form_login').serialize();
            // su dung ham $.ajax()
            $.ajax({
            type : 'POST', //kiểu post
            url  : '/blog/classification_svm/',
            data : data,
            success :  function(data)
                   {

                        if(data == 'false')
                        {
                            alert('something wrong with url');
                        }else{
                            $('#content').html(data);

                            var res = data.split(",");
                            var reslist = document.getElementById("reslist");

                            $('#store_data').html(res)

                            res.forEach(function (res) {
                                var li = document.createElement("li");

                                li.textContent = res;
                                reslist.appendChild(li);
                            });
                        }
                   }
            });
            return false;
        });
    });
  </script>

  // <script type="text/javascript">
  // $(document).ready(function()
  // {
  //     //khai báo nút submit form
  //     var submit   = $("button[type='submit']");

  //     //khi thực hiện kích vào nút Login
  //     submit.click(function()
  //     {
  //         //khai báo các biến
  //         var username = $("input[name='username']").val(); //lấy giá trị input tài khoản
  //         var password = $("input[name='password']").val(); //lấy giá trị input mật khẩu

  //         //kiem tra xem da nhap tai khoan chua
  //         if(username == ''){
  //             alert('Vui lòng nhập tài khoản');
  //             return false;
  //         } else {
  //           console.log(username);
  //           $("#lbType").html(username)

  //           $('#img_input').attr({
  //           'src': username,
  //           'alt': 'image'
  //           });
  //         }

  //         //kiem tra xem da nhap mat khau chua
  //         if(password == ''){
  //             alert('Vui lòng nhập mật khẩu');
  //             return false;
  //         } else {
  //           console.log(password);
  //         }

  //         //lay tat ca du lieu trong form login
  //         var data = $('form#form_login').serialize();
  //         // su dung ham $.ajax()
  //         $.ajax({
  //         type : 'POST', //kiểu post
  //         url  : '/blog/class_dog_cat/', //gửi dữ liệu sang trang submit.php
  //         data : data,
  //         success :  function(data)
  //                {
  //                     if(data == 'false')
  //                     {
  //                         alert('Sai tên hoặc mật khẩu');
  //                     }else{
  //                         $('#content').html(data);
  //                         alert(data)
  //                     }
  //                }
  //         });
  //         return false;
  //     });
  // });
