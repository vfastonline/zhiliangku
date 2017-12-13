tinymce.init({
    selector: "textarea",   // 选择该页面绑定的标签
    themes: "modern",
    menubar: false,
    convert_urls: false,
    height: 450,
    plugins: [
        'advlist autolink lists link image charmap print preview hr anchor pagebreak',
        'searchreplace wordcount visualblocks visualchars code fullscreen',
        'insertdatetime media nonbreaking save table contextmenu directionality',
        'emoticons template paste textcolor colorpicker textpattern imagetools',
        "link imageupload"
    ],
    toolbar: "undo redo | imageupload link | bold italic | styleselect fontselect fontsizeselect | bullist numlist outdent indent | alignleft aligncenter alignright alignjustify | print preview media | forecolor backcolor emoticons",
    content_css: [
        // '/static/tinymce/css/codepen.min.css'
    ],
    imageupload_url: '/upload?action=uploadimage',    // 指定图片上传处理目录
    language: 'zh_CN'
});