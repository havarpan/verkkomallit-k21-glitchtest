// pidä kaikki ennallaan tämän rivin alla

const getJson = async function() {
  const data = await fetch("/ryhma2", {
    method: "POST"
  });
  const postedJson = JSON.parse(await data.json());
  renderJson(postedJson);
};
getJson();

const renderJson = function(data) {
  // console.log(data);
  var pre = document.createElement('pre')
  pre.textContent = JSON.stringify(data, null, 4)
  document.body.appendChild(pre)
};
