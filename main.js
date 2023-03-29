'use strict';
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


}

console.log(`Application Started`);

