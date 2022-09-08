/*
Template Name: Dason - Admin & Dashboard Template
Author: Themesdesign
Website: https://themesdesign.in/
Contact: themesdesign.in@gmail.com
File: Sparkline chart Init
*/


$(document).ready(function () {
    var SparklineCharts = function () {


        $("#sparkline4").sparkline([0, 23, 43, 35, 44, 45, 56, 37, 40, 45, 56, 7, 10], {
            type: 'line',
            width: '160',
            height: '30',
            lineColor: '#F48B00',
            fillColor: 'transparent',
            spotColor: 'transparent',
            lineWidth: 2,
            minSpotColor: undefined,
            maxSpotColor: undefined,
            highlightSpotColor: undefined,
            highlightLineColor: undefined,
            sparklineOptions: {
                tooltip: {
                    enabled: false, // removes sparkline tooltips
                }
            }
        });


    }
    var sparkResize;

    $(window).resize(function (e) {
        clearTimeout(sparkResize);
        sparkResize = setTimeout(SparklineCharts, 500);
    });
    SparklineCharts();

});