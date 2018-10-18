#!/usr/bin/env python
# -*- coding: utf-8 -*-

html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
<title>扫描结果</title>

<!-- DataTables CSS -->
<link href="https://cdnjs.cloudflare.com/ajax/libs/datatables/1.10.16/css/jquery.dataTables.css" rel="stylesheet">
<link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
<!--  <link href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.1.0/css/bootstrap.min.css" rel="stylesheet">
 -->
<!-- jQuery -->
<script type="text/javascript" charset="utf8" src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
 
<!-- DataTables -->
<script type="text/javascript" charset="utf8" src="http://cdn.datatables.net/1.10.15/js/jquery.dataTables.js"></script>

</head>
<body>

<h3 class="text-info">扫描结果</h3>
<!-- <table id="example" class="display" cellspacing="0" width="100%"> -->
<table id="example" class="display compact" style="width:100%">
    <thead>
        <tr>
            <th>Payload</th>
            <th>Status</th>
            <th>Length</th>
            <th>State</th>
        </tr>
    </thead>
</table>

<script type="text/javascript" src="data.js"></script>

<script type="text/javascript">
	$('#example').DataTable({
		// "lengthChange": false,
        "lengthMenu": [ [50, 100, -1],[50, 100, "所有"] ],
		// "paging": false,
		data: data,
	});
</script>

</body>
</html>'''