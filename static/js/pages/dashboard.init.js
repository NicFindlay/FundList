/*
Template Name: Dason - Admin & Dashboard Template
Author: Themesdesign
Website: https://themesdesign.in/
Contact: themesdesign.in@gmail.com
File: Dashboard Init Js File
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

//  MINI CHART

// mini-1
var barchartColors = getChartColorsArray("#mini-chart1");
var options = {
    series: [60, 40],
    chart: {
        type: 'donut',
        height: 110,
    },
    colors: barchartColors,
    legend: {
        show: false
    },
    dataLabels: {
        enabled: false
    }
};

var chart = new ApexCharts(document.querySelector("#mini-chart1"), options);
chart.render();

// mini-2
var barchartColors = getChartColorsArray("#mini-chart2");
var options = {
    series: [30, 55],
    chart: {
        type: 'donut',
        height: 110,
    },
    colors: barchartColors,
    legend: {
        show: false
    },
    dataLabels: {
        enabled: false
    }
};

var chart = new ApexCharts(document.querySelector("#mini-chart2"), options);
chart.render();

// mini-3
var barchartColors = getChartColorsArray("#mini-chart3");
var options = {
    series: [65, 45],
    chart: {
        type: 'donut',
        height: 110,
    },
    colors: barchartColors,
    legend: {
        show: false
    },
    dataLabels: {
        enabled: false
    }
};

var chart = new ApexCharts(document.querySelector("#mini-chart3"), options);
chart.render();

// mini-4
var barchartColors = getChartColorsArray("#mini-chart4");
var options = {
    series: [30, 70],
    chart: {
        type: 'donut',
        height: 110,
    },
    colors: barchartColors,
    legend: {
        show: false
    },
    dataLabels: {
        enabled: false
    }
};

var chart = new ApexCharts(document.querySelector("#mini-chart4"), options);
chart.render();


//
// Market Overview
//
var barchartColors = getChartColorsArray("#market-overview");
var options = {
    chart: {
        height: 350,
        type: 'area',
        toolbar: {
            show: false,
        }
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        curve: 'smooth',
        width: 3,
    },
    series: [{

    }],
    colors: splneAreaColors,
    xaxis: {
        type: 'datetime',
        categories: ["2018-09-19T00:00:00", "2018-09-19T01:30:00", "2018-09-19T02:30:00", "2018-09-19T03:30:00", "2018-09-19T04:30:00", "2018-09-19T05:30:00", "2018-09-19T06:30:00"],
    },
    grid: {
        borderColor: '#f1f1f1',
    },
    tooltip: {
        x: {
            format: 'dd/MM/yy HH:mm'
        },
    }
}

var chart = new ApexCharts(document.querySelector("#market-overview"), options);
chart.render();


//   spline_area
var splneAreaColors = getChartColorsArray("#spline_area");
var options = {
    chart: {
        height: 350,
        type: 'area',
        toolbar: {
            show: false,
        }
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        curve: 'smooth',
        width: 3,
    },
    series: [{
        name: 'series1',
        data: [34, 40, 28, 52, 42, 109, 100]
    }, {
        name: 'series2',
        data: [32, 60, 34, 46, 34, 52, 41]
    }],
    colors: splneAreaColors,
    xaxis: {
        type: 'datetime',
        categories: ["2018-09-19T00:00:00", "2018-09-19T01:30:00", "2018-09-19T02:30:00", "2018-09-19T03:30:00", "2018-09-19T04:30:00", "2018-09-19T05:30:00", "2018-09-19T06:30:00"],
    },
    grid: {
        borderColor: '#f1f1f1',
    },
    tooltip: {
        x: {
            format: 'dd/MM/yy HH:mm'
        },
    }
}

var chart = new ApexCharts(
    document.querySelector("#spline_area"),
    options
);

chart.render();

// MAp

var vectormapColors = getChartColorsArray("#sales-by-locations");
$('#sales-by-locations').vectorMap({
    map: 'world_mill_en',
    normalizeFunction: 'polynomial',
    hoverOpacity: 0.7,
    hoverColor: false,
    regionStyle: {
        initial: {
            fill: '#e9e9ef'
        }
    },
    markerStyle: {
        initial: {
            r: 9,
            'fill': vectormapColors,
            'fill-opacity': 0.9,
            'stroke': '#fff',
            'stroke-width': 7,
            'stroke-opacity': 0.4
        },

        hover: {
            'stroke': '#fff',
            'fill-opacity': 1,
            'stroke-width': 1.5
        }
    },
    backgroundColor: 'transparent',
    markers: [{
        latLng: [41.90, 12.45],
        name: 'USA'
    }, {
        latLng: [12.05, -61.75],
        name: 'Russia'
    }, {
        latLng: [1.3, 103.8],
        name: 'Australia'
    }]
});

