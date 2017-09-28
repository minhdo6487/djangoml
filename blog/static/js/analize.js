$(document).ready(function(){

    $("#infocontent").hide();
    $("#infocontent div").hide();


    $('#linkwrapper a[id]').click(function(){

        var vsubmen = this.id +"content";

        if( $("#infocontent").is(":visible") == false ) {
            $("#" + vsubmen).show('fast',function() {
//                $("#infocontent").slideDown();
                $("#infocontent").fadeIn();
                if($('#image_upload').attr('src') != '/media/images/'){
                    $("#image_upload").show();
//                      alert("actulaly image will show")
                }
            });
        } else if ( $("#" + vsubmen).is(":visible") == false ) {
//            $("#infocontent").slideUp('slow',function(){
            $("#infocontent").fadeOut('slow',function(){
                $("#infocontent div").hide();
                $("#" + vsubmen).show();
//                $("#infocontent").slideDown('fast');
                $("#infocontent").fadeIn('fast');
            });
        } else {
//            $("#infocontent").slideUp('fast',function(){
            $("#infocontent").fadeOut('fast',function(){
                $("#infocontent div").hide();

            });
        }
        return false;
    });

    });


    $(document).ready(function()
    {


        var submit   = $("button#button_login[type='submit']");

        //khi thực hiện kích vào nút Login
        submit.click(function()
        {

            $('#img_gif').show(); //<----here
            // alert("hong")
            $('#reslist').empty();
            var url_string = $("input[name='url_image']").val(); //lấy giá trị input
//            alert(document.getElementById("url_image").files[0].name)

            if(url_image == ''){
                alert('please type Image url');
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
                        $('#img_gif').show();
                        // $("#image_upload").show();

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
                                $('#img_gif').hide();
                            });
                        }
                   }
            });
            return false;
        });
    });



    $(document).on('click','input#butonID',function (event) {
        $("#modal-progress").modal("show");
        var data = $('form#form_upload').serialize();
        $.ajax({
            type: "POST",
            data: data,
            url: '/blog/result/',
            success: function(data)
            {
                // $("#image_upload").show();
                if(data == 'false')
                {
                    alert('something wrong with url');
                }else{
                    $('#img_gif').hide();
                };
            }
        });



    });

