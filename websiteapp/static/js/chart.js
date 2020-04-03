function getchart(devicename, chartname, times, values, measure) {
    var ctx = document.getElementById(chartname);
    var myChart = new Chart(ctx, 
        { 
            type: 'line',
            data: 
            { 
                labels: times, datasets: 
                [
                { 
                    data: values, 
                    label: devicename, 
                    cubicInterpolationMode: 'monotone' 
                } 
                ] 
            }, 
            options: 
            {
                legend:
                {
                    display: false
                } ,
                scales: 
                {
                    xAxes: 
                    [
                    {
                        scaleLabel: {
                            display: true,
                            labelString: 'Datetime',
                            fontSize: 30,
                        },
                        ticks: {
                            fontSize: 15
                        }, 
                        type: 'time',
                        distribution: 'series'
                    }
                    ],
                    yAxes: 
                    [
                    {
                        scaleLabel: {
                            display: true,
                            labelString: measure,
                            fontSize: 30,
                        },
                        ticks: {
                            fontSize: 20
                        }, 
                    }
                    ]
                }
            } 
        }
    )
}