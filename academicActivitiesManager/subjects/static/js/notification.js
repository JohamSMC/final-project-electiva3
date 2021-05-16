const URI_BASE =
"https://d7a304cf-a52d-460d-827a-e8efae6c9cfd.mock.pstmn.io";
const endPoint = "notificationTask";

const notificationCheckTask = async () => {
await fetch(`${URI_BASE}/${endPoint}`)
  .then((response) => response.json())
  .then((data) => showNotification(data.tasks))
  .catch((e) => console.log(`Error: ${e}`));
};

function showNotification(data){
let notification_area = document.getElementById("notification_area")
let template_alert_task = document.getElementById('template_alert_task').content;

data.forEach(task => {
    console.log(task)
    // Llenamos datos en el alert
    let alertText = template_alert_task.getElementById("alertText")
    alertText.textContent = task.name

    let clone = template_alert_task.cloneNode(true);
    let newAlert = clone.firstElementChild;
    notification_area.appendChild(newAlert);
    // Se encarga de eliminar automaticamente el alert
    setTimeout(function(){
            notification_area.removeChild(newAlert);
        },5000)
    });
}

//   setInterval(notificationCheckTask, 3000);