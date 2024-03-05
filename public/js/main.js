console.log('Hello from main.js');
function publishEvent(eventName, data) {
  console.log('Publishing event: ' + eventName);
  var event = new CustomEvent(eventName, {detail: data});
  window.dispatchEvent(event);
}