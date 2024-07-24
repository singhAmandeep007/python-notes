function deleteReminder(reminderId) {
  fetch("/delete-reminder", {
    method: "POST",
    body: JSON.stringify({ reminderId: reminderId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
