import csv

csvFile = open('input.csv', 'r')#enter the csv filename
#csvReader = csv.reader(csvFile)
#csvData = list(csvReader)

dd = []
csvData =  csvFile.readline() 
while csvData:
    dd += [ csvData ]
    csvData = csvFile.readline()
csvData = dd

with open('index.html', 'w') as html: #enter the output filename
    html.write('''
<head>
<link rel="stylesheet" href="bootstrap-table.min.css">
<link rel="stylesheet" href="bootstrap.min.css">
</head>
''')    

    html.write('<body>')
    html.write('<div class="container" style="margin: 5px 5px 5px 5px;height:60%;">')
    html.write('<div class="row">')
    
    
    html.write('<table data-toggle="table" data-pagination="true">')
    r = 0
    for row in csvData:
        if r == 0:
            html.write('<thead><tr>')
            for col in row.split(','):
                html.write('<th data-sortable="true">' + col + '</th>')
            html.write('</tr></thead>')
            html.write('<tbody>')
        else:
            html.write('<tr>')
            for col in row.split(','):
                html.write('<td>' + col + '</td>')
            html.write('</tr>')

        r += 1
    html.write('</tbody>')
    html.write('</table>')
    
    html.write('''
<script src="jquery-2.2.1.min.js"></script>
<script src="bootstrap.min.js"></script>
<script src="bootstrap-table.min.js"></script>
''')
    
    html.write('</div>') #/row
    html.write('</div>') #/container
    html.write('</body>')
