// initialize file drop
 Dropzone.options.myDropzone = {
    autoProcessQueue: false,
    init: function() {
        var submitButton = $("#encrypt");
        myDropzone = this; // closure

        submitButton.addEventListener("click", function() {
            //myDropzone.processQueue(); 
            console.log("hi");
            console.log(myDropzone.getAcceptedFiles());
            var data = {
                files: myDropzone.getAcceptedFiles(),
            };
            $.post(url = '/_upload', data = data);
            myDropzone.processQueue();
        });
        
        this.on("success", function(file,responsenew) {
                     // alert(responsenew);
                     var response = jQuery.parseJSON(responsenew);
            console.log(response);
        });


        this.on("addedfile", function(file){
            var removeButton = Dropzone.createElement("<button>Remove file</button>");
            var _this = this;
            removeButton.addEventListener("click", function(e) {
                e.preventDefault();
                e.stopPropagation();

                // Remove the file preview.
                _this.removeFile(file);
                // TODO ADD AJAX REMOVAL FROM SERVER
            });

            file.previewElement.appendChild(removeButton);
        });
    }
}