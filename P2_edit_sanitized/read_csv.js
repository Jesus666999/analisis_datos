let rows = []
let header = ""
document.getElementById('fileInput').addEventListener('change', function (event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            const content = e.target.result;
            rows = content.split("\n");
            header = rows.shift();
            rows.pop();
            let table_header = $("#table_header");
            table_header.text("");
            let header_elements = header.split(",");
            header_elements.forEach(h_elem => {
                let th = $("<th>").text(h_elem)//.attr({"class" : "sticky-top"});
                table_header.append(th);
            });
            let table = $("#file_content");
            table.text("");
            rows.forEach(row => {
                row = row.split(",");
                let tableRow = $("<tr>");
                tableRow.attr({ "onclick": "highlightRow(this)" });
                row.forEach(row_element => {
                    let tableInput = $("<td>").append($("<input></input>").val(row_element).attr({ "class": "form-control" }));
                    tableRow.append(tableInput);
                });
                table.append(tableRow);
            });
        };
        reader.readAsText(file);
    }
});

function highlightRow(row) {
    console.log(row)
    const allRows = document.querySelectorAll('tr');
    allRows.forEach(r => r.classList.remove('table-dark'));
    row.classList.add("table-dark");
}

function saveFile() {
    console.log("Function executed...");
    let cajones = $(".form-control");
    let count = 0;
    let row = "";
    let csv_data = header + "\n";
    if (cajones.length == 1) {
        alert("Por favor, abra un archivo para modificar");
    } else {
        for (let i = 1; i <= cajones.length - 1; i++) {
            count++;
            if (count == 6) {
                row += cajones[i].value;
                csv_data += row + "\n";
                row = "";
                count = 0;
            } else {
                row += cajones[i].value + ",";
            }
        }
        downloadTextFile(csv_data);
    }
}

function downloadTextFile(csvData) {
    var blob = new Blob([csvData], { type: 'text/csv' });
    var link = document.createElement('a');
    link.href = URL.createObjectURL(blob);
    link.download = 'not_accepted_data.csv';
    link.click();
}