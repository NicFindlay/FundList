/*
Template Name: Dason - Admin & Dashboard Template
Author: Themesdesign
Website: https://themesdesign.in/
Contact: themesdesign.in@gmail.com
File: Sparkline chart Init
*/

// get colors array from the string
function getChartColorsArray(chartId) {
    var colors = $(chartId).attr('data-colors');
    var colors = JSON.parse(colors);
    return colors.map(function (value) {
        var newValue = value.replace(' ', '');
        if (newValue.indexOf('--') != -1) {
            var color = getComputedStyle(document.documentElement).getPropertyValue(newValue);
            if (color) return color;
        } else {
            return newValue;
        }
    })
}

$(document).ready(function () {
    var SparklineCharts = function () {

        var sparkline4ChartColors = getChartColorsArray("#sparkline4");
        $("#sparkline4").sparkline([0, 23, 43, 35, 44, 45, 56, 37, 40, 45, 56, 7, 10], {
            type: 'line',
            width: '100%',
            height: '40',
            lineColor: sparkline4ChartColors,
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