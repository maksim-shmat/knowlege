"""Table examples. CSS & HTML"""

#1 

CSS

table {display: table;}
tr {display: table-row;}
thead {display: table-header-group;}
tbody {display: table-row-group;}
tfoot {display: table-footer-group;}
col {display: table-column;}
colgroup {display: table-cell;}
td, th {display: table-cell;}
caption {display: table-caption;}

scores {display: table;}
headers {display: table-header-group;}
game {display: table-row-group;}
team {display: table-row;}
lable, name, score {display: table-cell;}

HTML

<scores>
  <headers>
    <label>Team</label>
    <label>Score</label>
  </headers>
  <game sport="MLB" league="NL">
    <team>
      <name>Socks</name>
      <score>18</score>
    </team>
    <team>
      <name>Bubs</name>
      <score>9</score>
    </team>
  </game>
</scores>

#2 Заголовок таблицы

caption {background: yellow; margin: lem 0; caption-side: top; text-align: left;}
table {color: white; background: gray; margin: 0.5em 0;}

#3 
<table border="3" cellpadding="7" cellspacing="3" height="80" width="50%">
	<caption>
		Simple table example
	</caption>
	<thead>
		<tr>
			<th></th>
			<th>First Column Header</th>
			<th>Second Column Header</th>
			<th>And So On, Ad Museum</th>
		<tr>
	</thead>
	<tbody>
		<tr align="center">
			<th>Juppa</th>
			<td>1.1</td>
			<td>1.2</td>
			<td>1.3</td>
		</tr>
		<tr align="center">
			<th>Pstruppe</th>
			<td align="center">2.1</td>
			<td align="right">2.2</td>
			<td>2.3</td>
		</tr>
	</tbody>
	<tfoot>
		<tr>
			<th>Totals</th>
			<th>100</th>
			<th>220</th>
			<th>100500</th>
		</tr>
	</tfoot>
</table>

#4
<table width="760" cellpadding="10" cellspacing="10" border="1">
	<tbody>
		<tr>
			<td align="center">LOGO</td>
			<td rowspan="2">Basicaly content</td>
		</tr>
		<tr>
			<td>Menu</td>
		</tr>
	</tbody>
</table>

#5
<table width="100%" cellpadding="10" cellspacing="10" border="0">
	<tbody>
		<tr align="center">
			<td colspan="3">Header</td>
		</tr>
		<tr>
			<td width="200px">Menu</td>
			<td width="*">Base content</td>
			<td width="200px">Other futures</td>
		</tr>
		<tr align="center">
			<td colspan="3">Cellar of site</td>
		</tr>
	</tbody>
</table>

#6
<table>
	<thead>
		<style>
		table, th, td:nth-child(2) {
			border: 1px solid black;
			border-collapse: collapse;
			padding: 5px;
		}
		caption {
			caption-side: bottom;
		}
		</style>
		<caption>Table 57: Current product inventory.</caption>
		<tr>
			<th></th>
			<th>Idiom</th>
			<th>Part of Seech</th>
			<th>Definition</th>
	</thead>
	<tbody>
		<tr>
			<th style="text-align: left; vertical-align: top;">
				One
			</th>
			<td style="text-align: center; vertical-align: bottom;">
				col1
			</td>
			<td style="text-align: right; vertical-align: middle;">
				column2
			</td>
			<td style="text-align: justify; width: 200px;">
				An imaginary boundary that separates urban
				sophisticates from those with simple,
				traditional, or unconsciously urges.
			</td>
		</tr>
	</tbody>
</table>
