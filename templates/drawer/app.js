let data = {"position": "2021-10-10"};
pr = fetch("/drawing/pixels", {
    method: "POST",
    headers: {'Content-Type': 'application/json'}
    body: JSON.stringify(data)
}
console.log(pr)
