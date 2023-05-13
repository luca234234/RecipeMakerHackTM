function DisplayGif(){
    const loader = document.querySelector('.loader-container');
    loader.classList.remove('d-none');
}


// function TakePhoto(context) {
//     context.drawImage(video, 0, 0, 640, 480);
//
//     document.getElementById("navbar").style.display = "none";
//     // Send the image data to the server
//     fetch("/predict", {
//       method: "POST",
//       headers: {
//         "Content-Type": "application/json",
//       },
//       body: JSON.stringify({ image: imageData }),
//     });
// }
//
// const constraints = {
//     audio: false,
//     video: {
//       facingMode: "environment", // Use the rear camera if available
//     },
// };
//
// // Get access to the camera!
// if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
//     navigator.mediaDevices
//       .getUserMedia(constraints)
//       .then(function (stream) {
//         // Video is streamed to the video element
//         let video = document.getElementById("video");
//         video.srcObject = stream;
//         video.play();
//
//         // Elements for taking the snapshot
//         let canvas = document.getElementById("canvas");
//         let context = canvas.getContext("2d");
//         TakePhoto(context);
//       })
//       .catch(function (err) {
//         console.log(err.name + ": " + err.message);
//       }); // Always check for errors at the end.
// }