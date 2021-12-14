let the_url   = $("#input-pic").attr("url"); 
Dropzone.autoDiscover=false;
if ($('#DropzoneElementId').length) {
const myDropzone= new Dropzone('#my-dropzone',{
    url:the_url,
    maxFiles:5,
    maxFilesize:4,
    acceptedFiles:'.jpg',
})
}