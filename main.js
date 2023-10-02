'use strict';
var xhr = new XMLHttpRequest();
const pica = require("pica");
const MI = require("merge-images");
const ls = require("looks-same");
const cropperjs = require("cropperjs");

const picaApi = new pica();
const MIAPI = new MI();
const lsAPI = ls();
const cropperjsAPI = cropperjs();

function MergeImage(image1, image2) 
{
    imageresult = MIAPI.MergeImage(image1, image2);
    return imageresult
}
function GetRobloxImage(userid){
    xhr.open('GET', 'https://example.com/api/data', true);

    xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        console.log(response); // Now you can work with the JSON data
      }
    };
    

}


xhr.send();


console.log(`Application Started`);

