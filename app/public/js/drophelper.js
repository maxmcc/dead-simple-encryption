var myDropzone;

// initialize file drop
 Dropzone.options.myDropzone = {
    autoProcessQueue: true,
    init: function() {
        myDropzone = this; // closure

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

$("#encrypt").click(function() {
    console.log("hi");
    console.log(myDropzone.getAcceptedFiles());
    var data = {
        files: myDropzone.getAcceptedFiles(),
        };
        $.post(url = '/_upload', data = data);
});