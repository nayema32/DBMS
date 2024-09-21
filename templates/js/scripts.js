document.addEventListener('DOMContentLoaded', function() {
    // demo dynamic table resize if needed
    const tableContainer = document.querySelector('.table-container');
    const table = document.querySelector('.table');

    function adjustTable() {
        if (table.offsetWidth > tableContainer.offsetWidth) {
            table.style.width = '100%';
        } else {
            table.style.width = 'auto';
        }
    }

    window.addEventListener('resize', adjustTable);
    adjustTable();
});
