async function loadEmployees() {

    try {

        const response =
            await fetch("/employees");

        const employees =
            await response.json();

        const table =
            document.getElementById(
                "employeeTable"
            );

        table.innerHTML = "";

        employees.forEach(emp => {

            table.innerHTML += `
                <tr>
                    <td>${emp.id}</td>
                    <td>${emp.name}</td>
                    <td>${emp.type}</td>
                    <td>${emp.weekly_pay}</td>
                </tr>
            `;
        });

    }

    catch(error) {

        console.log(error);

        alert(
            "Failed to load employees!"
        );
    }
}