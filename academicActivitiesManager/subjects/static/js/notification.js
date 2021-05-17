// const URI_BASE =
//   "https://d7a304cf-a52d-460d-827a-e8efae6c9cfd.mock.pstmn.io";
// const URI_BASE = "{% url 'subjects:notification_task' %}";
const URI_BASE = "/notification_task/";
// const endPoint = "notificationTask";

const notificationCheckTask = async () => {
  await fetch(`${URI_BASE}`)
    .then((response) => response.json())
    // .then((data) => console.log(data.tasks))
    .then((data) => showNotification(data.tasks))
    .catch((e) => console.log(`Error: ${e}`));
};

function showNotification(data) {
  let notification_area = document.getElementById("notification_area")
  let template_alert_task = document.getElementById('template_alert_task').content;

  data.forEach(task => {
    console.log(task)
    // Llenamos datos en el alert
    // debugger
    let alertName = template_alert_task.getElementById("alertName")
    let alertDateFinish = template_alert_task.getElementById("alertDateFinish")
    let alertTimeRest = template_alert_task.getElementById("alertTimeRest")
    let class_alert = template_alert_task.getElementById("class_alert")

    alertName.textContent = task.name
    alertDateFinish.textContent = task.date_finished
    alertTimeRest.textContent = time_restant(task.time_rest)

    class_alert = change_class_alert(class_alert, task.time_rest)

    let clone = template_alert_task.cloneNode(true);
    let newAlert = clone.firstElementChild;
    notification_area.appendChild(newAlert);
    // Se encarga de eliminar automaticamente el alert
    setTimeout(function () {
      notification_area.removeChild(newAlert);
    }, 5000)
  });
}

function showOneNotification({ title, message, class_to_add }) {
  let notification_area = document.getElementById("notification_normal")
  let template_alert = document.getElementById('template_alert').content;

  // Llenamos datos en el alert
  let alerTitle = template_alert.getElementById("alerTitle")
  let alertMessage = template_alert.getElementById("alertMessage")
  let class_alert = template_alert.getElementById("class_alert")

  alerTitle.textContent = title
  alertMessage.textContent = message
  class_alert.classList.add(class_to_add)

  let clone = template_alert.cloneNode(true);
  let newAlert = clone.firstElementChild;
  notification_area.appendChild(newAlert);
  // Se encarga de eliminar automaticamente el alert
  setTimeout(function () {
    notification_area.removeChild(newAlert);
  }, 5000)
}

const time_restant = (time_rest) => {
  let message = ""
  if (time_rest > 1) {
    message = "Quedan " + (time_rest) + " dias"
  }
  else if (time_rest == 1) {
    message = "Mañana"
  }
  else if (time_rest == -1) {
    message = "Hace " + (time_rest * -1) + " dia"
  }
  else if (time_rest == 0) {
    message = "Hoy"
  }
  else {
    message = "Hace " + (time_rest * -1) + " dias"
  }
  return message
}

const change_class_alert = (class_alert, time_rest) => {
  if (time_rest > 1) {

    class_alert.classList.remove('alert-warning')
    class_alert.classList.remove('alert-danger')
    class_alert.classList.add('alert-success')
  }
  else if ((time_rest == 1) || (time_rest == 0)) {

    class_alert.classList.remove('alert-success')
    class_alert.classList.remove('alert-danger')
    class_alert.classList.add('alert-warning')
  }
  else if (time_rest < 0) {
    class_alert.classList.remove('alert-success')
    class_alert.classList.remove('alert-warning')
    class_alert.classList.add('alert-danger')
  }
  return class_alert
}
setInterval(notificationCheckTask, 15000);