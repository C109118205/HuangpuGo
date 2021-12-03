    // <div> 元素的 DOM ID (這邊注意如果沒特別給定值，則要lat(緯度)在前 )
    let map = L.map('map').setView([
        22.618794358690458, // latitude(緯度)
        120.36315781103444 // longitude(經度)
      ], 18 // zoom(地圖的縮放，值越大->放大；反之縮小)
    );
    
  
    //  定義tileLayer(圖磚)，目前使用為 openstreetmap的底圖(也可以選擇其他底圖)
    let osm_tileLayer =  L.tileLayer('https://{s}.tile.openstreetmap.fr/osmfr/{z}/{x}/{y}.png', {
  maxZoom: 20,
    attribution: '&copy; OpenStreetMap France | &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

document.getElementById("fitBounds-btn").addEventListener("click", function () {
  map.fitBounds([
    [22.61845121771776, 120.36157807451778],
    [22.617700274719702, 120.3661117505427]
  ]);
});
